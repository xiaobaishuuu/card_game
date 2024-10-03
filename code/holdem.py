from Base import *

class Holdme(BaseGame):
    """ # only calculates\n
        程序入口為holdem(),調用后運行一回合而不是一整局,因此要運行一整局需配合循環(一局5回合)"""

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
        self.winnerList = []

    def check_game(self):
        """check the blind seat or someone win the game,"""
        # ensure blind seat not exceed the range
        self.small_blind = (self.small_blind) % 5
        self.__big_blind = (self.small_blind + 1) % 5

    def holdem(self,choiceFunc,updateChipFunc = None,updateCardFunc = None):
        self.betting_round(choiceFunc,updateChipFunc,updateCardFunc)
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
                return
        # get combo
        for player in self.playersList:
            player.combination()
            player.last_bet = 0
        print('============================================')

    def betting_round(self,choiceFunc,updateChipFunc = None,updateCardFunc = None):
        '''choiceFunc: real player operator,\n
           updateChipFunc: update each player's chip\n
           updateCardFunc: update card layer if player fold\n
           ONLY choiceFunc is necessary'''
        current = self.small_blind
        seat_range = range(current,current + len(self.playersList))
        least_bet = 0
        again = 1
        while again > 0:
            print('----------------------------------------------')
            for seat in seat_range:

                # find the next player index
                current = (current + 1) % len(self.playersList)

                # avoid index error(small blind)
                if  seat >= len(self.playersList):
                    seat -= len(self.playersList)

                # blind bet
                is_ante = self.pot < self.ante + self.ante/2
                if self.gameRound == 0 and is_ante:
                    if   seat == self.small_blind:  least_bet = round(self.ante/2)
                    elif seat == self.__big_blind:  least_bet = self.ante

                if not self.playersList[seat].fold:
                    # operation
                    result = self.playersList[seat].decision(is_ante,least_bet,choiceFunc)

                    print(self.playersList[seat].username,result)

                    self.pot += result['bet']
                    if (seat == self.__big_blind and is_ante):  least_bet = 0
                    elif not self.playersList[seat].fold:       least_bet = result['bet']

                    # update in interface
                    if updateChipFunc and updateCardFunc:
                        updateChipFunc(seat,self.playersList[seat].username,self.playersList[seat].chip)
                    if self.gameRound > 0:
                        updateCardFunc(seat,self.playersList[seat].hand    ,self.playersList[seat].fold)
                    # add one round if someone raise
                    if result['choice'] == kw.BET_RAISE:
                        seat_range = range(current,current + len(self.playersList) - 1)
                        print('again',self.playersList[seat].username)
                        again += 1
                        break
            again -= 1

    def check_winner(self):
        # players_combo format - {username:[combo_level,combo_high_card],...} e.g. {'tom':[5,[2,3,4,5,6]]},combo is straight 2 to 6
        players_combo = {player.username:[kw.COMBO_RATING.index(player.combo[0]),player.combo[1]] for player in self.playersList}
        # maybe play a draw so include all winner
        for i in self.playersList:
            print(i.username,i.combo)
        self.winnerList = {player:combo for player,combo in players_combo.items() if combo == max(players_combo.values())}

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