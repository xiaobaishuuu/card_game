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

        # if playerId == 2 and fold == True:
        #     fold_layer = pygame.Surface((POKER_WIDTH*POKER_RATIO,POKER_HEIGHT*POKER_RATIO),pygame.SRCALPHA)
        #     pygame.draw.rect(fold_layer,(0,0,0,128),fold_layer.get_rect(),0,2)
        #     screen.blit(fold_layer,position)
        # draw_hand(game.handList,r,game.get_players_info('fold')[2])
# 5 3 2
# 6 4 2
# 6 3 3
# 7 5 2
# 7 4 3
        # pygame.draw.rect(screen,POKER_PLACE_COLOR,(405+(GAP+POKER_WIDTH*POKER_TABLE_RATIO)*i,120,POKER_WIDTH*POKER_TABLE_RATIO,POKER_HEIGHT*POKER_TABLE_RATIO),3,5)
# TABLE_RECT.y + 90 +(POKER_HEIGHT*POKER_TABLE_RATIO - POKER_HEIGHT*POKER_RATIO)/2
# 2 1
# 5 4
# 6 5
# 7 6

        #get all player Id
        # players_dict = {player.name: player for player in iter(self.playersList)}
        # for ori_player in ori_players_info:  #original
        #     # find and update player data
        #     if ori_player['username'] in players_dict:
        #         ori_player['chip'] = players_dict[ori_player['username']].chip
        # return ori_players_info
# a = b`

# 0 1
# 1 2
# 2 3
# 3 4
# 4 0
# 0 1
# small_blind = 21831937192371923
# __big_blind = small_blind +1

# small_blind = (small_blind) % 5
# __big_blind = (small_blind + 1) % 5
# print(small_blind,__big_blind)
# small_blind = (small_blind + 1) % 5
# __big_blind = (small_blind + 1) % 5
# print(small_blind,__big_blind)

# from Base import *

# class Holdme(BaseGame):
#     """ # only calculates\n
#     def __init__(self,
#                  ante:int = 100,
#                  pot:int = 0,
#                  handList:list[list] = [],
#                  communityCardsList:list = [],
#                  gameRound = 0,
#                  small_blind = random.randint(1,5)):
#         #finish: someone win the game
#         super().__init__(total_player=5)
#         self.ante= ante
#         self.pot = pot
#         self.handList = handList
#         self.communityCardsList = communityCardsList
#         self.gameRound = gameRound
#         self.small_blind = small_blind
#         self.__big_blind = self.small_blind + 1
#         self.__pokerList = [f'{i}_{j}' for i in range(2,15) for j in range(1,5)]
#         self.winnerList = []

#     def check_game(self):
#         """check the blind seat or someone win the game,"""
#         # ensure blind seat not exceed the range
#         self.small_blind = (self.small_blind) % 5
#         self.__big_blind = (self.small_blind + 1) % 5

#     def holdem(self,choiceFunc = None,updateFunc = None):
#         '''choiceFunc: real player operator,\n
#         updateFunc: update each player's chip'''
#         self.gameRound += 1
#         match self.gameRound:
#             case 1:
#                 print(self.handList)
#                 self.deal_player()
#             case 2:
#                 self.deal_community(3)
#             case 3:
#                 self.deal_community(1)
#             case 4:
#                 self.deal_community(1)
#             case 5:
#                 print(1)
#                 self.check_winner()
#                 return
#         print('=========================================')
#         self.betting_round(choiceFunc,updateFunc)
#         print('==========================================')

#     def betting_round(self,choiceFunc = None,updateFunc = None):
#         '''choiceFunc: for real player operate,\n
#         updateFunc: draw or print each player's chip after bet'''
#         current = self.small_blind
#         seat_range = range(current,current + len(self.playersList))
#         least_bet = 0
#         again = 1
#         while again > 0:
#             # print('-------------------------------------------------')
#             for seat in seat_range:

#                 # avoid index error(small blind)
#                 if  seat >= len(self.playersList):
#                     seat -= len(self.playersList)

#                 # blind bet
#                 is_ante = self.pot < self.ante + self.ante/2
#                 if self.gameRound == 1 and is_ante:
#                     if   seat == self.small_blind:  least_bet = round(self.ante/2)
#                     elif seat == self.__big_blind:  least_bet = self.ante

#                 # get combo
#                 self.playersList[seat].combination()

#                 if not self.playersList[seat].fold:

#                     # operation
#                     result = self.playersList[seat].decision(is_ante,least_bet,choiceFunc)
#                     # print(self.playersList[seat].username,result)
#                     self.pot += result['bet']
#                     if (seat == self.__big_blind and is_ante): least_bet = 0
#                     elif not self.playersList[seat].fold:      least_bet = result['bet']

#                     # update in interface
#                     data = self.get_players_info('username'),self.get_players_info('chip')
#                     updateFunc(*data)

#                 # find the next player
#                 current = (current + 1) % len(self.playersList)

#                 if self.get_players_info('fold').count(True) == 4:
#                     self.gameRound = 5

#                 # add one round if someone raise
#                 if result.get('choice') == kw.BET_RAISE:
#                     seat_range = range(current,current + len(self.playersList) - 1)
#                     again += 1
#                     break


#             again -= 1

#     def check_winner(self):
#         # players_combo format - {username:[combo_level,combo_high_card],...} e.g. {'tom':[5,[2,3,4,5,6]]},combo is straight 2 to 6
#         players_combo = {player.username:[kw.COMBO_RATING.index(player.combo[0]),player.combo[1]] for player in self.playersList}
#         for k in players_combo.keys():
#             for i in self.playersList:
#                 if i.fold:
#                     del players_combo[k]
#         # maybe play a draw so include all winner
#         # for i in self.playersList:
#         #     print(i.username,i.combo)
#         self.winnerList = {player:combo for player,combo in players_combo.items() if combo == max(players_combo.values())}

#     def deal_player(self):
#         '''deal hand to self.handList'''
#         # already set hand
#         if len(self.handList) == 5:
#             for i in range(len(self.handList)):
#                 self.playersList[i].hand = self.handList[i]
#             return None
#         # deal card to Player()
#         for i in range(len(self.playersList)):
#             # get 2 hand
#             element = random.sample(self.__pokerList,2)
#             self.handList.append(element)
#             self.playersList[i].hand = element
#             for i in range(2):
#                 self.__pokerList.remove(element[i])

#     def deal_community(self,get:int):
#         """get == how many card will deal"""
#         # already set community
#         if len(self.communityCardsList) == 5:
#             Player.community = self.communityCardsList
#             return None
#         # deal card to Player()
#         for i in range(get):
#             element = random.choice(self.__pokerList)
#             Player.community.append(element)
#             self.communityCardsList.append(element)
#             self.__pokerList.remove(element)

# if least_bet + raise_bet > playerChip:
#     raise_bet = playerChip - least_bet
# # exceed min
# elif least_bet + raise_bet < least_bet:
#     raise_bet = 0
# return least_bet + raise_bet
# raise_bet = min(raise_bet, playerChip - least_bet) # not excced max
# return least_bet + max(0, raise_bet)               # not exceed min

# def draw_progress_bar(surface, color, rect, radius, progress):
#     # 绘制空心圆角矩形
#     pygame.draw.rect(surface, color, (*rect, *rect_size), border_radius=radius, width=2)

#     # 绘制进度条
#     if progress > 0:
#         total_length = 2 * (rect_size[0] + rect_size[1] - 4 * radius)  # 计算总长度
#         progress_length = (progress / 100) * total_length  # 计算进度长度

#         # 顶边
#         if progress_length <= rect_size[0]:
#             pygame.draw.rect(surface, progress_color, (rect[0] + radius, rect[1], progress_length, 2))
#         else:
#             pygame.draw.rect(surface, progress_color, (rect[0] + radius, rect[1], rect_size[0] - 2 * radius, 2))
#             progress_length -= (rect_size[0] - 2 * radius)

#             # 右边
#             if progress_length <= rect_size[1]:
#                 pygame.draw.rect(surface, progress_color, (rect[0] + rect_size[0] - 2, rect[1] + radius, 2, progress_length))
#             else:
#                 pygame.draw.rect(surface, progress_color, (rect[0] + rect_size[0] - 2, rect[1] + radius, 2, rect_size[1] - 2 * radius))
#                 progress_length -= (rect_size[1] - 2 * radius)

#                 # 底边
#                 if progress_length <= rect_size[0]:
#                     pygame.draw.rect(surface, progress_color, (rect[0] + radius, rect[1] + rect_size[1] - 2, progress_length, 2))
#                 else:
#                     pygame.draw.rect(surface, progress_color, (rect[0] + radius, rect[1] + rect_size[1] - 2, rect_size[0] - 2 * radius, 2))
#                     progress_length -= (rect_size[0] - 2 * radius)

#                     # 左边
#                     pygame.draw.rect(surface, progress_color, (rect[0], rect[1] + radius, 2, progress_length))

# if progress >= total_length:
#     pygame.draw.arc(surface, progress_color, (rect[0], rect[1], rect_size[0], rect_size[1]),
#                     0, math.radians(90), 2)  # 右上
#     pygame.draw.arc(surface, progress_color, (rect[0] + rect_size[0] - 2 * radius, rect[1],
#                                                 rect_size[0], rect_size[1]),
#                     math.radians(90), math.radians(180), 2)  # 左上
#     pygame.draw.arc(surface, progress_color, (rect[0] + rect_size[0] - 2 * radius, rect[1] + rect_size[1] - 2 * radius,
#                                                 rect_size[0], rect_size[1]),
#                     math.radians(180), math.radians(270), 2)  # 左下
#     pygame.draw.arc(surface, progress_color, (rect[0], rect[1] + rect_size[1] - 2 * radius,
#                                                 rect_size[0], rect_size[1]),
#                     math.radians(270), math.radians(360), 2)  # 右下

# PLAYER_INFO_BAR_POSITION= [(TABLE_RECT.x + TABLE_WIDTH - 85,TABLE_RECT.y + 100),
#                            (TABLE_RECT.x + TABLE_WIDTH - 85,TABLE_RECT.y + TABLE_HEIGHT),
#                            (SCREEN_WIDTH/2 - PLAYER_INFO_BAR_WIDTH/2,TABLE_RECT.y + TABLE_HEIGHT),
#                            (TABLE_RECT.x - PLAYER_INFO_BAR_WIDTH + 85,TABLE_RECT.y + TABLE_HEIGHT),
#                            (TABLE_RECT.x - PLAYER_INFO_BAR_WIDTH + 85,TABLE_RECT.y + 100)]

# __betButton_y = PLAYER_INFO_BAR_POSITION[2][1] + (PLAYER_INFO_BAR_HEIGHT/2) - BUTTON_HEIGHT/2
# __betButton_x = PLAYER_INFO_BAR_POSITION[2][0] #initial pos
# __raise_pos   = PLAYER_INFO_BAR_WIDTH + BUTTON_WIDTH + BUTTON_GAP*2

# gamePageButtons = [Button(kw.CHECK    ,pygame.Rect(__betButton_x - (BUTTON_GAP + BUTTON_WIDTH)*1,__betButton_y,BUTTON_WIDTH,BUTTON_HEIGHT)),
#                    Button(kw.CALL     ,pygame.Rect(__betButton_x - (BUTTON_GAP + BUTTON_WIDTH)*2,__betButton_y,BUTTON_WIDTH,BUTTON_HEIGHT)),
#                    Button(kw.FOLD     ,pygame.Rect(__betButton_x - (BUTTON_GAP + BUTTON_WIDTH)*3,__betButton_y,BUTTON_WIDTH,BUTTON_HEIGHT)),
#                    Button(kw.BET_RAISE,pygame.Rect(__betButton_x + __raise_pos ,__betButton_y,BUTTON_WIDTH,BUTTON_HEIGHT)),
#                    Button(kw.DECREASE ,pygame.Rect(__betButton_x + __raise_pos - BUTTON_WIDTH*SETTING_WIDTH_SCALE - BUTTON_GAP,__betButton_y + (BUTTON_HEIGHT - BUTTON_HEIGHT*SETTING_HEIGHT_SCALE)/2,BUTTON_WIDTH*SETTING_WIDTH_SCALE,BUTTON_HEIGHT*SETTING_HEIGHT_SCALE),flag=1),
#                    Button(kw.INCREASE ,pygame.Rect(__betButton_x + __raise_pos + BUTTON_WIDTH                     + BUTTON_GAP,__betButton_y + (BUTTON_HEIGHT - BUTTON_HEIGHT*SETTING_HEIGHT_SCALE)/2,BUTTON_WIDTH*SETTING_WIDTH_SCALE,BUTTON_HEIGHT*SETTING_HEIGHT_SCALE),flag=1)]

# loginPageButtons = [Button(kw.SIGN_IN ,pygame.Rect((SCREEN_WIDTH-120)/2 +80,500,120,60),flag=-1),
#                     Button(kw.SIGN_UP ,pygame.Rect((SCREEN_WIDTH-120)/2 -80,500,120,60),flag=-1)]

# def load_poker(path) -> dict:
#     """return a dictionary include {poker_name:poker_image_surface,...}"""
#     # nameList = os.listdir(path+'\\PNG-cards-1.3')
#     nameList = [i.replace('.png','') for i in os.listdir(path+'\\cards')]
#     pokerImages = {}
#     for i in range(len(nameList)):
#         pokerImage = pygame.image.load(f'{path}\\cards\\{nameList[i]}.png')
#         pokerImages[nameList[i]] = pokerImage
#     return pokerImages

# POKER_TABLE_RATIO = 0.19
# POKER_RATIO =  0.175

# def draw_reminder(playerCombination:list,bg_ratio = 1.3):
#     reminder_height = REMINDER_FONT.render('p',True,REMINDER_FONT_COLOR).get_height() # take the highest letter
#     for player in playerCombination:
#         reminder = REMINDER_FONT.render(player[0],True,REMINDER_FONT_COLOR)
#         if player == playerCombination[2]:
#             reminder_bg = pygame.Surface((reminder.get_width()*bg_ratio,reminder_height*bg_ratio),pygame.SRCALPHA)
#             pygame.draw.rect(reminder_bg,REMINDER_BG_COLOR,reminder_bg.get_rect(),0,12)
#             reminder_bg.blit(reminder,((reminder_bg.get_width()-reminder.get_width())/2,(reminder_bg.get_height()-reminder.get_height())/2))
#             # blit to screen
#             position = ((SCREEN_WIDTH - reminder.get_width()*bg_ratio)/2,((9*(TABLE_RECT.y+TABLE_HEIGHT))+(49*TABLE_RECT.y))/58 + POKER_PLACE_HEIGHT + GAP)
#             screen.blit(reminder_bg,position)
#         # dont want to do this part
#         elif CHEATING_MODE:
#             pass