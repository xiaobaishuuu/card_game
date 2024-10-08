from setting import *
from button import *
from input_box import *
import keywords as kw
import time

def introduction():
    title = TITLE_FONT.render(TITLE_TEXT,True,TITLE_FONT_COLOR)
    init_pos = ((SCREEN_WIDTH-title.get_width())/2,(SCREEN_HEIGHT-title.get_height())/2)
    final_position = ((SCREEN_WIDTH-title.get_width())/2,150)
    move_animation(title,init_pos,final_position,1,0)

def invalid_input():
    REMINDER_FONT.render()

def choose_game():
    pass

def draw_table(num=5):
    '''num: number of poker place'''
    pygame.draw.rect(screen,TABLE_COLOR,TABLE_RECT,0,1000)
    pygame.draw.rect(screen,TABLE_PADDING_COLOR,TABLE_RECT,50,1000)
    pygame.draw.rect(screen,TABLE_BORDER_COLOR,TABLE_RECT,10,1000)
    for i in range(num):
        x = TABLE_RECT.x + (TABLE_WIDTH - ((POKER_PLACE_WIDTH)*num + GAP*(num-1)))/2 + ((POKER_PLACE_WIDTH + GAP) * i)
        y = ((9*(TABLE_RECT.y+TABLE_HEIGHT))+(49*TABLE_RECT.y))/58   # ac:cb = 9:49
        pygame.draw.rect(screen,POKER_PLACE_COLOR,(x,y,POKER_PLACE_WIDTH,POKER_PLACE_HEIGHT),3,5)

def draw_reminder(playerCombination:list,bg_ratio = 1.3):
    reminder_height = REMINDER_FONT.render('p',True,REMINDER_FONT_COLOR).get_height() # take the highest letter
    for player in playerCombination:
        reminder = REMINDER_FONT.render(player[0],True,REMINDER_FONT_COLOR)
        if player == playerCombination[2]:
            reminder_bg = pygame.Surface((reminder.get_width()*bg_ratio,reminder_height*bg_ratio),pygame.SRCALPHA)
            pygame.draw.rect(reminder_bg,REMINDER_BG_COLOR,reminder_bg.get_rect(),0,12)
            reminder_bg.blit(reminder,((reminder_bg.get_width()-reminder.get_width())/2,(reminder_bg.get_height()-reminder.get_height())/2))
            # blit to screen
            position = ((SCREEN_WIDTH - reminder.get_width()*bg_ratio)/2,((9*(TABLE_RECT.y+TABLE_HEIGHT))+(49*TABLE_RECT.y))/58 + POKER_PLACE_HEIGHT + GAP)
            screen.blit(reminder_bg,position)
        # dont want to do this part
        elif CHEATING_MODE:
            pass

def draw_chip():
    screen.blit(CHIP['black'],(0,0))
    pygame.display.flip()


def draw_blind(small_blind= 1):
    return
    a = pygame.Surface((TABLE_WIDTH*(16/29),TABLE_HEIGHT*(16/29)),pygame.SRCALPHA)
    pygame.draw.rect(a,(0,0,0),a.get_rect())
    screen.blit(a,(SCREEN_WIDTH/2 - TABLE_WIDTH*(16/29)/2,TABLE_RECT.y + (TABLE_HEIGHT*(16/29)/2)))

def draw_winner(winner,c):
    print('=============WINNER==================')
    # print(c)
    print(winner)

def draw_players(seat:int,playerName:str,playerChip:int):
    """player seat : 0 - 4"""
    pygame.draw.rect(PLAYER_INFO_BAR_LIST[seat],PLAYER_INFO_BAR_COLOR,(0,0,PLAYER_INFO_BAR_WIDTH,PLAYER_INFO_BAR_HEIGHT),0,20)
    PLAYER_INFO_BAR_LIST[seat].blit(PLAYER_NAME_FONT.render(playerName,True,PLAYER_NAME_FONT_COLOR),(70,25))
    PLAYER_INFO_BAR_LIST[seat].blit(PLAYER_NAME_FONT.render(f'$ {round(playerChip)}',True,PLAYER_NAME_FONT_COLOR),(70,55))
    PLAYER_INFO_BAR_LIST[seat].blit(PLAYER_ICON,(0,20))
    screen.blit(PLAYER_INFO_BAR_LIST[seat],PLAYER_INFO_BAR_POSITION[seat])

def draw_hand(seat:int,hand:list,fold = False,deal:bool = False):
    '''draw all hand card'''
    for i in range(2):
        draw_card(seat,hand[i],HAND_POSITION[seat][i],deal,fold)

def draw_community(community:list,deal_range:range,deal:bool = False):
    '''"deal_range" is the range of dealing card(start with 0)\n'''
    for i in deal_range:
        draw_card(-1,community[i],COMMUNITY_CARDS_POSITION[i],deal)

def draw_card(playerId:int,card_id:str,position:tuple,deal:bool = False,fold:bool = False):
    '''playerId 1-5 == hand, -1 == community cards'''
    if deal:
        move_animation(CARD_BACK,POKER_INITIAL_POSITION,position,0.5)
    #2 player or -1 community
    if playerId in [-1,2] or CHEATING_MODE or fold:
        screen.blit(POKER[card_id],position)
    #bot
    else:
        screen.blit(CARD_BACK,position)
    #fold
    if fold == True:
        fold_layer = pygame.Surface((POKER_WIDTH,POKER_HEIGHT),pygame.SRCALPHA)
        pygame.draw.rect(fold_layer,(0,0,0,128),fold_layer.get_rect(),0,2)
        screen.blit(fold_layer,position)

def draw_consideration(seat:int,pause_time:int = 15):
    """thinking time is limited for 15s"""
    start_time = time.time()
    max_time = 1
    init_x  = PLAYER_INFO_BAR_POSITION[seat][0] + PLAYER_INFO_BAR_WIDTH*0.045
    final_x = PLAYER_INFO_BAR_POSITION[seat][0]+PLAYER_INFO_BAR_LIST[seat].get_width() - PLAYER_INFO_BAR_WIDTH*0.045
    y = PLAYER_INFO_BAR_POSITION[seat][1] + 20/2
    frame = screen.copy()
    pygame.draw.line(screen, (0,0,0), (init_x,y), (final_x,y),6)
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise QuitGame
        progress = (time.time() - start_time) / max_time
        x = init_x + (final_x - init_x) * progress
        pygame.draw.line(screen, (255,255,255), (init_x,y), (x,y),6)
        pygame.display.flip()
        if progress >= 1 or (time.time() - start_time)/pause_time >= 1:
            screen.blit(frame,(0,0))
            break

def move_animation(obj:pygame.Surface,init_pos:tuple,final_pos:tuple,duration:int,alpha:float=255):
    '''animation'''
    frame = screen.copy()
    start_time = time.time()
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise QuitGame
        #check animation time
        progress = min((time.time() - start_time) / duration,1)
        #change pos
        x = init_pos[0] + (final_pos[0] - init_pos[0]) * progress
        y = init_pos[1] + (final_pos[1] - init_pos[1]) * progress
        #set alpha channel
        if alpha < 255:
            alpha += 255/(duration*FPS)
        obj.set_alpha(alpha)
        screen.blit(frame,(0,0))
        screen.blit(obj,(x,y))
        pygame.display.flip()
        #end the animation
        if progress >= 1 and alpha >= 255:
            break

def interact(playerChip:int = -1,
             least_bet = 0,
             press = False,
             invalidList:list = [],
             buttonList:list[Button] = gamePageButtons,
             inputList:list[Input] = []) -> dict:
    '''press: True will pass,return button name\n
       invalidList: receive keyword to ban button'''
    bet = least_bet + 100
    call = least_bet
    result = {}

    def calculate_bet(raise_bet):
        nonlocal bet
        bet += raise_bet
        if   bet > playerChip: bet = playerChip  # excced max
        elif bet < least_bet +100: bet = least_bet +100   # exceed min

    while not press:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise QuitGame
            # only check
            for input_box in inputList:
                input_box.check(event)
            for button in buttonList:
                #check button
                if (button.text not in invalidList) and button.check(event):
                    result['choice'] = button.text
                    if   button.flag == 1:
                        calculate_bet(button.adjust_value(5000))  #暂时处理，实际数值于PLayer()中定
                        continue
                    elif button.flag == 0:
                        result['bet'] = bet
                    elif button.flag == -1:
                        result.update({input_box.text:input_box.content for input_box in inputList})
                    press = True
        # only draw
        for button in buttonList:
            value = None
            if button.text == kw.CALL:        value = call
            elif button.text == kw.BET_RAISE: value = bet
            button.draw(button.text in invalidList,value)

        for input_box in inputList: input_box.draw()
    return result

draw_table()