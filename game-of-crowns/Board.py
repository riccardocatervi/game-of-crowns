from dataclasses import dataclass

from RegionID import RegionID
from Region import Region
from Cell import Cell

@dataclass(frozen=True)
class Board:
    rows: int
    cols: int
    grid: tuple[tuple[Cell, ...], ...]
    regions: tuple[Region, ...]
    _region_lookup: dict[RegionID, Region] = None
    DIRS: tuple[tuple[int, int], ...] = (
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1),
    )

    def __post_init__(self) -> None:
            if len(self.grid) != self.rows:
                raise ValueError("Row count mismatch")
            for i, row in enumerate(self.grid):
                if len(row) != self.cols:
                    raise ValueError(f"Row {i} col count mismatch")

            lookup: dict[RegionID, Region] = {}
            for region in self.regions:
                if region.id in lookup:
                    raise ValueError(f"Duplicate RegionID {region.id}")
                lookup[region.id] = region
            object.__setattr__(self, "_region_lookup", lookup)

            seen = set()
            for region in self.regions:
                for cell in region.cells:
                    if cell in seen:
                        raise ValueError("Cell presente in due regioni")
                    seen.add(cell)
                    if self.grid[cell.row][cell.get_col()] is not cell:
                        raise ValueError(
                            f"Grid mismatch at ({cell.get_row()},{cell.get_col()})"
                        )

    def get_neighbors(self, cell: Cell) -> tuple[Cell, ...]:
        nr, nc = cell.get_row(), cell.get_col()
        return tuple(
            self.grid[r][c]
            for dr, dc in self.DIRS 
            if 0 <= (r := nr + dr) < self.rows
            if 0 <= (c := nc + dc) < self.cols
        )
    
    def conflicting_crowns(self) ->
        
