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
        self.content = ''

    def check(self,event:pygame.event):
        self.draw()
        if self.rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
            self.border_color = (255,255,255)
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.MOUSEBUTTONDOWN or event.key == pygame.K_RETURN:
                        self.border_color = (83, 67, 67)
                        return
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            self.content = self.content[:-1]
                        else:
                            self.content += event.unicode
                self.draw()

    def draw(self):
        text = INPUT_FONT.render(self.content,True,INPUT_FONT_COLOR)
        box = pygame.Surface((self.rect.width,self.rect.height),pygame.SRCALPHA)
        pygame.draw.rect(box,self.color,box.get_rect(),0,25)
        pygame.draw.rect(box,self.border_color,box.get_rect(),8,25)
        box.blit(text,((self.rect.width-text.get_width())/2,(self.rect.height-text.get_height())/2))
        screen.blit(box,(self.rect.x,self.rect.y))
        pygame.display.flip()

loginPageInputs = [Input(USERNAME,USERNAME_BOX_RECT,(0,0,0),(83, 67, 67)),
                   Input(PASSWORD,PASSWORD_BOX_RECT,(0,0,0),(83, 67, 67))]