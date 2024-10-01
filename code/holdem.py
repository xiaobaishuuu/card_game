from Base import *

class Holdme(BaseGame):
    """ # only calculates"""

    def __init__(self,
                 ante:int = 100,
                 pot:int = 0,
                 handList:list[list] = [],
                 communityCardsList:list = [],
                 gameRound = 0,
                 small_blind = 0):
        #finish: someone win the game
        super().__init__(total_player=5)
        self.ante= ante
        self.pot = pot
        self.handList = handList
        self.communityCardsList = communityCardsList
        self.gameRound = gameRound
        self.small_blind = small_blind
        self.__big_blind = self.small_blind + 1
        self.__pokerList = [f'{i}_{j}' for i in range(2,15) for j in range(1,5)]
        self.__finish = False

    def check_game(self):
        """check the blind seat or someone win the game,"""
        # ensure blind seat not exceed the range
        self.small_blind = (self.small_blind) % 5
        self.__big_blind = (self.small_blind + 1) % 5
        if self.__finish:
            self.small_blind = (self.small_blind + 1) % 5
            self.__big_blind = (self.small_blind + 1) % 5
            self.__finish = False

    def holdem(self,choiceFunc = None,updateFunc = None):
        '''choiceFunc: real player operator,\n
        updateFunc: update each player's chip'''
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
        seat_range = range(current,current + len(self.playersList))
        least_bet = 0
        again = 1
        while again > 0:
            for seat in seat_range:
                # avoid index error(small blind)
                if seat >= len(self.playersList):
                    seat -= len(self.playersList)
                # blind bet
                is_ante = self.pot < self.ante + self.ante/2
                if self.gameRound == 1 and is_ante:
                    if seat == self.small_blind:
                        least_bet = round(self.ante/2)
                    elif seat == self.__big_blind:
                        least_bet = self.ante
                # get combo
                self.playersList[seat].combination()
                if not self.playersList[seat].fold:
                    # operation
                    result = self.playersList[seat].decision(is_ante,least_bet,choiceFunc)
                    self.pot += result['bet']
                    least_bet = 0 if (seat == self.__big_blind and is_ante) else result['bet']
                    # update in interface
                    data = self.get_players_info('username'),self.get_players_info('chip')
                    updateFunc(*data)
                # find the next player
                current = (current + 1) % len(self.playersList)
                # add one round if someone raise
                if result['choice'] == kw.BET_RAISE:
                    seat_range = range(current,current + len(self.playersList) - 1)
                    again += 1
                    break
            again -= 1

    def check_winner(self):
        # players_combo format - {username:[combo_level,combo_high_card],...} e.g. {'tom':[5,[2,3,4,5,6]]},combo is straight 2 to 6
        players_combo = {player.username:[kw.COMBO_RATING.index(player.combo[0]),player.combo[1]] for player in self.playersList}
        # maybe play a draw so include all winner
        winner_list = [player for player,combo in players_combo.items() if combo == max(players_combo.values())]
        return winner_list

    def deal_player(self):
        '''deal hand to self.handList'''
        # already set hand
        if len(self.handList) == 5:
            for i in range(len(self.handList)):
                self.playersList[i].hand = self.handList[i]
            return None
        # deal card to Player()
        for i in range(len(self.playersList)):
            # get 2 hand
            element = random.sample(self.__pokerList,2)
            self.handList.append(element)
            self.playersList[i].hand = element
            for i in range(2):
                self.__pokerList.remove(element[i])

    def deal_community(self,get:int):
        """get == how many card will deal"""
        # already set community
        if len(self.communityCardsList) == 5:
            Player.community = self.communityCardsList
            return None
        # deal card to Player()
        for i in range(get):
            element = random.choice(self.__pokerList)
            Player.community.append(element)
            self.communityCardsList.append(element)
            self.__pokerList.remove(element)