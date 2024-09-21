from setting import *

class Input:
    """draw a input box in a Surface"""

    def __init__(self,
                 text:str,
                 rect:pygame.Rect,
                 color:tuple,
                 border_color:tuple,
                 active_color:tuple = (0,0,0,0),
                 active_border_color:tuple = (0,0,0,0)
                 ) -> None:
        self.text = text
        self.rect = rect
        self.color= color
        self.border_color = border_color
        self.active_color = active_color
        self.active_border_color = active_border_color
        self.content = ''

    def check(self,event:pygame.event):
        # click the input box
        if self.rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
            self.border_color,self.active_border_color = self.active_border_color,self.border_color
            self.color,self.active_color = self.active_color,self.color
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    # quit input box,enter and click again
                    elif event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.KEYDOWN and event.key in (pygame.K_RETURN, pygame.K_KP_ENTER)):
                        self.border_color,self.active_border_color = self.active_border_color,self.border_color
                        self.color,self.active_color = self.active_color,self.color
                        return None
                    # typing
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_TAB:
                            pass
                        elif event.key == pygame.K_BACKSPACE:
                            self.content = self.content[:-1]
                        else:
                            # text limitation is 20
                            if len(self.content) < 20:
                                self.content += event.unicode
                self.draw()

    def draw(self):
        # reminder
        if len(self.content) == 0:
            text = INPUT_FONT.render(self.text,True,INPUT_FONT_COLOR)
        else:
            text = INPUT_FONT.render(self.content,True,INPUT_FONT_COLOR)
        # render text and input box
        box = pygame.Surface((self.rect.width,self.rect.height),pygame.SRCALPHA)
        pygame.draw.rect(box,self.color,box.get_rect(),0,25)
        box.blit(text,((self.rect.width-text.get_width())/2,(self.rect.height-text.get_height())/2))
        pygame.draw.rect(box,self.border_color,box.get_rect(),6,25)
        screen.blit(box,(self.rect.x,self.rect.y))
        pygame.display.flip()

loginPageInputs = [Input(USERNAME,USERNAME_BOX_RECT,TABLE_COLOR,REMINDER_BG_COLOR,REMINDER_BG_COLOR,(244, 244, 244)),
                   Input(PASSWORD,PASSWORD_BOX_RECT,REMINDER_BG_COLOR,REMINDER_BG_COLOR,TABLE_COLOR,(244, 244, 244)),
                   Input(C_PASSWORD,C_PASSWORD_BOX_RECT,REMINDER_BG_COLOR,REMINDER_BG_COLOR,TABLE_COLOR,(244, 244, 244))]