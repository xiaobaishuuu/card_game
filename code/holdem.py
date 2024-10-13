from Base import *

class Holdme(BaseGame):
    """ # only calculates\n
        程序入口為holdem(),調用后運行一回合而不是一整局,因此要運行一整局需配合循環(一局5回合)"""

    def __init__(self,
                 ante:int = 100,
                 pot:int = 0,
                 handList:list[list] = [],
                 communityCardsList:list[str] = [""] * 5,
                 gameRound = 0,
                 small_blind = 2):
        #finish: someone win the game
        super().__init__(total_player=5)
        self.ante= ante
        self.pot = pot
        self.handList = handList
        self.communityCardsList = communityCardsList[:5] + [''] * (5 - len(communityCardsList))
        self.gameRound = gameRound
        self.small_blind = small_blind
        self.__big_blind = self.small_blind + 1
        self.__foldList  = [False] *5
        self.__pokerList = [f'{i}_{j}' for i in range(2,15) for j in range(1,5)]
        self.winnerList = {}

    def check_game(self):
        """check the blind seat or someone win the game,"""
        # ensure blind seat not exceed the range
        self.small_blind = (self.small_blind) % 5
        self.__big_blind = (self.small_blind + 1) % 5

    def holdem(self,choiceFunc,
               updateChipFunc = None,
               updateCardFunc = None,
               updatePotFunc  = None,
               ThinkingFunc   = None):
        '''choiceFunc (necessary): real player operator\n
           (OPTIONAL):\n
           updateChipFunc: update each player's chip\n
           updateCardFunc: update card layer if player fold\n
           updatePotFunc: update pot after player bet\n
           ThinkingFunc: sleep the programe for fake thinking of bot\n'''
        self.betting_round(choiceFunc,updateChipFunc,updateCardFunc,updatePotFunc,ThinkingFunc)
        # only 1 player
        if self.winnerList:
            return
        # new round
        self.gameRound += 1
        match self.gameRound:
            case 1:
                self.deal_player()
            case 2:
                self.deal_community(range(0,3))
            case 3:
                self.deal_community(range(3,4))
            case 4:
                self.deal_community(range(4,5))
            case 5:
                self.check_winner()
                return
        # get combo
        for player in self.playersList:
            player.combination(list(filter(lambda x:x != "",self.communityCardsList)))
            player.total_bet = 0

    def betting_round(self,choiceFunc,
                      updateChipFunc = None,
                      updateCardFunc = None,
                      updatePotFunc  = None,
                      ThinkingFunc   = None):
        current = self.small_blind
        seat_range = range(current,current + len(self.playersList))
        least_bet = 0
        again = 1
        while again > 0:
            for seat in seat_range:

                # find the next player index
                current = (current + 1) % len(self.playersList)

                # avoid index error(small blind)
                if  seat >= len(self.playersList):
                    seat -= len(self.playersList)

                # blind bet
                is_ante = self.pot < self.ante + self.ante/2
                if self.gameRound == 0:
                    if    seat == self.small_blind:  least_bet = round(self.ante/2)
                    elif  seat == self.__big_blind:  least_bet = self.ante
                    else: least_bet = 0

                if not self.playersList[seat].fold:
                    ### bot thinking
                    if ThinkingFunc and seat != 2: ThinkingFunc(seat,random.randint(1,7))

                    # operation
                    result = self.playersList[seat].decision(is_ante,least_bet,self.ante,choiceFunc)
                    self.pot += result['bet']
                    if result['choice'] == kw.FOLD: self.__foldList[seat] = self.playersList[seat].fold

                    ### update in interface
                    if updateChipFunc: updateChipFunc(seat,self.playersList[seat].username,self.playersList[seat].chip)
                    if updatePotFunc : updatePotFunc(self.pot,seat,result['choice'],result['bet'])
                    if updateCardFunc and self.playersList[seat].fold: updateCardFunc(seat,self.playersList[seat].hand,self.playersList[seat].fold)

                    # only one player
                    if self.__foldList.count(False) == 1:
                        self.check_winner()
                        return

                    # add one round if someone raise
                    if result['choice'] == kw.BET_RAISE:
                        least_bet = self.playersList[seat].total_bet
                        seat_range = range(current,current + len(self.playersList) - 1)
                        again += 1
                        break
            again -= 1

    def check_winner(self):
        players_combo = {}
        nonFoldList = [player for player in self.playersList if not player.fold]
        for player in self.playersList:
            if not player.fold:
                players_combo[player.username] = [kw.COMBO_RATING.index(player.combo[0]),player.combo[1]]

        for username,combo in players_combo.items():
            if combo[0] == max(players_combo.values()[0]):
                self.winnerList[username] = combo

        for player in nonFoldList:
            if player.username in self.winnerList.keys():
                player.chip += round(self.pot/len(self.winnerList))

        # nonFoldList = [player for player in self.playersList if not player.fold]
        # # players_combo format - {username:[combo_level,combo_high_card],...} e.g. {'tom':[5,[2,3,4,5,6]]},combo is straight 2 to 6
        # players_combo = {player.username:[kw.COMBO_RATING.index(player.combo[0]),player.combo[1]] for player in nonFoldList}
        # # maybe play a draw so include all winner
        # # for i in self.playersList:
        # #     print(i.username,i.combo)
        # self.winnerList = {player:combo for player,combo in players_combo.items() if combo == max(players_combo.values())}
        # prize = self.pot/round(len(self.winnerList))
        # for i in pla

    def deal_player(self):
        '''deal hand to self.handList'''
        # already set hand
        if len(self.handList) == 5:
            for i in range(len(self.handList)):
                self.playersList[i].hand = self.handList[i]
            return None
        # deal card to Player()
        self.handList = []

        for i in range(len(self.playersList)):
            # get 2 hand
            element = random.sample(self.__pokerList,2)
            self.handList.append(element)
            self.playersList[i].hand = element
            for i in range(2):
                self.__pokerList.remove(element[i])

        # for i in range(len(self.playersList)):
        # # for hand in self.handList:
        #     print(self.handList)
        #     while len(self.handList[i]) <= 2:
        #         element = random.choice(self.__pokerList)
        #         self.__pokerList.remove(element)
        #         self.handList[i].append(element)
        #         self.playersList[i].hand = self.handList[i]

    def deal_community(self,card_range:range):
        # deal community
        for i in card_range:
            if not self.communityCardsList[i]:
                element = random.choice(self.__pokerList)
                self.communityCardsList[i] = element
                self.__pokerList.remove(element)
# print([['',''],*5])
# a = Holdme()
# a.init_player([{
#             "type": 0,
#             "username": "Peter",
#             "password": "832jce83912deddwa",
#             "chip": 492000
#         },
#         {
#             "type": 0,
#             "username": "Amy",
#             "password": "832jce83912deddwa",
#             "chip": 498000
#         },
#         {
#             "type": 0,
#             "username": "Tom",
#             "password": "832jce83912deddwa",
#             "chip": 496000
#         },
#         {
#             "type": 0,
#             "username": "John",
#             "password": "832jce83912deddwa",
#             "chip": 500000
#         }],{
#             "type": 1,
#             "username": "Rex",
#             "password": "123",
#             "chip": 500000
#         })
# a.deal_player()
# print(a.handList)