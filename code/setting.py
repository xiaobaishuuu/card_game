import os.path,os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from keywords import *
# ====================================CAN CHANGE==========================================
# screen setting
SCREEN_HEIGHT= 720
SCREEN_WIDTH = 1280
SCREEN_COLOR = (242, 225, 231)

# FPS setting
FPS = 120

#draw table
TABLE_HEIGHT= 580
TABLE_WIDTH = 1000
TABLE_COLOR = (17, 113, 61)
TABLE_PADDING_COLOR= (77, 39, 18)
TABLE_BORDER_COLOR = (0, 0, 0)

#draw card
GAP = 5
POKER_WIDTH = 500
POKER_HEIGHT= 726
POKER_RATIO =  0.175
POKER_PLACE_COLOR = (204, 204, 204)
POKER_TABLE_RATIO = 0.18

#draw player
PLAYER_ICON_RATIO = 0.20
PLAYER_NAME_FONT_SIZE = 20
PLAYER_NAME_FONT_COLOR= (220, 220, 220)
PLAYER_INFO_BAR_HEIGHT= 100
PLAYER_INFO_BAR_WIDTH = 180
PLAYER_INFO_BAR_COLOR = (68, 45, 53)

#button
BUTTON_GAP   = 2.75
BUTTON_WIDTH = 105
BUTTON_HEIGHT= 75
BUTTON_FONT_SIZE = 20
BETTING_SIZE_FONT_SIZE = 15
BUTTON_FONT_COLOR= (255,255,255)
BUTTON_COLOR = (0,0,0)
BUTTON_ACTIVE_COLOR= (68, 45, 53)
BUTTON_TOUCH_COLOR = (68, 45, 53)
BUTTON_ACTIVE_TOUCH_COLOR = (255,255,255)

#reminder
REMINDER_FONT_SIZE = 20
REMINDER_FONT_COLOR = (220, 220, 220)
REMINDER_BG_COLOR = (204, 204, 204)

#cheat
CHEATING_MODE = False
# ====================================NO CHANGE==========================================

def load_poker(path) -> dict:
    """return a dictionary include {poker_name:poker_image_surface,...}"""
    # nameList = os.listdir(path+'\\PNG-cards-1.3')
    nameList = [i.replace('.png','') for i in os.listdir(path+'\\PNG-cards-1.3')]
    pokerImages = {}
    for i in range(52):
        pokerImage = pygame.image.load(f'{path}\\PNG-cards-1.3\\{nameList[i]}.png')
        pokerImages[nameList[i]] = pokerImage
    return pokerImages

# load image
imagePath = os.path.dirname(__file__).replace('code','image')
fontPath  = os.path.dirname(__file__).replace('code','font')
PLAYER_ICON = pygame.image.load(f'{imagePath}\\User.jpg')
CARD_BACK = pygame.image.load(f'{imagePath}\\card_back.png')
POKER = load_poker(imagePath)


#init
pygame.init()
pygame.display.set_caption('Card Game')
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
# screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.RESIZABLE)
screen.fill(SCREEN_COLOR)
clock = pygame.time.Clock()

#button
BUTTON_FONT = pygame.font.Font(f'{fontPath}\\FreeSansBold.ttf',BUTTON_FONT_SIZE)
BETTING_SIZE_FONT = pygame.font.Font(f'{fontPath}\\FreeSansBold.ttf',BETTING_SIZE_FONT_SIZE)
SETTING_WIDTH_SCALE  = 0.6
SETTING_HEIGHT_SCALE = 0.7
buttonList = [...] #(in button.py)

# reminder
REMINDER_FONT = pygame.font.Font(f'{fontPath}\\FreeSansBold.ttf',REMINDER_FONT_SIZE)

#table
TABLE_RECT  = pygame.Rect((SCREEN_WIDTH-TABLE_WIDTH)/2,(3/14)*(SCREEN_HEIGHT-TABLE_HEIGHT),TABLE_WIDTH,TABLE_HEIGHT)

# player info
PLAYER_NAME_FONT = pygame.font.Font(f'{fontPath}\\FreeSansBold.ttf',PLAYER_NAME_FONT_SIZE)
PLAYER_INFO_BAR_LIST = [pygame.Surface((PLAYER_INFO_BAR_WIDTH,PLAYER_INFO_BAR_HEIGHT),pygame.SRCALPHA) for i in range(5)]
PLAYER_INFO_BAR_POSITION= [(TABLE_RECT.x + TABLE_WIDTH - 85,TABLE_RECT.y + 100),
                           (TABLE_RECT.x + TABLE_WIDTH - 85,TABLE_RECT.y + TABLE_HEIGHT),
                           (SCREEN_WIDTH/2 - PLAYER_INFO_BAR_WIDTH/2,TABLE_RECT.y + TABLE_HEIGHT),
                           (TABLE_RECT.x - PLAYER_INFO_BAR_WIDTH + 85,TABLE_RECT.y + TABLE_HEIGHT),
                           (TABLE_RECT.x - PLAYER_INFO_BAR_WIDTH + 85,TABLE_RECT.y + 100)]

#card
POKER_INITIAL_POSITION = [(SCREEN_WIDTH/2)-(POKER_WIDTH*POKER_RATIO/2),0]
POKER_TABLE_START_POSITION = (SCREEN_WIDTH/2 - (POKER_WIDTH*POKER_RATIO/2) + (-(POKER_WIDTH*POKER_TABLE_RATIO - POKER_WIDTH*POKER_RATIO) -GAP -(POKER_WIDTH*POKER_RATIO))*2,
                              TABLE_RECT.y + 90 +(POKER_HEIGHT*POKER_TABLE_RATIO - POKER_HEIGHT*POKER_RATIO)/2)

# 需要改
HAND_POSITION = [[(PLAYER_INFO_BAR_POSITION[i][0]+((200 - (POKER_WIDTH*POKER_RATIO*2 - 30))/2),PLAYER_INFO_BAR_POSITION[i][1]-130),
                  (PLAYER_INFO_BAR_POSITION[i][0]+200-((200 - (POKER_WIDTH*POKER_RATIO*2 - 30))/2)-(POKER_WIDTH*POKER_RATIO),PLAYER_INFO_BAR_POSITION[i][1]-130)]
                  for i in range(len(PLAYER_INFO_BAR_POSITION))]
COMMUNITY_CARDS_POSITION = [(POKER_TABLE_START_POSITION[0] + ((POKER_WIDTH*POKER_TABLE_RATIO - POKER_WIDTH*POKER_RATIO) + GAP + (POKER_WIDTH*POKER_RATIO))* i,
                             POKER_TABLE_START_POSITION[1]) for i in range(5)]