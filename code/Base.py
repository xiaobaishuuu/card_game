import random
from player import *

class BaseGame:
    """game framework"""
    def __init__(self,total_player:int) -> None:
        #playerslist: all player information(username,chip)
        self.__playersList:list[Player] = []
        self.total_player:int = total_player

    @property
    def playersList(self):
        '''for child class'''
        return self.__playersList

    def save_game(self) -> list[dict]:
        '''return latest player info'''
        return [{kw.USERNAME:player.username,kw.CHIP:player.chip} for player in self.__playersList]

    def get_players_info(self,attr:str) -> list:
        '''for draw func\n
        return a list include all player info\n
        find the attr in class Player'''
        return [getattr(player,attr) for player in self.__playersList]

    def init_player(self,bot_list:list,real_player:dict = {}):
        random.shuffle(bot_list)
        for bot in bot_list:
            self.__playersList.append(Bot(bot[kw.USERNAME],bot[kw.CHIP]))
        if real_player:
            self.__playersList.insert(2,(Player(real_player[kw.USERNAME],real_player[kw.CHIP])))
        self.__playersList = self.__playersList[:self.total_player]
        # if len(self.__playersList) < self.total_player:
        #     raise 'init error'

    def game_loop(self):
        ''''''
        pass

if __name__ == '__main__':
    a = BaseGame(5)
    a.init_player([{
                "type": 0,
                "username": "Peter",
                "password": "832jce83912deddwa",
                "chip": 900
            },
            {
                "type": 0,
                "username": "Amy",
                "password": "832jce83912deddwa",
                "chip": 800
            },
            {
                "type": 0,
                "username": "Tom",
                "password": "832jce83912deddwa",
                "chip": 1000
            },
            {
                "type": 0,
                "username": "John",
                "password": "832jce83912deddwa",
                "chip": 1000
            },
            {
                "type": 0,
                "username": "Alex",
                "password": "832jce83912deddwa",
                "chip": 1000
            },
            {
                "type": 0,
                "username": "Ryan",
                "password": "832jce83912deddwa",
                "chip": 1000
            }])
    a.playersList[0].chip = 1000000000000e10
    print(a.save_game())
    print(a.get_players_info(kw.USERNAME))