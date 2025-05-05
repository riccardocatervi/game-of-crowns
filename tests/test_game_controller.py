import pytest

from game_of_crowns.GameController import GameController
from game_of_crowns.CellState import CellState
from game_of_crowns.GameState import GameState

def sample_puzzle_dict():
    return {
        "height": 2,
        "width": 2,
        "regions": {"R": [[0,0],[0,1],[1,0],[1,1]]}
    }

@pytest.fixture
def controller():
    gc = GameController(None)
    gc.load_puzzle(sample_puzzle_dict())
    return gc


def test_load_puzzle_sets_playing_and_empty_history(controller):
    assert controller.game_state is GameState.PLAYING
    assert controller.history == []


def test_place_state_updates_board_and_history(controller):
    # initially empty
    b0 = controller.current_board
    # place a crown at (0,0)
    ok = controller.place_state(0, 0, CellState.CROWN)
    assert ok
    # history should contain previous board
    assert controller.history == [b0]
    # current_board should have crown
    assert controller.current_board.get_cell_at(0,0).state is CellState.CROWN
    # state remains PLAYING until solved
    assert controller.game_state is GameState.SOLVED


def test_undo_reverts_last_move(controller):
    controller.place_state(0,0, CellState.BLOCKED)
    # undo should succeed
    undone = controller.undo()
    assert undone
    # history emptied
    assert controller.history == []
    # board returned to initial state
    assert controller.current_board.get_cell_at(0,0).state is CellState.EMPTY


def test_undo_fails_when_no_history(controller):
    # fresh controller, no moves
    assert not controller.undo()


def test_reset_clears_history_and_board(controller):
    controller.place_state(0,1, CellState.CROWN)
    controller.place_state(1,1, CellState.BLOCKED)
    # reset
    controller.reset()
    # history cleared
    assert controller.history == []
    # board back to initial empty
    for r in range(controller.current_board.rows):
        for c in range(controller.current_board.cols):
            assert controller.current_board.get_cell_at(r,c).state is CellState.EMPTY
    # state returns to PLAYING or NOT_STARTED according to spec
    assert controller.game_state in (GameState.PLAYING, GameState.NOT_STARTED)


def test_no_moves_allowed_when_solved(controller):
    # solve by placing exactly one crown in the only region
    # single region of 4 cells must have exactly one crown
    controller.place_state(0,0, CellState.CROWN)
    assert controller.current_board.is_solved
    # now further moves are rejected
    assert not controller.place_state(1,1, CellState.CROWN)

