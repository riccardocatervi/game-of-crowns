import pytest

from game_of_crowns.Cell import Cell
from game_of_crowns.CellState import CellState
from game_of_crowns.RegionID import RegionID

@pytest.fixture
def sample_cell():
     return Cell(row=0, col=0, region_id=RegionID("R"), state=CellState.EMPTY)


def test_initial_attributes(sample_cell):
    assert sample_cell.row == 0
    assert sample_cell.col == 0
    assert sample_cell.region_id == RegionID("R")
    assert sample_cell.state is CellState.EMPTY


def test_with_state_returns_new_object(sample_cell):
    new = sample_cell.with_state(CellState.CROWN)
    assert new is not sample_cell
    assert new.state is CellState.CROWN
    assert sample_cell.state is CellState.EMPTY


def test_chain_with_state(sample_cell):
    c1 = sample_cell.with_state(CellState.BLOCKED)
    c2 = c1.with_state(CellState.CROWN)
    assert sample_cell.state is CellState.EMPTY
    assert c1.state is CellState.BLOCKED
    assert c2.state is CellState.CROWN
