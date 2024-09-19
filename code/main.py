from card_game import *
from holdem import *
from login import *

game = Holdme(os.path.dirname(__file__).replace('code','data') + '\\player.json')
            #   ,handList=[['2_1','2_1'],['4_1','5_1'],['14_1','5_1'],['8_1','9_1'],['10_1','11_1']],
            #   communityCardsList=['8_1','9_1','10_1','5_1','5_1'])
game.init_player()
game.check_game()

def login():
    screen.fill(SCREEN_COLOR)
    draw_table(0)
    introduction()
    # while True:
        # input_box(USERNAME_BOX_RECT)
    interact(buttonList = loginPageButtons)

def update_game():
    screen.fill(SCREEN_COLOR)
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        draw_table()
        # draw_blind()
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
        game.holdem(interact,draw_players)
        game.check_game()
        pygame.display.flip()

if __name__ == '__main__':


    login()
    update_game()