import json
import random
from player import *

class Holdme:
    """ # only calculates"""
    def __init__(self,
                 playersDataPath:str,
                 ante:int = 100,
                 pot:int = 0,
                 handList:list[list] = [],
                 communityCardsList:list = [],
                 gameRound = 0,
                 small_blind = 0):
        #finish: someone win the game
        #playersData: original data,only read
        #playerslist: players information, can change , length of it == player number
        self.ante= ante
        self.pot = pot
        self.handList = handList
        self.communityCardsList = communityCardsList
        self.gameRound = gameRound
        self.small_blind = small_blind
        self.__big_blind = self.small_blind + 1
        self.__pokerList = [f'{i}_{j}' for i in range(2,15) for j in range(1,5)]
        self.__finish = False
        self.__playersDataPath = playersDataPath
        self.__playersData:list[dict] = self.__load_players(self.__playersDataPath)
        self.__playersList:list[Player] = []

    def __load_players(self,path) -> list:
        '''return a list include player data [{Id:1,name:...},{...}...]'''
        with open(path,mode='r',encoding='utf-8') as fp:
            return json.load(fp)['player_data']

    def save_players(self):
        """save the player data to json"""
        #get all player Id
        players_dict = {player.Id: player for player in iter(self.__playersList)}
        for ori_player in self.__playersData:  #ori = original
            # find and replace player data
            if ori_player['Id'] in players_dict:
                ori_player['chip'] = players_dict[ori_player['Id']].chip
        with open(self.__playersDataPath,mode='w',encoding='utf-8') as fp:
            json.dump({'player_data':self.__playersData},fp,indent=4)

    def init_player(self,Id = 1001):
        # self.check_game()
        #playerList is ordered by the player seat
        for player in self.__playersData:
            if player['Id'] == Id:
                # insert player to the middle seat
                self.__playersList.insert(2,(Player(Id,player['name'],player['chip'])))
                break
            else:
                self.__playersList.append(Bot(player['Id'],player['name'],player['chip']))

    def get_player_info(self,key:str) -> list:
        '''for draw func\n
        return a list include all player info\n
        find the attr in playerslist by key'''
        return [getattr(player,key) for player in self.__playersList]

    def check_game(self):
        """when someone win the game,change the blind seat"""
        self.small_blind = 0 if self.small_blind >= len(self.__playersList) else self.small_blind
        self.__big_blind   = 1 if self.__big_blind >= len(self.__playersList) else self.__big_blind
        if self.__finish:
            self.small_blind = self.small_blind + 1 if self.small_blind < 4 else 0
            self.__big_blind   = self.__big_blind + 1 if self.__big_blind < 4 else 0
            self.__finish = False

    def holdem(self,choiceFunc = None,updateFunc = None):
        '''choiceFunc: for real player operate,\n
        updatFunc: update each player's chip after bet'''
        self.gameRound += 1
        self.betting_round(choiceFunc,updateFunc)
        match self.gameRound:
            case 1:
                self.deal_player()
            case 2:
                self.deal_community(3)
            case 3:
                self.deal_community(1)
            case 4:
                self.deal_community(1)
            case 5:
                pass
        print('=========')

    def betting_round(self,choiceFunc = None,updateFunc = None):
        '''choiceFunc: for real player operate,\n
        updateFunc: draw or print each player's chip after bet'''
        current = self.small_blind
        seat_range = range(current,current + len(self.__playersList))
        least_bet = 0
        again = 1
        while again > 0:
            for seat in seat_range:
                if seat >= len(self.__playersList):
                    seat -= len(self.__playersList)
                # blind bet
                is_ante = self.pot < self.ante + self.ante/2
                if self.gameRound == 1 and is_ante:
                    if seat == self.small_blind:
                        least_bet = self.ante/2
                    elif seat == self.__big_blind:
                        least_bet = self.ante
                # operate
                self.__playersList[seat].combination()
                result = self.__playersList[seat].decision(is_ante,least_bet,choiceFunc)
                self.pot += result['bet']
                least_bet = 0 if (seat == self.__big_blind and is_ante) else result['bet']
                # find the next player and update in interface
                current = (current + 1) % len(self.__playersList)
                data = self.get_player_info('name'),self.get_player_info('chip'),self.get_player_info('combination_name')
                print(data)
                updateFunc(*data)
                # add one more round if someone raise
                if result['choice'] == BET_RAISE:
                    seat_range = range(current,current + len(self.__playersList) - 1)
                    again += 1
                    break
            again -= 1

    def check_winner(self):
        for player in self.__playersList:
            player.combination()

    def deal_player(self):
        '''deal hand to self.handList'''
        # index 2 == player,else bot
        if len(self.handList) == 5:
            for i in range(len(self.handList)):
                self.__playersList[i].hand = self.handList[i]
            return None
        for i in range(len(self.__playersList)):
            # get 2 hand
            element = random.sample(self.__pokerList,2)
            self.handList.append(element)
            self.__playersList[i].hand = element
            for i in range(2):
                self.__pokerList.remove(element[i])

    def deal_community(self,get:int):
        """get == how many card will deal"""
        if len(self.communityCardsList) == 5:
            Player.community = self.communityCardsList
            return None
        for i in range(get):
            element = random.choice(self.__pokerList)
            Player.community.append(element)
            self.communityCardsList.append(element)
            self.__pokerList.remove(element)