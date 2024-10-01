import keywords as kw

class Player():

    community = []
    def __init__(self,
                 username:str,
                 chip:int,
                 hand:list = [],
                 fold = False) -> None:
        self.username = username
        self.chip = chip
        self.hand = hand
        self.fold = fold
        self.combo= ['','']

    def decision(self,is_ante:bool,least_bet:int,choiceFunc) -> dict:
        ''' return a dict{choice,bet}'''
        if self.fold:       # fold
            invalidList = [kw.INCREASE,kw.DECREASE,kw.FOLD,kw.CALL,kw.CHECK,kw.BET_RAISE]
        elif is_ante:       # blind seat
            invalidList = [kw.INCREASE,kw.DECREASE,kw.FOLD,kw.CALL,kw.CHECK]
        elif not self.hand: #first round
            invalidList = [kw.FOLD,kw.CALL]
        elif least_bet > 0: # someone bet
            invalidList = [kw.CHECK]
        elif least_bet == 0 and self.hand: #first seat
            invalidList = [kw.CALL]
        # receive ui interect result
        result:dict = choiceFunc(self.chip,least_bet,self.fold,invalidList)
        if result['choice'] == kw.FOLD:
            self.fold = True
            result['bet'] = 0
        self.chip -= result.get('bet',0)
        return result

    def combination(self):
        if self.hand:
            rank = [int(i.split('_')[0]) for i in (self.hand + self.community)]
            suit = [i.split('_')[1] for i in (self.hand + self.community)]
            # priority permutation
            check_dict = {
                'straight flush':self.straight_flush,
                'four of a kind':self.four_of_a_kind,
                'full house':self.full_house,
                'flush':self.flush,
                'straight':self.straight,
                'three of a kind':self.three_of_a_kind,
                'two pair':self.two_pair,
                'one pair':self.one_pair,
                'high card':self.high_card
            }
            for combo,check_func in check_dict.items():
                result = check_func({'rank':rank,'suit':suit})
                if result:
                    self.combo = [combo,result]
                    break

    def high_card(self,card_list):
        return sorted([int(i.split('_')[0]) for i in (self.hand)])

    def one_pair(self,card_list):
        power = []
        for rank in set(card_list['rank']):
            if card_list['rank'].count(rank) == 2:
                power.append(rank)
        return [max(power)] if power else power

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
        ranks = list(set(card_list['rank']))
        length= 5                        # detect 5 consecutive number, length = 5
        if {2,3,4,5,14}.issubset(ranks): # special combination A,2,3,4,5
            power.append([1,2,3,4,5])
        for i in range(len(ranks) - length + 1):
            tempList = ranks[i:i + length]
            if all((tempList[j] + 1 == tempList[j + 1]) for j in range(length - 1)):
                power.append(tempList)
        return max(power) if power else power

    def flush(self,card_list):
        count = {}
        card_list = list(zip(card_list['rank'],card_list['suit']))
        for card in card_list:
            count[card[1]] = count[card[1]] + 1 if card[1] in count else 1
        count = [suit for suit,c in count.items() if c >= 5]
        power = [card[0] for card in card_list if card[1] in count]
        if 14 in power: # special situation
            power.append(1)
        return power

    def full_house(self,card_list):
        three_of_a_kind = self.three_of_a_kind(card_list)
        one_pair = self.one_pair(card_list)
        if three_of_a_kind and one_pair and three_of_a_kind != one_pair:
            return [three_of_a_kind,one_pair]
        return False

    def four_of_a_kind(self,card_list):
        power = sorted([rank for rank in set(card_list['rank']) if card_list['rank'].count(rank) == 4])
        return power

    def straight_flush(self,card_list):
        straight = self.straight(card_list)
        flush = self.flush(card_list)
        if straight and flush and set(straight).issubset(flush):
            return max(straight)
        return False

class Bot(Player):
    def __init__(self,
                 username,
                 chip,
                 hand=[],
                 fold = False) -> None:
        super().__init__(username,chip,hand,fold)
        choiceList = [kw.BET_RAISE,kw.CHECK,kw.FOLD,kw.CALL]

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
        if self.fold:
            choice = kw.FOLD
            bet = 0
        elif is_ante:
            choice = kw.ANTE
            bet = least_bet
        else:
            # choice = BET_RAISE
            # bet = least_bet + 100
            choice = kw.CALL
            bet = least_bet
        self.chip -= bet
        return {'choice':choice,'bet':bet}