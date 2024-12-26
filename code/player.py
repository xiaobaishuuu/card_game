import keywords as kw
import random
from evalutor import Card,Evaluator,evaluator

class Player():

    def __init__(self,
                 username:str,
                 chip:int,
                 hand:list = [],
                 fold = False) -> None:
        self.username = username
        self.chip = chip
        self.hand = hand
        self.fold = fold
        self.allin= False   # ***temp
        self.combo= ['',''] # combo int, combo name
        self.total_bet = 0
        if self.chip < 10000: self.chip = 10000 # ***temp

    def decision(self,is_ante:bool,least_bet:int,least_raise:int,choiceFunc) -> dict:
        ''' return a dict{choice,bet}'''
        # calculate player's least bet,(not least bet for a round)
        least_bet -= self.total_bet
        #used in gui
        if is_ante:                       # blind seat or allin
            invalidList = [kw.INCREASE,kw.DECREASE,kw.BET_RAISE,kw.FOLD,kw.CHECK]
        elif not self.hand:               # first round
            invalidList = [kw.INCREASE,kw.DECREASE,kw.BET_RAISE,kw.FOLD,kw.CALL]
        # ======================================================================== ***temp
        elif self.chip <= least_bet + least_raise:  # allin
            invalidList = [kw.INCREASE,kw.DECREASE,kw.BET_RAISE,kw.CHECK]
            self.allin = True
        # ========================================================================
        elif least_bet > 0:               # someone bet
            invalidList = [kw.CHECK]
        elif least_bet == 0 and self.hand:# first seat or allin
            invalidList = [kw.CALL]
        # receive data
        result:dict = choiceFunc(self.chip,least_bet,least_raise,self.fold,invalidList)
        # handle data
        choice = result['choice']
        # ========================================================================= ***temp
        if result['choice'] == kw.CALL and self.allin or (self.chip <= least_bet + least_raise and is_ante):
            self.allin = True
            bet = self.chip
            choice = kw.ALL_IN
        #==========================================================================
        elif result['choice'] == kw.CALL or is_ante: bet = least_bet
        elif result['choice'] == kw.BET_RAISE:       bet = result['bet']
        elif result['choice'] == kw.CHECK:           bet = 0
        elif result['choice'] == kw.FOLD:            bet,self.fold = 0,True

        # upload data
        self.total_bet += bet
        self.chip -= bet
        return {'choice':choice,'bet':bet}

    def combination(self,community:list):
        community = list(filter(lambda x: x,community))
        rank_int = evaluator.evaluate([Card.new(card) for card in self.hand],[Card.new(card) for card in community])
        combo = evaluator.get_rank_string(rank_int)
        self.combo = [rank_int,combo]

class Bot(Player):
    def __init__(self,
                 username,
                 chip,
                 hand=[],
                 fold = False) -> None:
        super().__init__(username,chip,hand,fold)

    def decision(self,is_ante:bool,least_bet:int,least_raise:int,choiceFunc):
        # filter invalid ones
        weights = [100]
        if is_ante:          # ante
            validList = [kw.CALL]
        elif not self.hand:  # first round
            validList = [kw.CHECK]
        # ======================================================================== ***temp
        elif self.chip <= least_bet + least_raise:  # allin
            validList = [kw.FOLD,kw.CALL]
            weights = [80,20]
            self.allin = True
        # ========================================================================
        elif least_bet == 0: # nobody bet
            validList = [kw.FOLD,kw.CHECK,kw.BET_RAISE]
            weights = [5,60,45]
        elif least_bet > 0:  # someone bet
            validList = [kw.FOLD,kw.CALL,kw.BET_RAISE]
            weights = [15,60,25]
        # calculate player's least bet,(not least bet for a round)
        least_bet = least_bet - self.total_bet
        # make decision
        choice = random.choices(validList,weights=weights,k=1)[0]
        # ========================================================================= ***temp
        if choice == kw.CALL and self.allin or (self.chip <= least_bet + least_raise and is_ante):
            self.allin = True
            bet = self.chip
            choice = kw.ALL_IN
        #==========================================================================
        elif choice == kw.CALL or is_ante: bet = least_bet
        elif choice == kw.BET_RAISE:       bet = least_bet + least_raise
        elif choice == kw.CHECK:           bet = 0
        elif choice == kw.FOLD:            bet,self.fold = 0,True

        self.chip -= bet
        self.total_bet += bet
        return {'choice':choice,'bet':bet}