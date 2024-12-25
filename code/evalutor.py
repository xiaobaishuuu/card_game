import itertools

class Card:
    """算法來自 https://suffe.cool/poker/evaluator.html """
    # the basics
    STR_RANKS: str = ('2','3','4','5','6','7','8','9','10','11','12','13','14')
    INT_RANKS: range = range(13)
    PRIMES: list[int] = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]

    # conversion from string => int
    CHAR_RANK_TO_INT_RANK: dict[str, int] = dict(zip(list(STR_RANKS), INT_RANKS))
    CHAR_SUIT_TO_INT_SUIT: dict[str, int] = {
        '1': 1,  # spades
        '2': 2,  # hearts
        '3': 4,  # diamonds
        '4': 8,  # clubs
    }
    INT_SUIT_TO_CHAR_SUIT: str = 'x12x3xxx4'  #按八位運算

    @staticmethod
    def new(string: str) -> int:
        rank_int = Card.CHAR_RANK_TO_INT_RANK[string.split('_')[0]]
        suit_int = Card.CHAR_SUIT_TO_INT_SUIT[string.split('_')[1]]
        rank_prime = Card.PRIMES[rank_int]

        bitrank = 1 << rank_int << 16
        suit = suit_int << 12
        rank = rank_int << 8

        return bitrank | suit | rank | rank_prime

    @staticmethod
    def int_to_str(card_int: int) -> str:
        rank_int = Card.get_rank_int(card_int)
        suit_int = Card.get_suit_int(card_int)
        return f'{Card.STR_RANKS[rank_int]}_{Card.INT_SUIT_TO_CHAR_SUIT[suit_int]}'

    @staticmethod
    def get_rank_int(card_int: int) -> int:
        return (card_int >> 8) & 0xF

    @staticmethod
    def get_suit_int(card_int: int) -> int:
        return (card_int >> 12) & 0xF

    @staticmethod
    def get_bitrank_int(card_int: int) -> int:
        return (card_int >> 16) & 0x1FFF

    @staticmethod
    def get_prime(card_int: int) -> int:
        return card_int & 0x3F

    @staticmethod
    def hand_to_binary(card_strs: list[str]) -> list[int]:
        """
        Expects a list of cards as strings and returns a list
        of integers of same length corresponding to those strings.
        """
        bhand = []
        for c in card_strs:
            bhand.append(Card.new(c))
        return bhand

    @staticmethod
    def prime_product_from_hand(card_ints: list[int]) -> int:
        product = 1
        for c in card_ints:
            product *= (c & 0xFF)
        return product

    @staticmethod
    def prime_product_from_rankbits(rankbits: int) -> int:
        product = 1
        for i in Card.INT_RANKS:
            # if the ith bit is set
            if rankbits & (1 << i):
                product *= Card.PRIMES[i]

        return product


class LookupTable:
    """
    Number of Distinct Hand Values:

    Straight Flush   10
    Four of a Kind   156      [(13 choose 2) * (2 choose 1)]
    Full Houses      156      [(13 choose 2) * (2 choose 1)]
    Flush            1277     [(13 choose 5) - 10 straight flushes]
    Straight         10
    Three of a Kind  858      [(13 choose 3) * (3 choose 1)]
    Two Pair         858      [(13 choose 3) * (3 choose 2)]
    One Pair         2860     [(13 choose 4) * (4 choose 1)]
    High Card      + 1277     [(13 choose 5) - 10 straights]
    -------------------------
    TOTAL            7462

    Here we create a lookup table which maps:
        5 card hand's unique prime product => rank in range [1, 7462]

    Examples:
    * Royal flush (best hand possible)          => 1
    * 7-5-4-3-2 unsuited (worst hand possible)  => 7462
    """
    MAX_ROYAL_FLUSH: int     = 1
    MAX_STRAIGHT_FLUSH: int  = 10
    MAX_FOUR_OF_A_KIND: int  = 166
    MAX_FULL_HOUSE: int      = 322
    MAX_FLUSH: int           = 1599
    MAX_STRAIGHT: int        = 1609
    MAX_THREE_OF_A_KIND: int = 2467
    MAX_TWO_PAIR: int        = 3325
    MAX_PAIR: int            = 6185
    MAX_HIGH_CARD: int       = 7462

    MAX_TO_RANK_CLASS: dict[int, int] = {
        MAX_ROYAL_FLUSH: 0,
        MAX_STRAIGHT_FLUSH: 1,
        MAX_FOUR_OF_A_KIND: 2,
        MAX_FULL_HOUSE: 3,
        MAX_FLUSH: 4,
        MAX_STRAIGHT: 5,
        MAX_THREE_OF_A_KIND: 6,
        MAX_TWO_PAIR: 7,
        MAX_PAIR: 8,
        MAX_HIGH_CARD: 9
    }

    RANK_CLASS_TO_STRING: dict[int, str] = {
        0: "Royal Flush",
        1: "Straight Flush",
        2: "Four of a Kind",
        3: "Full House",
        4: "Flush",
        5: "Straight",
        6: "Three of a Kind",
        7: "Two Pair",
        8: "One Pair",
        9: "High Card"
    }

    def __init__(self) -> None:
        """
        Calculates lookup tables
        """
        # create dictionaries
        self.flush_lookup: dict[int, int] = {}
        self.unsuited_lookup: dict[int, int] = {}

        # create the lookup table in piecewise fashion
        # this will call straights and high cards method,
        # we reuse some of the bit sequences
        self.flushes()
        self.multiples()

    def flushes(self) -> None:
        """
        Straight flushes and flushes.

        Lookup is done on 13 bit integer (2^13 > 7462):
        xxxbbbbb bbbbbbbb => integer hand index
        """
        # straight flushes in rank order
        straight_flushes = [
            7936,  # int('0b1111100000000', 2), # royal flush
            3968,  # int('0b111110000000', 2),
            1984,  # int('0b11111000000', 2),
            992,   # int('0b1111100000', 2),
            496,   # int('0b111110000', 2),
            248,   # int('0b11111000', 2),
            124,   # int('0b1111100', 2),
            62,    # int('0b111110', 2),
            31,    # int('0b11111', 2),
            4111   # int('0b1000000001111', 2) # 5 high
        ]

        # now we'll dynamically generate all the other
        # flushes (including straight flushes)
        flushes = []
        gen = self.get_lexographically_next_bit_sequence(int('0b11111', 2))

        # 1277 = number of high cards
        # 1277 + len(str_flushes) is number of hands with all cards unique rank
        for i in range(1277 + len(straight_flushes) - 1):   # we also iterate over SFs
            # pull the next flush pattern from our generator
            f = next(gen)

            # if this flush matches perfectly any
            # straight flush, do not add it
            notSF = True
            for sf in straight_flushes:
                # if f XOR sf == 0, then bit pattern
                # is same, and we should not add
                if not f ^ sf:
                    notSF = False

            if notSF:
                flushes.append(f)

        # we started from the lowest straight pattern, now we want to start ranking from
        # the most powerful hands, so we reverse
        flushes.reverse()

        # now add to the lookup map:
        # start with straight flushes and the rank of 1
        # since it is the best hand in poker
        # rank 1 = Royal Flush!
        rank = 1
        for sf in straight_flushes:
            prime_product = Card.prime_product_from_rankbits(sf)
            self.flush_lookup[prime_product] = rank
            rank += 1

        # we start the counting for flushes on max full house, which
        # is the worst rank that a full house can have (2,2,2,3,3)
        rank = LookupTable.MAX_FULL_HOUSE + 1
        for f in flushes:
            prime_product = Card.prime_product_from_rankbits(f)
            self.flush_lookup[prime_product] = rank
            rank += 1

        # we can reuse these bit sequences for straights
        # and high cards since they are inherently related
        # and differ only by context
        self.straight_and_highcards(straight_flushes, flushes)

    def straight_and_highcards(self, straights: list[int], highcards: list[int]) -> None:
        """
        Unique five card sets. Straights and highcards.

        Reuses bit sequences from flush calculations.
        """
        rank = LookupTable.MAX_FLUSH + 1

        for s in straights:
            prime_product = Card.prime_product_from_rankbits(s)
            self.unsuited_lookup[prime_product] = rank
            rank += 1

        rank = LookupTable.MAX_PAIR + 1
        for h in highcards:
            prime_product = Card.prime_product_from_rankbits(h)
            self.unsuited_lookup[prime_product] = rank
            rank += 1

    def multiples(self) -> None:
        """
        Pair, Two Pair, Three of a Kind, Full House, and four of a Kind.
        """
        backwards_ranks = list(range(len(Card.INT_RANKS) - 1, -1, -1))

        # 1) Four of a Kind
        rank = LookupTable.MAX_STRAIGHT_FLUSH + 1

        # for each choice of a set of four rank
        for i in backwards_ranks:

            # and for each possible kicker rank
            kickers = backwards_ranks[:]
            kickers.remove(i)
            for k in kickers:
                product = Card.PRIMES[i]**4 * Card.PRIMES[k]
                self.unsuited_lookup[product] = rank
                rank += 1

        # 2) Full House
        rank = LookupTable.MAX_FOUR_OF_A_KIND + 1

        # for each three of a kind
        for i in backwards_ranks:

            # and for each choice of pair rank
            pairranks = backwards_ranks[:]
            pairranks.remove(i)
            for pr in pairranks:
                product = Card.PRIMES[i]**3 * Card.PRIMES[pr]**2
                self.unsuited_lookup[product] = rank
                rank += 1

        # 3) Three of a Kind
        rank = LookupTable.MAX_STRAIGHT + 1

        # pick three of one rank
        for r in backwards_ranks:

            kickers = backwards_ranks[:]
            kickers.remove(r)
            gen = itertools.combinations(kickers, 2)

            for kickers_2combo in gen:

                c1, c2 = kickers_2combo
                product = Card.PRIMES[r]**3 * Card.PRIMES[c1] * Card.PRIMES[c2]
                self.unsuited_lookup[product] = rank
                rank += 1

        # 4) Two Pair
        rank = LookupTable.MAX_THREE_OF_A_KIND + 1

        tpgen = itertools.combinations(tuple(backwards_ranks), 2)
        for tp in tpgen:

            pair1, pair2 = tp
            kickers = backwards_ranks[:]
            kickers.remove(pair1)
            kickers.remove(pair2)
            for kicker in kickers:

                product = Card.PRIMES[pair1]**2 * Card.PRIMES[pair2]**2 * Card.PRIMES[kicker]
                self.unsuited_lookup[product] = rank
                rank += 1

        # 5) Pair
        rank = LookupTable.MAX_TWO_PAIR + 1

        # choose a pair
        for pairrank in backwards_ranks:

            kickers = backwards_ranks[:]
            kickers.remove(pairrank)
            kgen = itertools.combinations(tuple(kickers), 3)

            for kickers_3combo in kgen:

                k1, k2, k3 = kickers_3combo
                product = Card.PRIMES[pairrank]**2 * Card.PRIMES[k1] \
                    * Card.PRIMES[k2] * Card.PRIMES[k3]
                self.unsuited_lookup[product] = rank
                rank += 1

    def get_lexographically_next_bit_sequence(self, bits: int):
        """
        Bit hack from here:
        http://www-graphics.stanford.edu/~seander/bithacks.html#NextBitPermutation

        Generator even does this in poker order rank
        so no need to sort when done! Perfect.
        """
        t = int((bits | (bits - 1))) + 1
        next = t | ((int(((t & -t) / (bits & -bits))) >> 1) - 1)
        yield next
        while True:
            t = (next | (next - 1)) + 1
            next = t | ((((t & -t) // (next & -next)) >> 1) - 1)
            yield next

class Evaluator:

    HAND_LENGTH = 2
    BOARD_LENGTH = 5

    def __init__(self) -> None:

        self.table = LookupTable()
        self.hand_size_map = {
            2: self._two,
            5: self._five,
            6: self._six,
            7: self._seven
        }

    def evaluate(self, hand: list[int], board: list[int]) -> int:
        """
        This is the function that the user calls to get a hand rank.

        No input validation because that's cycles!
        """
        all_cards = hand + board
        return self.hand_size_map[len(all_cards)](all_cards)

    def _two(self, cards: list[int]) -> int:
        """新添加"""
        if (Card.get_prime(cards[0])) == (Card.get_prime(cards[1])):
            return LookupTable.MAX_PAIR - (Card.get_prime(cards[0]))*(Card.get_prime(cards[1]))
        else:
            return LookupTable.MAX_HIGH_CARD - max(cards[0] & 0xff,cards[1] & 0xff)

    def _five(self, cards: list[int]) -> int:
        """
        Performs an evalution given cards in integer form, mapping them to
        a rank in the range [1, 7462], with lower ranks being more powerful.

        Variant of Cactus Kev's 5 card evaluator, though I saved a lot of memory
        space using a hash table and condensing some of the calculations.
        """
        # if flush
        if cards[0] & cards[1] & cards[2] & cards[3] & cards[4] & 0xF000:
            handOR = (cards[0] | cards[1] | cards[2] | cards[3] | cards[4]) >> 16
            prime = Card.prime_product_from_rankbits(handOR)
            return self.table.flush_lookup[prime]

        # otherwise
        else:
            prime = Card.prime_product_from_hand(cards)
            return self.table.unsuited_lookup[prime]

    def _six(self, cards: list[int]) -> int:
        """
        Performs five_card_eval() on all (6 choose 5) = 6 subsets
        of 5 cards in the set of 6 to determine the best ranking,
        and returns this ranking.
        """
        minimum = LookupTable.MAX_HIGH_CARD

        for combo in itertools.combinations(cards, 5):

            score = self._five(combo)
            if score < minimum:
                minimum = score

        return minimum

    def _seven(self, cards: list[int]) -> int:
        """
        Performs five_card_eval() on all (7 choose 5) = 21 subsets
        of 5 cards in the set of 7 to determine the best ranking,
        and returns this ranking.
        """
        minimum = LookupTable.MAX_HIGH_CARD

        for combo in itertools.combinations(cards, 5):
            score = self._five(combo)
            if score < minimum:
                minimum = score

        return minimum

    def get_rank_string(self, hr: int) -> int:
        """
        Returns the class name of hand
        returned from evaluate.
        """
        if hr >= 0 and hr <= LookupTable.MAX_ROYAL_FLUSH:
            class_int = LookupTable.MAX_TO_RANK_CLASS[LookupTable.MAX_ROYAL_FLUSH]
        elif hr <= LookupTable.MAX_STRAIGHT_FLUSH:
            class_int =  LookupTable.MAX_TO_RANK_CLASS[LookupTable.MAX_STRAIGHT_FLUSH]
        elif hr <= LookupTable.MAX_FOUR_OF_A_KIND:
            class_int =  LookupTable.MAX_TO_RANK_CLASS[LookupTable.MAX_FOUR_OF_A_KIND]
        elif hr <= LookupTable.MAX_FULL_HOUSE:
            class_int =  LookupTable.MAX_TO_RANK_CLASS[LookupTable.MAX_FULL_HOUSE]
        elif hr <= LookupTable.MAX_FLUSH:
            class_int =  LookupTable.MAX_TO_RANK_CLASS[LookupTable.MAX_FLUSH]
        elif hr <= LookupTable.MAX_STRAIGHT:
            class_int =  LookupTable.MAX_TO_RANK_CLASS[LookupTable.MAX_STRAIGHT]
        elif hr <= LookupTable.MAX_THREE_OF_A_KIND:
            class_int =  LookupTable.MAX_TO_RANK_CLASS[LookupTable.MAX_THREE_OF_A_KIND]
        elif hr <= LookupTable.MAX_TWO_PAIR:
            class_int =  LookupTable.MAX_TO_RANK_CLASS[LookupTable.MAX_TWO_PAIR]
        elif hr <= LookupTable.MAX_PAIR:
            class_int =  LookupTable.MAX_TO_RANK_CLASS[LookupTable.MAX_PAIR]
        elif hr <= LookupTable.MAX_HIGH_CARD:
            class_int =  LookupTable.MAX_TO_RANK_CLASS[LookupTable.MAX_HIGH_CARD]
        else:
            raise Exception("Inavlid hand rank, cannot return rank class")
        return LookupTable.RANK_CLASS_TO_STRING[class_int]