from setting import *

class Button:
    '''draw a button in a Surface'''
    def __init__(self,
                 text:str,
                 rect:pygame.Rect,
                 color:tuple = BUTTON_COLOR,
                 touch_color:tuple = BUTTON_TOUCH_COLOR,
                 flag  = 0):
        """flag is button function,setting == -1 betting == 0,bet setting == 1"""
        self.text  = text
        self.rect  = rect
        self.color = color
        self.touch = touch_color
        self.flag  = flag

    def adjust_value(self,value):
        # increase /decrese
        if   self.text == INCREASE:
            return value + 100
        elif self.text == DECREASE:
            return value - 100

    def check(self, event:pygame.event):
        """return True when the button release"""
        # reset color in every loop
        self.color = BUTTON_COLOR
        self.touch = BUTTON_TOUCH_COLOR
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.touch = BUTTON_ACTIVE_TOUCH_COLOR
            # press
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.color = BUTTON_ACTIVE_COLOR
            # release
            elif event.type == pygame.MOUSEBUTTONUP:
                self.color = BUTTON_COLOR
                self.touch = BUTTON_TOUCH_COLOR
                return True
        return False

    def draw(self,c,invalidList:list = []):
        """draw the button"""
        pygame.draw.rect(screen,self.color, self.rect,0,25)
        pygame.draw.rect(screen,self.touch, self.rect,10,25)
        pygame.draw.rect(screen,self.color, self.rect,5,25)
        text = BUTTON_FONT.render(self.text,True,BUTTON_FONT_COLOR)
        screen.blit(text,((self.rect.x + self.rect.width/2) - text.get_width()/2,(self.rect.y + self.rect.height/2) - text.get_height()/2))
        if self.text == BET_RAISE:
            bet = BETTING_SIZE_FONT.render(str(c),True,BUTTON_FONT_COLOR)
            screen.blit(bet,(self.rect.x + (self.rect.width - bet.get_width())/2,(self.rect.y + self.rect.height/2) - text.get_height() - 5))
        if self.text in invalidList:
            invalid_layer = pygame.Surface((self.rect.width,self.rect.height),pygame.SRCALPHA)
            pygame.draw.rect(invalid_layer,(0,0,0,128),invalid_layer.get_rect(),0,25)
            screen.blit(invalid_layer,self.rect)
        pygame.display.flip()

## =====NO CHANGE=====
__betButton_y = PLAYER_INFO_BAR_POSITION[2][1] + (PLAYER_INFO_BAR_HEIGHT/2) - BUTTON_HEIGHT/2
__betButton_x = PLAYER_INFO_BAR_POSITION[2][0] #initial pos
__raise_pos   = PLAYER_INFO_BAR_WIDTH + BUTTON_WIDTH + BUTTON_GAP*2

gamePageButtons = [Button(CHECK    ,pygame.Rect(__betButton_x - (BUTTON_GAP + BUTTON_WIDTH)*1,__betButton_y,BUTTON_WIDTH,BUTTON_HEIGHT)),
                   Button(CALL     ,pygame.Rect(__betButton_x - (BUTTON_GAP + BUTTON_WIDTH)*2,__betButton_y,BUTTON_WIDTH,BUTTON_HEIGHT)),
                   Button(FOLD     ,pygame.Rect(__betButton_x - (BUTTON_GAP + BUTTON_WIDTH)*3,__betButton_y,BUTTON_WIDTH,BUTTON_HEIGHT)),
                   Button(BET_RAISE,pygame.Rect(__betButton_x + __raise_pos ,__betButton_y,BUTTON_WIDTH,BUTTON_HEIGHT)),
                   Button(DECREASE ,pygame.Rect(__betButton_x + __raise_pos - BUTTON_WIDTH*SETTING_WIDTH_SCALE - BUTTON_GAP,__betButton_y + (BUTTON_HEIGHT - BUTTON_HEIGHT*SETTING_HEIGHT_SCALE)/2,BUTTON_WIDTH*SETTING_WIDTH_SCALE,BUTTON_HEIGHT*SETTING_HEIGHT_SCALE),flag=1),
                   Button(INCREASE ,pygame.Rect(__betButton_x + __raise_pos + BUTTON_WIDTH                     + BUTTON_GAP,__betButton_y + (BUTTON_HEIGHT - BUTTON_HEIGHT*SETTING_HEIGHT_SCALE)/2,BUTTON_WIDTH*SETTING_WIDTH_SCALE,BUTTON_HEIGHT*SETTING_HEIGHT_SCALE),flag=1)]

loginPageButtons = [Button(SIGN_IN ,pygame.Rect((SCREEN_WIDTH-120)/2 +80,500,120,60),flag=-1),
                    Button(SIGN_UP ,pygame.Rect((SCREEN_WIDTH-120)/2 -80,500,120,60),flag=-1)]