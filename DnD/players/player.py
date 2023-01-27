from .base import BasePlayer
from settings.settings import PlayerShootSettings as PSS


class Player(BasePlayer):
    """ """

    shoot_directions = {
        PSS.UP.value: PSS.UP_DIR.value,
        PSS.DOWN.value: PSS.DOWN_DIR.value,
        PSS.RIGHT.value: PSS.RIGHT_DIR.value,
        PSS.LEFT.value: PSS.LEFT_DIR.value,
    }

    def shoot(self, user_input: str) -> list[tuple[int, int]]:
        """

        Parameters
        ----------
        user_input: str : user input


        Returns list[tuple[int, int]]: a list of coordinate of the shots fired
        -------

        """
        shots = list()
        shot_direction = self.shoot_directions[user_input]
        for shot in shot_direction:
            x, y = self.coord
            x_shot, y_shot = shot

            new_x = x + y_shot
            new_y = y + x_shot
            shot_coord = (new_x, new_y)

            shots.append(shot_coord)
        return shots
