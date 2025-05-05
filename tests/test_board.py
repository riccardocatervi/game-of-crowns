import pytest

from game_of_crowns.Board import Board
from game_of_crowns.Cell import Cell
from game_of_crowns.CellState import CellState
from game_of_crowns.Region import Region
from game_of_crowns.RegionID import RegionID

@pytest.fixture
def simple_board():
    rid = RegionID("R")
    cells = {(r, c): Cell(r, c, rid, CellState.EMPTY)
             for r in range(2) for c in range(2)}
    grid = tuple(tuple(cells[(r, c)] for c in range(2)) for r in range(2))
    region = Region(rid, tuple(cells.values()))
    return Board(2, 2, grid, (region,))


def test_get_neighbors_of(simple_board):
    b = simple_board
    cell = b.get_cell_at(0, 0)
    neigh = b.get_neighbors_of(cell)
    assert len(neigh) == 3 
    expected = {b.get_cell_at(0, 1), b.get_cell_at(1, 0), b.get_cell_at(1, 1)}
    assert set(neigh) == expected  
    cell_c = b.get_cell_at(1, 1)
    neigh_c = b.get_neighbors_of(cell_c)
    assert len(neigh_c) == 3
    expected_c = {b.get_cell_at(0,0), b.get_cell_at(0,1), b.get_cell_at(1,0)}
    assert set(neigh_c) == expected_c



def test_with_cell_state_immutability_and_region(simple_board):
    b1 = simple_board
    b2 = b1.with_cell_state(0, 0, CellState.CROWN)
    assert b1.get_cell_at(0, 0).state is CellState.EMPTY
    assert b2.get_cell_at(0, 0).state is CellState.CROWN
    region = b2.get_region_of(b2.get_cell_at(0, 0))
    assert region.count_crowns() == 1
    assert region.has_exactly_one_crown()


def test_conflicting_crowns_and_is_solved(simple_board):
    b = simple_board
    b_conf = b.with_cell_state(0, 0, CellState.CROWN)
    b_conf = b_conf.with_cell_state(0, 1, CellState.CROWN)
    conflicts = b_conf.conflicting_crowns()
    assert len(conflicts) == 1
    pair = conflicts[0]
    assert {pair[0].row, pair[1].row} == {0}  
    assert not b_conf.is_solved

    b_sol = b.with_cell_state(1, 1, CellState.CROWN)
    assert b_sol.conflicting_crowns() == ()
    assert b_sol.is_solved


def test_conflicting_crowns_empty(simple_board):
    assert simple_board.conflicting_crowns() == ()
    assert not simple_board.is_solved
