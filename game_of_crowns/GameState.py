from enum import Enum, auto

class GameState(Enum):
    NOT_STARTED = auto()
    PLAYING = auto()
    SOLVED = auto()
    ABANDONED = auto()
    