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
                    pass
        except AttributeError:
            pass
loginPageInputs = [Input(SIGN_IN,USERNAME_BOX_RECT,(0,0,0),(83, 67, 67))]