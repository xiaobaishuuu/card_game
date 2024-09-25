import random
from player import *

class BaseGame:
    """game framework"""
    def __init__(self,total_player) -> None:
        #playerslist: all player information(username,chip)
        self.__playersList:list[Player] = []
        self.total_player = total_player

    def init_player(self,bot_list:list,real_player:dict = {}):
        random.shuffle(bot_list)
        for bot in bot_list:
            self.__playersList.append(Bot(bot['username'],bot['chip']))
        if real_player:
            self.__playersList.insert(2,(Player(real_player['username'],real_player['chip'])))
        self.__playersList = self.__playersList[:self.total_player]

    @property
    def playersList(self):
        return self.__playersList

    def get_players_info(self,attr:str) -> list:
        '''for draw func\n
        return a list include all player info\n
        find the attr in class Player'''
        return [getattr(player,attr) for player in self.__playersList]