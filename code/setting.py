import os.path
import pygame
import keywords as kw
# ====================================CAN CHANGE==========================================
# screen setting
SCREEN_HEIGHT= 750
SCREEN_WIDTH = 1380
SCREEN_COLOR = (242, 225, 231)

# FPS setting
FPS = 120

# title
TITLE_FONT_SIZE = 72
TITLE_FONT_COLOR= (255,255,255)

# login page
INPUT_BOX_WIDTH = 320
INPUT_FONT_SIZE = 22
INPUT_FONT_COLOR= (231, 231, 231)
LOGIN_REMINDER_BG_COLOR = (5, 36, 19)

# table
TABLE_WIDTH = 1000
TABLE_HEIGHT= 580
TABLE_COLOR = (17, 113, 61)
TABLE_PADDING_COLOR= (77, 39, 18)
TABLE_BORDER_COLOR = (0, 0, 0)

# cards
GAP = 5
POKER_WIDTH = 87.5
POKER_HEIGHT= 127.05
POKER_PLACE_COLOR = (204, 204, 204)
POKER_PLACE_WIDTH = 95
POKER_PLACE_HEIGHT= 137.94

# player info
PLAYER_ICON_WIDTH = 60
PLAYER_ICON_HEIGHT= 60
PLAYER_NAME_FONT_SIZE = 20
PLAYER_NAME_FONT_COLOR= (220, 220, 220)
PLAYER_INFO_BAR_WIDTH = 220
PLAYER_INFO_BAR_HEIGHT= 100
PLAYER_INFO_BAR_COLOR = (68, 45, 53)
PLAYER_INFO_BAR_MARGIN= 5   # distance from the edge of scree

# player betting info
PLAYER_BETTEING_INFO_WIDTH = 160
PLAYER_BETTEING_INFO_HEIGHT= 70

# chips
CHIP_WIDTH = 40
CHIP_HEIGHT= 40

# button  edit:(in button.py)
BUTTON_FONT_SIZE = 20
BETTING_SIZE_FONT_SIZE = 15
BUTTON_FONT_COLOR = (255,255,255)
BUTTON_COLOR = (0,0,0)
BUTTON_TOUCH_COLOR  = (68, 45, 53)
BUTTON_ACTIVE_COLOR = (68, 45, 53)
BUTTON_ACTIVE_TOUCH_COLOR = (255,255,255)

# reminder
COMBO_REMINDER_PADDING  = 10
COMBO_REMINDER_BG_COLOR = (7, 61, 31)
BETTING_REMINDER_PADDING  = 25
BETTING_REMINDER_BG_COLOR = (11, 15, 11)
REMINDER_HEIGHT     = 30
REMINDER_FONT_SIZE  = 20
REMINDER_FONT_COLOR = (220, 220, 220)

#cheat
CHEATING_MODE = False

# ====================================NO CHANGE==========================================

# quitgame
class QuitGame(Exception):
    pass

def load_image(path,size = None) -> dict:
    """return a dictionary include {file_name:image_surface,...}"""
    # nameList = os.listdir(path+'\\PNG-cards-1.3')
    nameList = [i.replace('.png','') for i in os.listdir(path)]
    imageList = {}
    for i in range(len(nameList)):
        image = pygame.image.load(f'{path}\\{nameList[i]}.png')
        if size:
            image = pygame.transform.smoothscale(image,size)
        imageList[nameList[i]] = image
    return imageList

# path
imagePath = os.path.dirname(__file__).replace('code','image')
fontPath  = os.path.dirname(__file__).replace('code','font')

# load image
PLAYER_ICON = pygame.transform.smoothscale(pygame.image.load(f'{imagePath}\\User.jpg'),(PLAYER_ICON_WIDTH,PLAYER_ICON_HEIGHT))
CARD_BACK   = pygame.transform.smoothscale(pygame.image.load(f'{imagePath}\\card_back.png'),(POKER_WIDTH,POKER_HEIGHT))
POKER = load_image(imagePath+'\\cards',(POKER_WIDTH,POKER_HEIGHT))
CHIP  = load_image(imagePath+'\\chips',(CHIP_WIDTH,CHIP_HEIGHT))

# init
pygame.init()
pygame.display.set_caption('Card Game')
clock  = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# title
TITLE_FONT = pygame.font.Font(f'{fontPath}\\FreeSansBold.ttf',TITLE_FONT_SIZE)

# login page
USERNAME_BOX_RECT   = pygame.Rect((SCREEN_WIDTH-INPUT_BOX_WIDTH)/2,300,INPUT_BOX_WIDTH,INPUT_FONT_SIZE*2)
PASSWORD_BOX_RECT   = pygame.Rect((SCREEN_WIDTH-INPUT_BOX_WIDTH)/2,370,INPUT_BOX_WIDTH,INPUT_FONT_SIZE*2)
C_PASSWORD_BOX_RECT = pygame.Rect((SCREEN_WIDTH-INPUT_BOX_WIDTH)/2,440,INPUT_BOX_WIDTH,INPUT_FONT_SIZE*2)
INPUT_FONT = pygame.font.Font(f'{fontPath}\\FreeSansBold.ttf',INPUT_FONT_SIZE)

# button
BUTTON_FONT = pygame.font.Font(f'{fontPath}\\FreeSansBold.ttf',BUTTON_FONT_SIZE)
BETTING_SIZE_FONT = pygame.font.Font(f'{fontPath}\\FreeSansBold.ttf',BETTING_SIZE_FONT_SIZE)
buttonList = [...] #(in button.py)

# reminder
REMINDER_FONT = pygame.font.Font(f'{fontPath}\\FreeSansBold.ttf',REMINDER_FONT_SIZE)

# table
TABLE_RECT = pygame.Rect((SCREEN_WIDTH-TABLE_WIDTH)/2,(3/14)*(SCREEN_HEIGHT-TABLE_HEIGHT),TABLE_WIDTH,TABLE_HEIGHT)

# player info
PLAYER_NAME_FONT = pygame.font.Font(f'{fontPath}\\FreeSansBold.ttf',PLAYER_NAME_FONT_SIZE)
PLAYER_INFO_BAR_LIST = [pygame.Surface((PLAYER_INFO_BAR_WIDTH,PLAYER_INFO_BAR_HEIGHT),pygame.SRCALPHA) for i in range(5)]
PLAYER_INFO_BAR_POSITION= [(SCREEN_WIDTH - PLAYER_INFO_BAR_MARGIN - PLAYER_INFO_BAR_WIDTH,TABLE_RECT.y + 150),
                           (SCREEN_WIDTH - PLAYER_INFO_BAR_MARGIN - PLAYER_INFO_BAR_WIDTH,TABLE_RECT.y + TABLE_HEIGHT + REMINDER_HEIGHT),
                           (SCREEN_WIDTH/2 - PLAYER_INFO_BAR_WIDTH/2,TABLE_RECT.y + TABLE_HEIGHT + REMINDER_HEIGHT),
                           (PLAYER_INFO_BAR_MARGIN,TABLE_RECT.y + TABLE_HEIGHT + REMINDER_HEIGHT),
                           (PLAYER_INFO_BAR_MARGIN,TABLE_RECT.y + 150)]

# player betting info
PLAYER_BETTEING_INFO_LIST = [pygame.Surface((PLAYER_INFO_BAR_WIDTH,REMINDER_HEIGHT),pygame.SRCALPHA) for i in range(5)]

# cards
POKER_INITIAL_POSITION = ((SCREEN_WIDTH/2)-(POKER_WIDTH/2),0)
POKER_TABLE_START_POSITION = (SCREEN_WIDTH/2 - (POKER_WIDTH/2) + (-(POKER_PLACE_WIDTH - POKER_WIDTH) -GAP -(POKER_WIDTH))*2,
                              ((TABLE_RECT.y) * 96911 + (TABLE_RECT.y + TABLE_HEIGHT)* 19089)/116000) #ac:cb = 19089:96911

HAND_POSITION = [[(PLAYER_INFO_BAR_POSITION[i][0] + ((PLAYER_INFO_BAR_WIDTH - (POKER_WIDTH*2 - 30))/2),
                   PLAYER_INFO_BAR_POSITION[i][1] - POKER_HEIGHT - REMINDER_HEIGHT),
                  (PLAYER_INFO_BAR_POSITION[i][0] + PLAYER_INFO_BAR_WIDTH - ((PLAYER_INFO_BAR_WIDTH - (POKER_WIDTH*2 - 30))/2)-(POKER_WIDTH),
                   PLAYER_INFO_BAR_POSITION[i][1] - POKER_HEIGHT - REMINDER_HEIGHT)]
                  for i in range(len(PLAYER_INFO_BAR_POSITION))]

COMMUNITY_CARDS_POSITION = [(POKER_TABLE_START_POSITION[0] + ((POKER_PLACE_WIDTH - POKER_WIDTH) + GAP + (POKER_WIDTH))* i,
                             POKER_TABLE_START_POSITION[1]) for i in range(5)]