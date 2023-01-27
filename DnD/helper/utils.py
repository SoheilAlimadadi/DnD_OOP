import os
from time import sleep

from helper.messages import HomepageMessages as HB


class Utils:

    @staticmethod
    def clean() -> None:
        '''Clear terminal'''
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')


    @staticmethod
    def wait_clean() -> None:
        '''Wait 2 seconds then clear terminal'''
        sleep(2)
        Utils.clean()
    

    @staticmethod
    def print_logo() -> None:
        """Prints game's logo"""
        print(
                """
*********************************
*********** Dungeon *************
************** & ****************
*********** Dragons *************
*********************************
                """)
