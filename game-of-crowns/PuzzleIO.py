import json

from RegionID import RegionID
from CellState import CellState
from Cell import Cell
from Region import Region
from Board import Board

class PuzzleIO:

    @staticmethod
    def board_from_dict(d: dict) -> Board:
        rows, cols = d["height"], d["width"]
        cells = {
            (r,c): Cell(r, c, RegionID(color), CellState.EMPTY)
            for color, coords in d["regions"].items()
            for (r,c) in coords
        }
        grid = tuple(tuple(cells[r,c] for c in range(cols)) for r in range(rows))
        regions = tuple(
            Region(RegionID(color), tuple(cells[r,c] for (r,c) in coords))
            for color, coords in d["regions"].items()
        )
        return Board(rows, cols, grid, regions)

    @staticmethod
    def dump_to_dict(b: Board) -> dict:
        return {
            "height": b.rows,
            "width":  b.cols,
            "regions": {
                reg.id.value: [[c.row,c.col] for c in reg.cells]
                for reg in b.regions
            },
            "crowns":  [[c.row,c.col] for row in b.grid for c in row if c.state is CellState.CROWN],
            "blocked": [[c.row,c.col] for row in b.grid for c in row if c.state is CellState.BLOCKED]
        }

    @staticmethod
    def load_from_json_file(path: str) -> Board:
        return PuzzleIO.load_from_dict(json.load(open(path)))

    @staticmethod
    def dump_to_json_file(b: Board, path: str) -> None:
        json.dump(PuzzleIO.dump_to_dict(b), open(path,"w"), indent=2)