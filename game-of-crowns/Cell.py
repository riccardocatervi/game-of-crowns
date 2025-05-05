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
    
    def with_state(self, new_state: CellState) -> "Cell":
        return Cell(self.row, self.col, self.region_id, new_state)
    

    

