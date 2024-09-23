import random
from player import *

class Holdme:
    """ # only calculates"""
    def __init__(self,
                 playersData:list,
                 ante:int = 100,
                 pot:int = 0,
                 handList:list[list] = [],
                 communityCardsList:list = [],
                 gameRound = 0,
                 small_blind = 1):
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
        self.__playersData:list[dict] = playersData
        self.__playersList:list[Player] = []

    def update_players_info(self):
        """save the player data to json"""
        #get all player Id
        players_dict = {player.name: player for player in iter(self.__playersList)}
        for ori_player in self.__playersData:  #ori = original
            # find and replace player data
            if ori_player['username'] in players_dict:
                ori_player['chip'] = players_dict[ori_player['username']].chip
        return self.__playersData

    def init_player(self,username):
        #playerList is ordered by the player seat
        for player in self.__playersData:
            if player['username'] == username:
                # insert player to the middle seat
                self.__playersList.insert(2,(Player(player['username'],player['chip'])))
                break
            else:
                self.__playersList.append(Bot(player['username'],player['chip']))
        self.__playersList = self.__playersList[:5]

    def get_players_info(self,key:str) -> list:
        '''for draw func\n
        return a list include all player info\n
        find the attr in playerslist by key'''
        return [getattr(player,key) for player in self.__playersList]

    def check_game(self):
        """when someone win the game,change the blind seat"""
        self.small_blind = 0 if self.small_blind >= len(self.__playersList) else self.small_blind
        self.__big_blind = 1 if self.__big_blind >= len(self.__playersList) else self.__big_blind
        if self.__finish:
            self.small_blind = self.small_blind + 1 if self.small_blind < 4 else 0
            self.__big_blind   = self.__big_blind + 1 if self.__big_blind < 4 else 0
            self.__finish = False

    def holdem(self,choiceFunc = None,updateFunc = None):
        '''choiceFunc: for real player operate,\n
        updatFunc: update each player's chip after bet'''
        self.gameRound += 1
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
                self.check_winner()
                self.__finish = True
        self.betting_round(choiceFunc,updateFunc)
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
                # avoid index error(small blind)
                if seat >= len(self.__playersList):
                    seat -= len(self.__playersList)
                # blind bet
                is_ante = self.pot < self.ante + self.ante/2
                if self.gameRound == 1 and is_ante:
                    if seat == self.small_blind:
                        least_bet = round(self.ante/2)
                    elif seat == self.__big_blind:
                        least_bet = self.ante
                # get combination name
                self.__playersList[seat].combination()
                if not self.__playersList[seat].fold:
                    # operation
                    result = self.__playersList[seat].decision(is_ante,least_bet,choiceFunc)
                    self.pot += result['bet']
                    least_bet = 0 if (seat == self.__big_blind and is_ante) else result['bet']
                    # update in interface
                    data = self.get_players_info('name'),self.get_players_info('chip')
                    updateFunc(*data)
                # find the next player
                current = (current + 1) % len(self.__playersList)
                # add one more round if someone raise
                if result['choice'] == BET_RAISE:
                    seat_range = range(current,current + len(self.__playersList) - 1)
                    again += 1
                    break
            again -= 1

    def check_winner(self):
        s = [COMBO_RATING.index(player.combo[0]) for player in self.__playersList]
        for player in s:
            pass



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