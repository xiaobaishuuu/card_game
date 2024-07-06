from keywords import *
import random

class Player():

    community = []
    def __init__(self,
                 Id,
                 name:str,
                 chip:int,
                 hand:list = [],
                 fold = False) -> None:
        self.Id = Id
        self.name = name
        self.chip = chip
        self.hand = hand
        self.fold = fold
        self.combination_name = ''

    def decision(self,is_ante:bool,least_bet:int,choiceFunc) -> dict[str,int]:
        ''' return a dict["choice","bet"]'''
        if self.fold:       # fold
            invalidList = [INCREASE,DECREASE,FOLD,CALL,CHECK,BET_RAISE]
        elif is_ante:       # blind seat
            invalidList = [INCREASE,DECREASE,FOLD,CALL,CHECK]
        elif not self.hand: #first round
            invalidList = [FOLD,CALL]
        elif least_bet > 0: # someone bet
            invalidList = [CHECK]
        elif least_bet == 0 and self.hand: #first seat
            invalidList = [CALL]
        self.c = self.combination()
        # receive ui interect result
        result:dict[str,int] = choiceFunc(self.chip,least_bet,self.fold,invalidList)
        if result['choice'] == FOLD:
            self.fold = True
        self.chip -= result['bet']
        return result

    def combination(self):
        rank = sorted([int(i.split('_')[0]) for i in (self.hand + self.community)])
        suit = [i.split('_')[1] for i in (self.hand + self.community)]
        # priority permutation
        check_dict = {
            # 'straight flush':self.straight_flush,
            # 'four of a kind':self.four_of_a_kind,
            # 'full house':self.full_house,
            # 'flush':self.flush,
            'straight':self.straight,
            'three of a kind':self.three_of_a_kind,
            'two pair':self.two_pair,
            'one pair':self.one_pair
        }
        for name,check_func in check_dict.items():
            result = check_func({'rank':rank,'suit':suit})
            if result:
                print(name)
                return result

    def one_pair(self,card_list):
        power = []
        if len(set(card_list['rank'])) == len(card_list['rank']) - 1:
            for rank in set(card_list['rank']):
                if card_list['rank'].count(rank) == 2:
                    power.append(rank)
                    break
        return power

    def two_pair(self,card_list):
        power = []
        if len(card_list['rank']) - len(set(card_list['rank'])) >= 2:
            power = sorted([rank for rank in set(card_list['rank']) if card_list['rank'].count(rank) == 2])[-2:]
        return power

    def three_of_a_kind(self,card_list):
        power = sorted([rank for rank in set(card_list['rank']) if card_list['rank'].count(rank) == 3])
        return power if not power else power[-1]

    def straight(self,card_list):
        power = []
        ranks = list(set(card_list['rank']))[::-1]
        for i in range(len(ranks) - 1):
            power.append(ranks[i]) if ranks[i] - ranks[i+1] == 1 else power.clear()
            if len(power) >= 4:
                power = max(power)
                break
        return power.clear() if power

    def flush(self,card_list):
        for i in set(card_list['suit']):
            if card_list['suit'].count(i) >= 5:
                return True
        return False

    def full_house(self,card_list):
        for i in set(card_list['rank']):
            pass

    def four_of_a_kind(self,card_list):
        pass

    def straight_flush(self,card_list):
        pass

class Bot(Player):
    def __init__(self,Id,name,chip,hand=[],fold = False) -> None:
        super().__init__(Id,name,chip,hand,fold)
        choiceList = [BET_RAISE,CHECK,FOLD,CALL]

    def monte_carlo(self,n = 100,opponents = 4):
        win_chip_list = []
        p = 0
        def decision():
            pass
        for i in range(n):
            hand_list = []
            for i in range(opponents):
                hand_list.append([])
        # return p,(sum(win_chip  _list)/len(win_chip_list))

    def linear_regression(self):
        self.monte_carlo()
        pass

    def decision(self,is_ante,least_bet,choiceFunc):
        self.combination()
        if self.fold:
            return
        if is_ante:
            choice = ANTE
            bet = least_bet
        else:
            # choice = BET_RAISE
            # bet = least_bet + 100
            choice = CALL
            bet = least_bet
        self.chip -= bet
        return {'choice':choice,'bet':bet}

Player.community = ['2_1','3_1','4_1','5_1']
a = Player(12,'aaa',100,[])

print(a.combination())