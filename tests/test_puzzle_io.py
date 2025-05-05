import json
import pytest

from game_of_crowns.PuzzleIO import PuzzleIO
from game_of_crowns.CellState import CellState
from game_of_crowns.RegionID import RegionID
from game_of_crowns.Cell import Cell
from game_of_crowns.Region import Region
from game_of_crowns.Board import Board

# Sample puzzle dictionary as provided by challenge format
def sample_dict():
    return {
        "height": 2,
        "width": 2,
        "regions": {
            "red": [[0,0], [0,1]],
            "blue": [[1,0], [1,1]]
        }
    }


def test_board_from_dict_and_dump_to_dict():
    data = sample_dict()
    # Load into Board
    board = PuzzleIO.load_from_dict(data)
    # Check basic board properties
    assert isinstance(board, Board)
    assert board.rows == 2
    assert board.cols == 2
    # All cells initially EMPTY
    for r in range(2):
        for c in range(2):
            assert board.get_cell_at(r, c).state is CellState.EMPTY
    # Dump back to dict
    out = PuzzleIO.dump_to_dict(board)
    # Regions match original
    assert out["regions"] == data["regions"]
    # No crowns or blocked in a fresh board
    assert out["crowns"] == []
    assert out["blocked"] == []
    # Height/width preserved
    assert out["height"] == data["height"]
    assert out["width"] == data["width"]


def test_load_and_dump_json_file(tmp_path):
    data = sample_dict()
    # Write JSON file
    puzzle_file = tmp_path / "puzzle.json"
    puzzle_file.write_text(json.dumps(data))
    # Load from file
    board = PuzzleIO.load_from_json_file(str(puzzle_file))
    assert board.rows == 2 and board.cols == 2
    # Modify board: place one crown and one blocked
    b2 = board.with_cell_state(0, 0, CellState.CROWN).with_cell_state(1, 1, CellState.BLOCKED)
    # Dump to JSON file
    out_file = tmp_path / "solution.json"
    PuzzleIO.dump_to_json_file(b2, str(out_file))
    # Read back JSON
    out_data = json.loads(out_file.read_text())
    # Should contain the crown and blocked positions
    assert [0, 0] in out_data["crowns"]
    assert [1, 1] in out_data["blocked"]
    # Regions still the same
    assert out_data["regions"] == data["regions"]
