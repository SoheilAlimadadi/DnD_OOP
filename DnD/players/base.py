from game_mechanics.movement import Movement
from settings.settings import (
    PlayerSettings as PS,
    GameBoardSize as GBS,
    PlayerShootSettings as PSS
)

class BasePlayer(Movement):
    """The base class for player"""
    def __init__(self, game_board: list[list[str]]) -> None:
        self.emoji: str = PS.PLAYER
        self.string: str = PS.PLAYER_STR
        self.health: list[str] = [PS.HEALTH for _ in range(int(PS.HEALTH_NUM))]
        self.shots: list[str] = [
            PS.SHOTS for _ in range(PSS.SHOTS_NUM.value)
        ]
        self.game_board = game_board
        self.X = GBS.MAP_WIDTH.value // 2
        self.Y = GBS.MAP_HEIGHT.value - 2
        self.coord: tuple[int, int] = (self.Y, self.X)


    def __str__(self) -> str:
        return self.string
