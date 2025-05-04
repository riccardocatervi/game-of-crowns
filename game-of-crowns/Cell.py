from dataclasses import dataclass

from CellState import CellState
from Region import Region
from RegionID import RegionID

@dataclass(frozen=True)
class Cell:
    _row: int
    _col: int
    _region_id: RegionID
    _state: CellState

    def get_row(self) -> int:
        return self._row
    
    def get_col(self) -> int:
        return self._col

    def get_region_id(self) -> RegionID:
        return self._region

    def get_state(self) -> CellState:
        return self._state
    
    def with_state(self, new_state: CellState) -> "Cell":
        return Cell(self._row, self._col, self._region_id, new_state)
    

    

