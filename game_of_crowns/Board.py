from dataclasses import dataclass, field
from typing import ClassVar

from game_of_crowns.RegionID import RegionID
from game_of_crowns.Region import Region
from game_of_crowns.Cell import Cell
from game_of_crowns.CellState import CellState


@dataclass(frozen=True)
class Board:
    rows: int
    cols: int
    grid: tuple[tuple[Cell, ...], ...]
    regions: tuple[Region, ...]
    _region_lookup: dict[RegionID, Region] = field(init=False, repr=False, compare= False)
    
    DIRS: ClassVar[tuple[tuple[int, int], ...]] = (
        (-1,  0), #N
        (-1, -1), #NW
        (-1, +1), #NE
        ( 0, -1), #E
        ( 0, +1), #W
        (+1,  0), #S
        (+1, -1), #SW
        (+1, +1), #SE
    )

    def __post_init__(self) -> None:
        lookup = {region.id: region for region in self.regions}
        object.__setattr__(self, "_region_lookup", lookup)

    def get_cell_at(self, row: int, col: int) -> Cell:
        return self.grid[row][col]
    
    def get_region_of(self, cell: Cell) -> Region:
        return self._region_lookup[cell.region_id]

    def get_neighbors_of(self, cell: Cell) -> tuple[Cell, ...]:
        current_row, current_col = cell.row, cell.col
        neighbors: list[Cell] = []
        for delta_row, delta_col in self.DIRS:
            new_row, new_col = current_row + delta_row, current_col + delta_col
            if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                neighbors.append(self.grid[new_row][new_col])
        return tuple(neighbors)
    
    def conflicting_crowns(self) -> tuple[tuple[Cell, Cell], ...]:
        pairs = {
            tuple(sorted((cell, neigh), key=lambda c: (c.row, c.col)))
            for row in self.grid
            for cell in row
            if cell.state is CellState.CROWN
            for neigh in self.get_neighbors_of(cell)
            if neigh.state is CellState.CROWN
        }
        return tuple(pairs)
    
    def with_cell_state(self, row: int, col: int, new_state: CellState) -> "Board":
        mutable_grid = [ list(row) for row in self.grid ]
        old_cell = mutable_grid[row][col]
        new_cell = old_cell.with_state(new_state)
        mutable_grid[row][col] = new_cell
        new_grid = tuple(tuple(row) for row in mutable_grid)
        
        mutable_regions = []
        for region in self.regions:
            if old_cell in region.cells:
                new_cells = tuple(new_cell if c is old_cell else c for c in region.cells)
                mutable_regions.append(Region(region.id, new_cells))
            else:
                mutable_regions.append(region)
        new_regions = tuple(mutable_regions)

        return Board(self.rows, self.cols, new_grid, new_regions)
    
    @property
    def is_solved(self) -> bool:
        if not all(region.has_exactly_one_crown() for region in self.regions):
            return False
        
        if self.conflicting_crowns():
            return False
        
        row_lines = [[ self.get_cell_at(r,c) for c in range(self.cols) ]
                     for r in range(self.rows)]
        col_lines = [[ self.get_cell_at(r,c) for r in range(self.rows) ]
                     for c in range(self.cols)]

        return self._one_crown_per_line(row_lines) and \
               self._one_crown_per_line(col_lines)
    
    def _one_crown_per_line(self, lines: list[list[Cell]]) -> bool:
        return all(
            sum(1 for cell in line if cell.state is CellState.CROWN) == 1
            for line in lines
        )

