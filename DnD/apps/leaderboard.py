import json

from tabulate import tabulate

from database.database import DataBase
from settings.settings import LeaderBoardVars as LBV
from helper.utils import Utils


class Leaderboard:
    """Leaderboard showing games won, games lost and win ratio of each user"""
    def __init__(self) -> None:
        self.database = DataBase()
        self.name: str = LBV.NAME
        self.won: str = LBV.WON
        self.lost: str = LBV.LOST
        self.ratio: str = LBV.RATIO
        self.no_registers: str = LBV.NO_USERS
        self.style: str = LBV.TABLE_STYLE
        self.any_key: str = LBV.PRESS_ANY

    def show_leaderboard(self) -> None:
        """Prints a table in the terminal containing the game's leaderboard"""
        with open(self.database.database_name) as file_object:
            database = json.load(file_object)

        players_stats = list()
        for name, stats in database[self.database.players].items():
            player = dict()
            player.setdefault(self.name, name)
            for stat, value in stats.items():
                if stat == self.database.games_won:
                    player.setdefault(self.won, value)
                if stat == self.database.games_lost:
                    player.setdefault(self.lost, value)
                if stat == self.database.win_ratio:
                    player.setdefault(self.ratio, value)
            players_stats.append(player)

        sorted_players = sorted(
            players_stats, key=lambda player: player[self.ratio]
        )[::-1]
        sorted_players = [
            {
                stat: (
                    f"{value:.2f} %" if stat == self.ratio else value
                ) for stat, value in player.items()
            } for player in sorted_players
        ]

        if not len(sorted_players):
            print(self.no_registers)
        else:
            headers = list(sorted_players[0].keys())
            rows = [player.values() for player in sorted_players]
            print(tabulate(rows, headers, tablefmt=self.style))
        print(self.any_key)
        input()
        Utils.clean()
