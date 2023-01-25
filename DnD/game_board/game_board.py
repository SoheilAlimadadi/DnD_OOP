from settings.settings import GameBoardElements as GBE
from settings.settings import GameBoardSize as GBS


class GameBoard:
    """
    Class for the gameboard of the game
    """

    def __init__(self) -> None:
        self.row_len: str = GBS.MAP_WIDTH.value
        self.col_len: str = GBS.MAP_HEIGHT.value
        self.walls: str = GBE.MAP_WALLS
        self.tiles: str = GBE.MAP_TILES


    def make_board(self) -> list[list[str]]:
        """Creates the gameboard"""
        game_map = [self.walls * self.row_len 
                    if col == 0 or col == (self.col_len - 1)
                    else [self.walls if row == 0 or row == (self.row_len - 1)
                    else self.tiles for row in range(self.row_len)]
                    for col in range(self.col_len)]

        
        for col in range(2, self.col_len - 2, 3):
            if col % 2 == 0:
                for row in range(2, self.row_len - 1):
                    game_map[col][row] = self.walls

            else:
                for row in range(1, self.row_len - 2):
                    game_map[col][row] = self.walls

        return game_map


    @staticmethod
    def place_on_board(
        board: list[list[str]],
        coord: tuple[int, int],
        obj: str
    ) -> tuple[int, int]:
        """Draws objects onto the gameboard"""
        xpos, ypos = coord
        board[xpos][ypos] = obj

        return coord


    @staticmethod
    def delete(board, coord: tuple[int, int]) -> None:
        """Deletes objects from the gameboard"""
        xpos, ypos = coord
        board[xpos][ypos] = GBE.MAP_TILES


    @staticmethod
    def draw_game_board(board: list[list[str]]) -> None:
        """Draws the gameboard"""
        for row in board:
            print(''.join(row))
