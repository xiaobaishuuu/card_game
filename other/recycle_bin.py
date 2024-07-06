# HAND_POSITION = []
# for i in range(len(PLAYER_INFO_BAR_POSITION)):
#     HAND_POSITION.append([(PLAYER_INFO_BAR_POSITION[i][0]+((200 - (POKER_WIDTH*POKER_RATIO*2 - 30))/2),PLAYER_INFO_BAR_POSITION[i][1]-130),
#                           (PLAYER_INFO_BAR_POSITION[i][0]+200-((200 - (POKER_WIDTH*POKER_RATIO*2 - 30))/2)-(POKER_WIDTH*POKER_RATIO),PLAYER_INFO_BAR_POSITION[i][1]-130)
#                           ])

# # HAND Center position: (200 - (POKER_WIDTH*POKER_RATIO*2 - 30))/2   ,   200-((200 - (POKER_WIDTH*POKER_RATIO*2 - 30))/2)-(POKER_WIDTH*POKER_RATIO)
# #[[(hand 1 pos,hand 2 pos)],[(hand 1 pos,hand 2 pos)],...]
# #[[(52.5, 0), (110.0, 0)], [(52.5, 480), (110.0, 480)], [(567.5, 480), (625.0, 480)], [(1082.5, 480), (1140.0, 480)], [(1082.5, 0), (1140.0, 0)]]
# HAND_POSITION = [[(PLAYER_INFO_BAR_POSITION[i][0]+((200 - (POKER_WIDTH*POKER_RATIO*2 - 30))/2),PLAYER_INFO_BAR_POSITION[i][1]-130),
#                   (PLAYER_INFO_BAR_POSITION[i][0]+200-((200 - (POKER_WIDTH*POKER_RATIO*2 - 30))/2)-(POKER_WIDTH*POKER_RATIO),PLAYER_INFO_BAR_POSITION[i][1]-130)]
#                   for i in range(len(PLAYER_INFO_BAR_POSITION))]

# # [(406.25, 121.815), (501.25, 121.815), (596.25, 121.815), (691.25, 121.815), (786.25, 121.815)]
# COMMUNITY_CARDS_POSITION = [(POKER_TABLE_START_POSITION[0] + ((POKER_WIDTH*POKER_TABLE_RATIO - POKER_WIDTH*POKER_RATIO) + GAP + (POKER_WIDTH*POKER_RATIO))* i,
#                              POKER_TABLE_START_POSITION[1]) for i in range(5)]

#start : SCREEN_WIDTH/2 - (POKER_WIDTH*POKER_RATIO/2) + (-(POKER_WIDTH*POKER_TABLE_RATIO - POKER_WIDTH*POKER_RATIO) -GAP -(POKER_WIDTH*POKER_RATIO))*2 , 120+(POKER_HEIGHT*POKER_TABLE_RATIO - POKER_HEIGHT*POKER_RATIO)/2
# HAND Center position: (200 - (POKER_WIDTH*POKER_RATIO*2 - 30))/2   ,   200-((200 - (POKER_WIDTH*POKER_RATIO*2 - 30))/2)-(POKER_WIDTH*POKER_RATIO)

# BUTTON_RECT = [pygame.Rect(PLAYER_INFO_BAR_POSITION[2][0]- (BUTTON_GAP + BUTTON_WIDTH)*2,__betButton_y,BUTTON_WIDTH,BUTTON_HEIGHT),
#                pygame.Rect(PLAYER_INFO_BAR_POSITION[2][0]- (BUTTON_GAP + BUTTON_WIDTH)*3,__betButton_y,BUTTON_WIDTH,BUTTON_HEIGHT),
#                pygame.Rect(PLAYER_INFO_BAR_POSITION[2][0]- (BUTTON_GAP + BUTTON_WIDTH)  ,__betButton_y,BUTTON_WIDTH,BUTTON_HEIGHT),
#                pygame.Rect(PLAYER_INFO_BAR_POSITION[2][0]+ PLAYER_INFO_BAR_WIDTH + BUTTON_GAP + BUTTON_WIDTH ,__betButton_y,BUTTON_WIDTH,BUTTON_HEIGHT),
#                pygame.Rect(PLAYER_INFO_BAR_POSITION[2][0]+ PLAYER_INFO_BAR_WIDTH + BUTTON_WIDTH ,__betButton_y,BUTTON_WIDTH,BUTTON_HEIGHT),
#                pygame.Rect(PLAYER_INFO_BAR_POSITION[2][0]+ PLAYER_INFO_BAR_WIDTH + BUTTON_WIDTH + BUTTON_GAP + BUTTON_WIDTH,__betButton_y,BUTTON_WIDTH,BUTTON_HEIGHT)]

# buttonList = [Button(CHECK   ,BUTTON_RECT[0]),
#               Button(FOLD    ,BUTTON_RECT[1]),
#               Button(BET_CALL,BUTTON_RECT[2]),
#               Button(RAISE   ,BUTTON_RECT[3]),
#               Button(UP      ,BUTTON_RECT[4],BUTTON_GAP),
#               Button(DOWN    ,BUTTON_RECT[5],BUTTON_GAP)]

# # player operation
# def wager(self,wager,money = 0,ante = 10):
#     totalBet = 0
#     if   wager == ANTE:
#         for player in playerData:
#             player['chip'] -= ante
#             totalBet += ante
#     elif wager == CALL:
#         #bot oper
#         pass
#     elif wager == CHECK:
#         pass
#     elif wager == BET_RAISE:
#         pass
#     elif wager == FOLD:
#         pass

    # return totalBet


# if self.gameRound == 1:
#     if seat == self.__small_blind:
#         least_bet = self.ante
#     elif seat == self.__big_blind:
#         least_bet = self.ante/2
#     else:
#         least_bet = 0

# least_bet = self.ante if self.gameRound == 1 and seat == self.__small_blind else self.ante/2 if self.gameRound == 1 and seat == self.__big_blind else 0

# def check_button(playerChip:int,gameRound = 0,least_bet = 0,press = False):
#     '''press == True will pass,return button name'''
#     choice = ''
#     Button.init_raise(least_bet)
#     while not press:
#         clock.tick(FPS)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 exit()
#             # only check
#             for button in buttonList:
#                 #check all betting button
#                 # if (least_bet > 0 and button.text == CHECK):
#                 #     continue
#                 if button.check(event):
#                     choice = button.text
#                     #either betting button press
#                     if button.flag == 0:
#                         press = True
#                 # first round cant fold
#                 if gameRound == 1:
#                     break
#         # only draw
#         for button in buttonList:
#             button.draw(screen,playerChip,gameRound)
#             # first round cant fold
#             if gameRound == 1:
#                 break
#     return {'choice':choice,'bet':button.get_raise() if choice == BET_RAISE else least_bet}

    # round 1 deal hand
    # if game.get_attr('gameRound') >= 1:
    #     draw_hand(game)
    # # round 2 deal commu 3
    # if game.get_attr('gameRound') >= 2:
    #     draw_community(game,range(3),2)
    # # round 3 deal commu 1
    # if game.get_attr('gameRound') >= 3:
    #     draw_community(game,range(3,4),3)
    # # round 4 deal commu 1
    # if game.get_attr('gameRound') >= 4:
    #     draw_community(game,range(4,5),4)

    # match game.get_attr('gameRound'):
    #     # r == game round
    #     case r if r >= 4:
    #         draw_community(game.get_attr('communityCardsList'),r,range(4,5),4)
    #     case r if r >= 3:
    #         draw_community(game.get_attr('communityCardsList'),r,range(3,4),3)
    #     case r if r >= 2:
    #         draw_community(game.get_attr('communityCardsList'),r,range(3),2)
    #     case r if r >= 1:
    #         draw_hand(game.get_attr('handList'),r)

            # least_bet = 0
            # again = 1
            # while again > 0:
            #     again -= 1
            #     for seat in range(self.__small_blind,self.__small_blind + len(self.__playersList)):
            #         if seat >= len(self.__playersList):
            #             seat -= 5
            #         # blind bet
            #         if self.__gameRound == 1 and again == 0:
            #             if seat == self.__small_blind:
            #                 least_bet = self.ante
            #             elif seat == self.__big_blind:
            #                 least_bet = self.ante/2
            #         # operate
            #         result = self.__playersList[seat].decision(choiceFunc,self.__gameRound,least_bet)
            #         # least bet = 0 after big blind
            #         least_bet = 0 if (self.__gameRound == 1 and seat == self.__big_blind) else result['bet']
            #         self.pot += result['bet']
            #         updateFunc(self.get_player_info('name'),self.get_player_info('chip'))

            #         if result['choice'] == BET_RAISE:
            #             again += 1

            # def betting_round(self,choiceFunc = None,updateFunc = None):
            #     '''choiceFunc: for real player operate,\n
            #     updatFunc: draw or print each player's chip after bet'''
            #     current = self.__small_blind
            #     start = current
            #     end = start + len(self.__playersList)

            #     seat_range = range(current,start + len(self.__playersList))
            #     least_bet = 0
            #     again = 1
            #     while again > 0:
            #         for seat in seat_range:
            #         # for seat in range(start,end):
            #             # make sure range in playersList
            #             if seat >= len(self.__playersList):
            #                 seat -= len(self.__playersList)
            #             # blind bet
            #             if self.__gameRound == 1 and (self.pot < self.ante + self.ante/2):
            #                 if seat == self.__small_blind:
            #                     least_bet = self.ante
            #                 elif seat == self.__big_blind:
            #                     least_bet = self.ante/2
            #             is_ante = self.pot < self.ante + self.ante/2
            #             # operate
            #             result = self.__playersList[seat].decision(is_ante,least_bet,self.__gameRound,choiceFunc)
            #             self.pot += result['bet']
            #             least_bet = 0 if seat == self.__big_blind and is_ante else result['bet']
            #             # find the next player and update in screen or text
            #             current = (current + 1) % len(self.__playersList)
            #             updateFunc(self.get_player_info('name'),self.get_player_info('chip'))
            #             # print(f"{self.__playersList[seat].name}:{result['choice']},{result['bet']}",least_bet)
            #             if result['choice'] == BET_RAISE:
            #                 start = current
            #                 end = current + len(self.__playersList) - 1
            #                 again += 1
            #                 break
            #         again -= 1

# {
#     "player_data": [
#         {
#             "Id": 1,
#             "userName": "Peter",
#             "chip": 1000
#         },
#         {
#             "Id": 2,
#             "userName": "Amy",
#             "chip": 1000
#         },
#         {
#             "Id": 3,
#             "userName": "Tom",
#             "chip": 1000
#         },
#         {
#             "Id": 4,
#             "userName": "John",
#             "chip": 1000
#         },
#         {
#             "Id": 1001,
#             "userName": "Rex",
#             "chip": 1000
#         },
#         {
#             "Id": 1002,
#             "userName": "Felix",
#             "chip": 1000
#         }
#     ]
# }

    # def get_private_attr(self,variable):
    #     return getattr(self,f'_{self.__class__.__name__}__{variable}')

# def two_pair(self,card_list):
#     if len(set(card_list['rank'])) != len(card_list['rank']) - 2:
#         return False,None
#     pair_list = {}
#     for rank in card_list['rank']:
#         if rank in pair_list:
#             pair_list[rank] += 1
#         else:
#             pair_list[rank] = 1
#     return True,sorted(list(pair_list.keys()))[-2]


# def one_pair(card_list) -> tuple[bool,tuple]:
#     if len(set(card_list['rank'])) == len(card_list['rank']) - 1:
#         for rank in set(card_list['rank']):
#             if card_list['rank'].count(rank) == 2:
#                 return True,(rank,)
#     return False,(None,)

# def two_pair(card_list):
#     if len(card_list['rank']) - len(set(card_list['rank'])) >= 2:
#         pair_list = []
#         for rank in set(card_list['rank']):
#             if card_list['rank'].count(rank) == 2:
#                 pair_list.append(rank)
#         return True,sorted(pair_list,reverse=True)[:2]
#     return False,(None,)


a = {'rank':[1,0,0,1,8,3]}
# print(one_pair(a))

# 5 3 2
# 6 4 2
# 6 3 3
# 7 5 2
# 7 4 3

# 2 1
# 5 4
# 6 5
# 7 6

5 3
6 4
6 2
7 5
7 3
def is_straight_flush(card_list):
    return len(set(card['suit'] for card in card_list)) == 1 and sorted(['--23456789TJQKA'.index(card['rank']) for card in card_list]) == list(range(min(['--23456789TJQKA'.index(card['rank']) for card in card_list]), min(['--23456789TJQKA'.index(card['rank']) for card in card_list]) + 5))

def is_four_of_a_kind(card_list):
    return any(sum(card['rank'] == c['rank'] for c in card_list) == 4 for card in card_list)

def is_full_house(card_list):
    return len(set(card['rank'] for card in card_list)) == 2 and sorted([sum(card['rank'] == c['rank'] for c in card_list) for card in set(tuple(c.items()) for c in card_list)]) == [2, 3]

def is_flush(card_list):
    return len(set(card['suit'] for card in card_list)) == 1

def is_straight(card_list):
    return sorted(['--23456789TJQKA'.index(card['rank']) for card in card_list]) == list(range(min(['--23456789TJQKA'.index(card['rank']) for card in card_list]), min(['--23456789TJQKA'.index(card['rank']) for card in card_list]) + 5))

def is_three_of_a_kind(card_list):
    return any(sum(card['rank'] == c['rank'] for c in card_list) == 3 for card in card_list)

def is_two_pair(card_list):
    return sorted([sum(card['rank'] == c['rank'] for c in card_list) for card in set(tuple(c.items()) for c in card_list)]).count(2) == 2

def is_one_pair(card_list):
    return sorted([sum(card['rank'] == c['rank'] for c in card_list) for card in set(tuple(c.items()) for c in card_list)]).count(2) == 1

a = {'rank':[1,0,0,1,8,3]}
print(is_one_pair(a))