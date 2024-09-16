from card_game import *
from holdem import *
from login import *

game = Holdme(os.path.dirname(__file__).replace('code','data') + '\\player.json')
            #   ,handList=[['2_1','2_1'],['4_1','5_1'],['6_1','7_1'],['8_1','9_1'],['10_1','11_1']],
            #   communityCardsList=['12_1','13_1','14_1','2_2','4_1'])
game.init_player()
game.check_game()

def login():
    login_page()
    pygame.display.flip()



def update_game():
    screen.fill(SCREEN_COLOR)
    draw_table()
    draw_players(game.get_players_info('name'),game.get_players_info('chip'))
    r = game.gameRound
    if r >= 1:
        draw_hand(game.handList,r,game.get_players_info('fold'))
    draw_reminder(game.get_players_info('combo'))
    if r >= 2:
        draw_community(game.communityCardsList,r,range(3),2)
    if r >= 3:
        draw_community(game.communityCardsList,r,range(3,4),3)
    if r >= 4:
        draw_community(game.communityCardsList,r,range(4,5),4)
    game.holdem(check_button,draw_players)
    game.check_game()
    pygame.display.flip()

if __name__ == '__main__':
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        login()
        # update_game()