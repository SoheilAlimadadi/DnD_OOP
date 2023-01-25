from enum import StrEnum, Enum


class HomepageButtons(StrEnum):
    LOGIN_BUTTON: str = 'l'
    REGISTER_BUTTON: str = 'r'
    QUIT_BUTTON: str = 'q'
    LOGIN_BACK: str = 'b'


class MenuButtons(StrEnum):
    EASY_DIFF: str = '1'
    NORMAL_DIFF: str = '2'
    HARD_DIFF: str = '3'
    LEADERBOARD: str = 'l'
    LOGOUT: str = 'q'


class LeaderBoardVars(StrEnum):
    NAME: str = 'Name'
    WON: str = 'Games won'
    LOST: str = 'Games lost'
    RATIO: str = 'Win ratio'
    NO_USERS: str = "No registered users yet"
    TABLE_STYLE: str = 'grid'
    PRESS_ANY: str = '\n\nEnter any key to go back.'

class ValidGameInputs(StrEnum):
    UP: str = 'up'
    DOWN: str = 'down'
    RIGHT: str = 'right'
    LEFT: str = 'left'
    BACK: str = 'q'


class GameBoardElements(StrEnum):
    MAP_WALLS: str = '⬛'
    MAP_TILES: str = '⬜'


class GameBoardSize(Enum):
    MAP_WIDTH: int = 15
    MAP_HEIGHT: int = 15


class GameMechanicElemenets(StrEnum):
    X: str = 'x'
    Y: str = 'y'


class MonsterSettings(StrEnum):
    MONSTER_STR: str = 'monster'
    MONSTER: str = '🐉'
    DRAGON_NUM: str = '3'


class PlayerSettings(StrEnum):
    PLAYER_STR: str = 'player'
    PLAYER: str = '😎'
    HEALTH: str = '💜'
    HEALTH_NUM: str = '3'


class DungeonDoorSettings(StrEnum):
    DOOR_STR: str = 'dungeon door'
    EMOJI: str = '🟥'
    

class MovementSettings(Enum):
    UP_INPUT: str = 'up'
    DOWN_INPUT: str = 'down'
    LEFT_INPUT: str = 'left'
    RIGHT_INPUT: str = 'right'
    UP: tuple[int, int] = (0, -1)
    DOWN: tuple[int, int] = (0, 1)
    RIGHT: tuple[int, int] = (1, 0)
    LEFT: tuple[int, int] = (-1, 0)


class GameState(StrEnum):
    ON_GOING: str = 'on going'
    WIN: str = 'won'
    LOSE: str = 'lost'