from game_of_crowns.Board import Board
from game_of_crowns.GameState import GameState
from game_of_crowns.CellState import CellState
from game_of_crowns.PuzzleIO import PuzzleIO

class GameController:
    def __init__(self, current_board: Board) -> None:
        self.current_board = current_board
        self.history = []
        self.game_state = GameState.NOT_STARTED

    def place_state(self, row: int, col: int, new_state: CellState) -> bool:
        if self.game_state is not GameState.PLAYING:
            return False
        new_board = self.current_board.with_cell_state(row, col, new_state)
        self.history.append(self.current_board)
        self.current_board = new_board
        if new_board.is_solved:
            self.game_state = GameState.SOLVED
            return True
        
    def undo(self) -> bool:
        if self.game_state is not GameState.PLAYING or len(self.history) == 0:
            return False
        self.current_board  = self.history.pop()
        return True

    def reset(self) -> None:
        self.current_board = self.history[0]
        self.history.clear()
        self.game_state = GameState.PLAYING
    
    def load_puzzle(self, data: dict) -> None:
        board = PuzzleIO.load_from_dict(data)
        self.current_board = board
        self.history.clear()
        self.game_state = GameState.PLAYING

    

    
    



        