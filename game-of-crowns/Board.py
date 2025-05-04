from dataclasses import dataclass
from typing import ClassVar

from RegionID import RegionID
from Region import Region
from Cell import Cell
from CellState import CellState


@dataclass(frozen=True)
class Board:
    rows: int
    cols: int
    grid: tuple[tuple[Cell, ...], ...]
    regions: tuple[Region, ...]
    _region_lookup: dict[RegionID, Region]
    
    DIRS: tuple[tuple[int, int], ...] = (
        (-1,  0), #N
        (-1, -1), #NW
        (-1, +1), #NE
        ( 0, -1), #E
        ( 0, +1), #W
        (+1,  0), #S
        (+1, -1), #SW
        (+1, +1), #SE
    )

    def get_cell_at(self, row: int, col: int) -> Cell:
        return self.grid[row][col]
    
    def get_region_of(self, cell: Cell) -> Region:
        return self._region_lookup[cell.get_region_id()]

    def get_neighbors_of(self, cell: Cell) -> tuple[Cell, ...]:
        current_row, current_col = cell.get_row(), cell.get_col()
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
        new_grid = self.with_new_grid(row, col)


    def with_new_grid(self, row: int, col: int) -> tuple[tuple[Cell, ...], ...]:
        mutable_grid = [ list(row) for row in self.grid ]
        
        old_cell = mutable_grid[row][col]
        new_cell = old_cell.with_state(new_state)

        mutable_grid[row][col] = new_cell

        return tuple(tuple(r) for r in mutable_grid)

    


        




