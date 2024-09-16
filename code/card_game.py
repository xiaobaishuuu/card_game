from setting import *
from button import *
import time

def login_page():
    """login"""
    screen.fill(SCREEN_COLOR)
    pygame.draw.rect(screen,)
    
def draw_table(num=5):
    '''num: number of poker place'''
    pygame.draw.rect(screen,TABLE_COLOR,TABLE_RECT,0,1000)
    pygame.draw.rect(screen,TABLE_PADDING_COLOR,TABLE_RECT,50,1000)
    pygame.draw.rect(screen,TABLE_BORDER_COLOR,TABLE_RECT,10,1000)
    for i in range(num):
        x = TABLE_RECT.x + (TABLE_WIDTH - ((POKER_WIDTH*POKER_TABLE_RATIO)*num + GAP*(num-1)))/2 + ((POKER_WIDTH*POKER_TABLE_RATIO + GAP) * i)
        y = ((9*(TABLE_RECT.y+TABLE_HEIGHT))+(49*TABLE_RECT.y))/58
        pygame.draw.rect(screen,POKER_PLACE_COLOR,(x,y,POKER_WIDTH*POKER_TABLE_RATIO,POKER_HEIGHT*POKER_TABLE_RATIO),3,5)

def draw_reminder(playerCombination:list):
    for player in playerCombination:
        if player == playerCombination[2]:
            reminder = REMINDER_FONT.render(player[0],True,REMINDER_FONT_COLOR)

            pygame.draw.rect(screen,(7, 61, 31),(SCREEN_WIDTH/2 - ((reminder.get_width()*1.2)/2),300,(reminder.get_width()*1.2),(reminder.get_height()*1.2)),0,15)
            pygame.draw.rect(screen,REMINDER_FONT_COLOR,(SCREEN_WIDTH/2 - ((reminder.get_width()*1.2)/2),300,(reminder.get_width()*1.2),(reminder.get_height()*1.2)),1,13)

            reminder = REMINDER_FONT.render(player[0],True,REMINDER_FONT_COLOR)
            screen.blit(reminder,(640 - reminder.get_width()/2,300))

def draw_players(playerName:list,playerChip:list):
    for i in range(len(PLAYER_INFO_BAR_LIST)):
        pygame.draw.rect(PLAYER_INFO_BAR_LIST[i],PLAYER_INFO_BAR_COLOR,(0,0,PLAYER_INFO_BAR_WIDTH,PLAYER_INFO_BAR_HEIGHT),0,20)
        PLAYER_INFO_BAR_LIST[i].blit(PLAYER_NAME_FONT.render(playerName[i],True,PLAYER_NAME_FONT_COLOR),(70,25))
        PLAYER_INFO_BAR_LIST[i].blit(PLAYER_NAME_FONT.render(f'$ {round(playerChip[i])}',True,PLAYER_NAME_FONT_COLOR),(70,55))
        PLAYER_INFO_BAR_LIST[i].blit(pygame.transform.scale_by(PLAYER_ICON,PLAYER_ICON_RATIO),(0,20))
        screen.blit(PLAYER_INFO_BAR_LIST[i],PLAYER_INFO_BAR_POSITION[i])

def draw_card(playerId:int,card_id:str,position:tuple,deal:bool = False,fold:bool = False):
    '''playerId 1-5 == hand, -1 == community cards'''
    if deal:
        deal_animation(position)
    #player or community
    if playerId == 2 or playerId == -1:
        screen.blit(pygame.transform.smoothscale_by(POKER[card_id],POKER_RATIO),position)
    #bot
    else:
        screen.blit(pygame.transform.smoothscale_by(CARD_BACK,POKER_RATIO),position)
    #fold
    if fold == True:
        fold_layer = pygame.Surface((POKER_WIDTH*POKER_RATIO,POKER_HEIGHT*POKER_RATIO),pygame.SRCALPHA)
        pygame.draw.rect(fold_layer,(0,0,0,128),fold_layer.get_rect(),0,2)
        screen.blit(fold_layer,position)

def draw_hand(handList:list[list],gameRound:int,foldList = False):
    '''draw all hand card'''
    for i in range(len(PLAYER_INFO_BAR_LIST)):
        for j in range(2):
            if gameRound == 1:
                draw_card(i,handList[i][j],HAND_POSITION[i][j],True)
            draw_card(i,handList[i][j],HAND_POSITION[i][j],False,foldList[i])

def draw_community(community:list,gameRound:int,deal_range:range,conditon_num:int):
    '''"deal_range" is the range of dealing card(start with 0)\n
    "conditon_num" is which round will deal the card in animation'''
    for i in deal_range:
        if gameRound == conditon_num:
            draw_card(-1,community[i],COMMUNITY_CARDS_POSITION[i],True)
        draw_card(-1,community[i],COMMUNITY_CARDS_POSITION[i])

def deal_animation(position:tuple,duration:int = 0.3):
    '''deal single card animation'''
    frame = screen.copy()
    start_time = time.time()
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        #check animation time
        progress = min((time.time() - start_time) / duration, 1.0)
        #change pos
        x = POKER_INITIAL_POSITION[0] + (position[0] - POKER_INITIAL_POSITION[0]) * progress
        y = POKER_INITIAL_POSITION[1] + (position[1] - POKER_INITIAL_POSITION[1]) * progress
        screen.blit(frame,(0,0))
        screen.blit(pygame.transform.smoothscale_by(CARD_BACK,POKER_RATIO),(x,y))
        pygame.display.flip()
        #end the animation
        if progress >= 1.0:
            break

def check_button(playerChip:int,least_bet = 0,press = False,invalidList:list = []) -> dict[str,int]:
    '''press: True will pass,return button name\n
       invalidList: receive keyword to ban button'''
    choice = FOLD
    Button.init_raise(least_bet)
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # elif event.type == pygame.VIDEORESIZE:
            #     screen = pygame.display.set_mode(event.size,pygame.RESIZABLE)
            # only check
            for button in buttonList:
                #check betting button
                if (button.text not in invalidList) and button.check(event):
                    choice = button.text
                    #either betting button press
                    if button.flag == 0:
                        press = True
        # only draw
        for button in buttonList:
            button.draw(screen,playerChip,invalidList)
        if press:
            break
    return {'choice':choice,'bet':button.get_raise() if choice == BET_RAISE else least_bet}

def draw_blind(small_blind):
    pass
