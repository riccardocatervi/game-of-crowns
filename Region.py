from dataclasses import dataclass

from Cell import Cell
from CellState import CellState
from RegionID import RegionID



@dataclass(frozen=True)
class Region:
    id: RegionID
    cells: tuple[Cell, ...] 

    def count_crowns(self) -> int:
        return sum(1 for cell in self.cells
                   if cell.state is CellState.CROWN)
    
    def has_exactly_one_crown(self) -> bool:
        return self.count_crowns() == 1 
    
    def get_empty_cells(self) -> tuple[Cell, ...]:
        return tuple(
            cell for cell in self.cells
                     if cell.state is CellState.EMPTY)
    
    def possible_positions(self) -> list[Cell]:
        return list(self.get_empty_cells())
    
    def contains(self, cell: Cell) -> bool:
        return True if cell in self.cells else False
    


        

    
    


    