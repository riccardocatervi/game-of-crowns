import pytest

from game_of_crowns.Region import Region
from game_of_crowns.Cell import Cell
from game_of_crowns.CellState import CellState
from game_of_crowns.RegionID import RegionID

@pytest.fixture
def sample_cells_and_region():
    rid = RegionID("R")
    c1 = Cell(row=0, col=0, region_id=rid, state=CellState.CROWN)
    c2 = Cell(row=0, col=1, region_id=rid, state=CellState.EMPTY)
    c3 = Cell(row=0, col=2, region_id=rid, state=CellState.BLOCKED)
    region = Region(rid, (c1, c2, c3))
    return c1, c2, c3, region


def test_count_crowns(sample_cells_and_region):
    c1, c2, c3, region = sample_cells_and_region
    assert region.count_crowns() == 1


def test_has_exactly_one_crown_true(sample_cells_and_region):
    c1, c2, c3, region = sample_cells_and_region
    assert region.has_exactly_one_crown() is True


def test_has_exactly_one_crown_false(sample_cells_and_region):
    c1, c2, c3, region = sample_cells_and_region
    region2 = Region(region.id, (c1, c2.with_state(CellState.CROWN), c3))
    assert region2.has_exactly_one_crown() is False


def test_get_empty_cells(sample_cells_and_region):
    c1, c2, c3, region = sample_cells_and_region
    empty_cells = region.get_empty_cells()
    assert empty_cells == (c2,)


def test_possible_positions(sample_cells_and_region):
    c1, c2, c3, region = sample_cells_and_region
    poss = region.possible_positions()
    assert isinstance(poss, list)
    assert poss == [c2]


def test_contains(sample_cells_and_region):
    c1, c2, c3, region = sample_cells_and_region
    assert region.contains(c1) is True
    assert region.contains(c2) is True
    assert region.contains(c3) is True
    other = Cell(row=1, col=1, region_id=RegionID("R"), state=CellState.EMPTY)
    assert region.contains(other) is False
