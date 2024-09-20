from setting import *

class Input:
    def __init__(self,
                 text:str,
                 rect:pygame.Rect,
                 color:tuple,
                 border_color:tuple
                 ) -> None:
        self.text = text
        self.rect = rect
        self.color= color
        self.border_color = border_color

    def check(self,event:pygame.event):
        try:
            pygame.draw.rect(screen,self.color,self.rect,0,25)
            pygame.draw.rect(screen,self.border_color,self.rect,8,25)
            if self.rect.collidepoint(event.pos) and pygame.MOUSEBUTTONDOWN:
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        try:
                            if not box.collidepoint(event.pos) and event.type == pygame.MOUSEBUTTONDOWN:
                                return
                        except AttributeError:
                            pass
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_BACKSPACE:
                                user_text = user_text[:-1]
                            else:
                                user_text += event.unicode
                                if not self.rect.collidepoint(event.pos) and pygame.MOUSEBUTTONDOWN:
                                    return
                    except AttributeError:
                        pass
loginPageInputs = [Input(SIGN_IN,USERNAME_BOX_RECT,(0,0,0),(83, 67, 67))]