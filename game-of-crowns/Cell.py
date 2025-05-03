from dataclasses import dataclass

from CellState import CellState
from Region import Region
from RegionID import RegionID

@dataclass(frozen=True)
class Cell:
    row: int
    col: int
    region_id: RegionID
    state: CellState

    def get_row(self) -> int:
        return self.row
    
    def get_col(self) -> int:
        return self.col

    def get_region_id(self) -> RegionID:
        return self.region

    def get_state(self) -> CellState:
        return self.state
    
    def with_state(self, new_state: CellState) -> "Cell":
        return Cell(self.row, self.col, self.region_id, new_state)
    

    

