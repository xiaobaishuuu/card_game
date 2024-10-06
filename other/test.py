# from init import *

# def draw_table():
#     pygame.draw.rect(screen,TABLE_COLOR,TABLE_RECT,0,1000)
#     pygame.draw.rect(screen,TABLE_PADDING_COLOR,TABLE_RECT,50,1000)
#     pygame.draw.rect(screen,TABLE_BORDER_COLOR,TABLE_RECT,10,1000)
#     for i in range(5):
#         pygame.draw.rect(screen,POKER_PLACE_COLOR,(405+(5+POKER_WIDTH*POKER_TABLE_RATIO)*i,120,POKER_WIDTH*POKER_TABLE_RATIO,POKER_HEIGHT*POKER_TABLE_RATIO),3,5)                                       
#         # pygame.draw.rect(screen,POKER_PLACE_COLOR,(POKER_TABLE_START_POSITION[0] - (POKER_WIDTH*POKER_TABLE_RATIO - POKER_WIDTH*POKER_RATIO)/2 + 5 + (POKER_WIDTH*POKER_RATIO) +  , 
#         # pygame.draw.rect(screen,POKER_PLACE_COLOR,(POKER_TABLE_START_POSITION[0]+ ((POKER_WIDTH*POKER_TABLE_RATIO - POKER_WIDTH*POKER_RATIO) +5 +(POKER_WIDTH*POKER_RATIO))*i,
#                                                 #    POKER_TABLE_START_POSITION[1]-(POKER_HEIGHT*POKER_TABLE_RATIO - POKER_HEIGHT*POKER_RATIO)/2
#                                                 #    ,POKER_WIDTH*POKER_TABLE_RATIO,POKER_HEIGHT*POKER_TABLE_RATIO),3,5)
#     # x: (640-(500*0.18/2)- 5 - (500*0.18)*n
#     # pygame.draw.rect(screen,POKER_PLACE_COLOR,(640-(500*0.18/2),120,POKER_WIDTH*POKER_TABLE_RATIO,POKER_HEIGHT*POKER_TABLE_RATIO),0,0)

# def draw_players():
#     for i in range(len(PLAYER_INFO_BAR_LIST)):
#         pygame.draw.rect(PLAYER_INFO_BAR_LIST[i],PLAYER_INFO_BAR_COLOR,(0,0,PLAYER_INFO_BAR_WIDTH,PLAYER_INFO_BAR_HEIGHT),0,20) 
#         PLAYER_INFO_BAR_LIST[i].blit(PLAYER_NAME_FONT.render(f'User {i+1}',True,PLAYER_NAME_FONT_COLOR),(70,25))
#         PLAYER_INFO_BAR_LIST[i].blit(PLAYER_NAME_FONT.render(f'$ {play_chip[i]}',True,PLAYER_NAME_FONT_COLOR),(70,55))
#         PLAYER_INFO_BAR_LIST[i].blit(pygame.transform.scale_by(PLAYER_ICON,PLAYER_ICON_RATIO),(0,20))
#         screen.blit(PLAYER_INFO_BAR_LIST[i],PLAYER_INFO_BAR_POSITION[i])

# def draw_card(playerId:int,card_id:str,position:tuple,deal:bool = False):
#     '''playerId 1-5 == hand, -1 == community cards'''
#     if deal:
#         deal_animation(position)
#     #player
#     if playerId == 2 or playerId == -1:
#         screen.blit(pygame.transform.smoothscale_by(POKER[card_id],POKER_RATIO),position)
#     #bot
#     else:
#         screen.blit(pygame.transform.smoothscale_by(CARD_BACK,POKER_RATIO),position)

# def deal_animation(position:tuple,duration:int = 0.3):
#     frame = screen.copy()
#     start_pos = [596.25,0]
#     start_time = time.time()
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 exit()
#         progress = min((time.time() - start_time) / duration, 1.0)
#         current_x = start_pos[0] + (position[0] - start_pos[0]) * progress
#         current_y = start_pos[1] + (position[1] - start_pos[1]) * progress
#         screen.blit(frame,(0,0))
#         # if playerId == 2 or playerId == -1:
#         #     screen.blit(pygame.transform.smoothscale_by(POKER[card_id],POKER_RATIO),(current_x, current_y))
#         # else:
#         screen.blit(pygame.transform.smoothscale_by(CARD_BACK,POKER_RATIO),(current_x, current_y))
#         pygame.display.flip()
#         if progress >= 1.0:
#             break
# playersList = [1,2,3,4,5]
# small_blind = 0
# big_blind = small_blind + 1
# small_blind = 0 if small_blind >= len(playersList) else small_blind
# big_blind = 1 if big_blind >= len(playersList) else big_blind

#   ,handList=[['2_1','2_1'],['4_1','5_1'],['14_1','5_1'],['8_1','9_1'],['10_1','11_1']],
#   communityCardsList=['8_1','9_1','10_1','5_1','5_1'])

#   prime: 2 3 5 7 11 13 17 19 23 29 31 37 41
#   rank : 2 3 4 5 6  7  8  9  10  J Q  K  A

# #   xxxAKQJT 98765432 CDHSrrrr xxPPPPPP
#    x =0b00000_00000001
#    y =0b00000_00000010
#    z =0b00000_00000100

# #   00001000 00000000 01001011 00100101    King of Diamonds
# #   00000000 00001000 00010011 00000111    Five of Spades
# #   00000010 00000000 10001001 00011101    Jack of Clubs

# a = 0b00000010_00000000_10001001_00011101
# b = 0b00000000_00001000_10000011_00000111


#                         # 10000000 00000000
#                         # 10000001_00000101
#     # 0b      10 00001000 10001011 00011111
# # print(0xF000)
# # print(bin(a & b & 0xF000))
# # print(a)
# a = int(0b1,2)
# print(a)

# l = 最少下注額
# a 下注 100 l = 100

# b 下注 200 l = 200

# c 下注 300 l = 300
# ==================
# a 跟住 200 l = 300 - 100

# b 跟住 100 l = 300 - 200

# check
# def calculate_bet(playerChip,least_bet,raise_bet):
#     # excced max
#     if least_bet + raise_bet > playerChip:
#         raise_bet = playerChip - least_bet
#     # exceed min
#     elif least_bet + raise_bet < least_bet:
#         raise_bet = 0
#     return least_bet + raise_bet

# def adjust_value(a,b):
#     return a + b

# playerChip = 100
# least_bet = 100
# bet = least_bet
# raise_bet = 0

# raise_bet = adjust_value(raise_bet,int(input()))
# bet = calculate_bet(playerChip,least_bet,raise_bet
