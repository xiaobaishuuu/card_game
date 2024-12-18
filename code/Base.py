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
        '''for child class, cheat mode'''
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

    def game_loop(self):...

if __name__ == '__main__':
    pass