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

    def adjust_value(self):
        # increase /decrese
        if   self.text == kw.INCREASE: return  100
        elif self.text == kw.DECREASE: return -100

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

    def draw(self, invalid:bool,value = None):
        """draw the button\n
           value will render above the button text"""
        pygame.draw.rect(screen,self.color, self.rect,0,25)
        pygame.draw.rect(screen,self.touch, self.rect,10,25)
        pygame.draw.rect(screen,self.color, self.rect,5,25)
        text = BUTTON_FONT.render(self.text,True,BUTTON_FONT_COLOR)
        screen.blit(text,((self.rect.x + self.rect.width/2) - text.get_width()/2,(self.rect.y + self.rect.height/2) - text.get_height()/2))
        if value:
            value = BETTING_SIZE_FONT.render(str(value),True,BUTTON_FONT_COLOR)
            screen.blit(value,(self.rect.x + (self.rect.width - value.get_width())/2,(self.rect.y + self.rect.height/2) - text.get_height() - 5))
        if invalid:
            invalid_layer = pygame.Surface((self.rect.width,self.rect.height),pygame.SRCALPHA)
            pygame.draw.rect(invalid_layer,(0,0,0,128),invalid_layer.get_rect(),0,25)
            screen.blit(invalid_layer,self.rect)
        pygame.display.flip()

## =====NO CHANGE=====

# bet button
__betButton_width = 105
__betButton_height= 75
__betButton_y = PLAYER_INFO_BAR_POSITION[2][1] + (PLAYER_INFO_BAR_HEIGHT/2) - __betButton_height/2
__betButton_x = PLAYER_INFO_BAR_POSITION[2][0] #initial pos
__gap = (PLAYER_INFO_BAR_POSITION[1][0] - (PLAYER_INFO_BAR_POSITION[2][0] + PLAYER_INFO_BAR_WIDTH) - __betButton_width*3)/4
__raise_pos   = PLAYER_INFO_BAR_POSITION[2][0] + PLAYER_INFO_BAR_WIDTH + (PLAYER_INFO_BAR_POSITION[1][0] - (PLAYER_INFO_BAR_POSITION[2][0] + PLAYER_INFO_BAR_WIDTH) - __betButton_width)/2

gamePageButtons = [Button(kw.CHECK    ,pygame.Rect(__betButton_x - (__gap + __betButton_width)*1,__betButton_y,__betButton_width,__betButton_height)),
                   Button(kw.CALL     ,pygame.Rect(__betButton_x - (__gap + __betButton_width)*2,__betButton_y,__betButton_width,__betButton_height)),
                   Button(kw.FOLD     ,pygame.Rect(__betButton_x - (__gap + __betButton_width)*3,__betButton_y,__betButton_width,__betButton_height)),
                   Button(kw.BET_RAISE,pygame.Rect(__raise_pos ,__betButton_y,__betButton_width,__betButton_height)),
                   Button(kw.DECREASE ,pygame.Rect(__raise_pos - 63                - __gap,__betButton_y + (__betButton_height - 52.5)/2,63,52.5),flag=1),
                   Button(kw.INCREASE ,pygame.Rect(__raise_pos + __betButton_width + __gap,__betButton_y + (__betButton_height - 52.5)/2,63,52.5),flag=1)]

# login button
loginPageButtons = [Button(kw.SIGN_IN ,pygame.Rect((SCREEN_WIDTH-120)/2 +80,500,120,60),flag=-1),
                    Button(kw.SIGN_UP ,pygame.Rect((SCREEN_WIDTH-120)/2 -80,500,120,60),flag=-1)]