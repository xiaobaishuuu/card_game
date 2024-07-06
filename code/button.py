from setting import *

class Button:
    '''draw a button in a Surface'''

    # 不想改了，只能写这里了
    # bet = raising bet + least bet
    __least_bet = 0
    __raising_bet = 0

    def __init__(self,
                 text:str,
                 rect:pygame.Rect,
                 color = BUTTON_COLOR,
                 touch_color = BUTTON_TOUCH_COLOR,
                 flag  = 0):
        """flag is button function,setting == -1 betting == 0,bet setting == 1"""
        self.text  = text
        self.rect  = rect
        self.color = color
        self.touch = touch_color
        self.flag  = flag

    @classmethod
    def init_raise(cls,least_bet):
        cls.__raising_bet = 0
        cls.__least_bet = least_bet

    @classmethod
    def get_raise(cls) -> int:
        '''return the bet after player raise'''
        return cls.__least_bet + cls.__raising_bet

    @classmethod
    def __calculate_bet(cls,playerChip) -> int:
        # excced max
        if cls.__least_bet + cls.__raising_bet > playerChip:
            cls.__raising_bet = playerChip - cls.__least_bet
        # exceed min
        elif cls.__least_bet + cls.__raising_bet < cls.__least_bet:
            cls.__raising_bet = 0
        return round(cls.__least_bet + cls.__raising_bet)

    def check(self, event:pygame.event):
        """return True when the button release"""
        # reset color in every loop
        self.color = BUTTON_COLOR
        self.touch = BUTTON_TOUCH_COLOR
        # mouse out of screen will lead to attr errer (null event.pos)
        try:
            if self.rect.collidepoint(event.pos):
                self.touch = BUTTON_ACTIVE_TOUCH_COLOR
                # press
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.color = BUTTON_ACTIVE_COLOR
                # release
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.color = BUTTON_COLOR
                    self.touch = BUTTON_TOUCH_COLOR
                    # inc/dec the bet
                    if   self.text == INCREASE:
                        Button.__raising_bet += 100
                    elif self.text == DECREASE:
                        Button.__raising_bet -= 100
                    return True
        except AttributeError:
            pass
        return False

    def draw(self, screen:pygame.Surface,playerChip:int,invalidList:list = []):
        """draw the button"""
        pygame.draw.rect(screen,self.color, self.rect,0,25)
        pygame.draw.rect(screen,self.touch, self.rect,10,25)
        pygame.draw.rect(screen,self.color, self.rect,5,25)
        text = BUTTON_FONT.render(self.text,True,BUTTON_FONT_COLOR)
        screen.blit(text,((self.rect.x + self.rect.width/2) - text.get_width()/2,(self.rect.y + self.rect.height/2) - text.get_height()/2))
        if self.text == BET_RAISE:
            bet = BETTING_SIZE_FONT.render(str(Button.__calculate_bet(playerChip)),True,BUTTON_FONT_COLOR)
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

buttonList = [Button(CHECK    ,pygame.Rect(__betButton_x - (BUTTON_GAP + BUTTON_WIDTH)*1,__betButton_y,BUTTON_WIDTH,BUTTON_HEIGHT)),
              Button(CALL     ,pygame.Rect(__betButton_x - (BUTTON_GAP + BUTTON_WIDTH)*2,__betButton_y,BUTTON_WIDTH,BUTTON_HEIGHT)),
              Button(FOLD     ,pygame.Rect(__betButton_x - (BUTTON_GAP + BUTTON_WIDTH)*3,__betButton_y,BUTTON_WIDTH,BUTTON_HEIGHT)),
              Button(BET_RAISE,pygame.Rect(__betButton_x + __raise_pos ,__betButton_y,BUTTON_WIDTH,BUTTON_HEIGHT)),
              Button(DECREASE ,pygame.Rect(__betButton_x + __raise_pos - BUTTON_WIDTH*SETTING_WIDTH_SCALE - BUTTON_GAP,__betButton_y + (BUTTON_HEIGHT - BUTTON_HEIGHT*SETTING_HEIGHT_SCALE)/2,BUTTON_WIDTH*SETTING_WIDTH_SCALE,BUTTON_HEIGHT*SETTING_HEIGHT_SCALE),flag=1),
              Button(INCREASE ,pygame.Rect(__betButton_x + __raise_pos + BUTTON_WIDTH                     + BUTTON_GAP,__betButton_y + (BUTTON_HEIGHT - BUTTON_HEIGHT*SETTING_HEIGHT_SCALE)/2,BUTTON_WIDTH*SETTING_WIDTH_SCALE,BUTTON_HEIGHT*SETTING_HEIGHT_SCALE),flag=1)]