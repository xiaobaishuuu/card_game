from card_game import *
from holdem import *
from login import *

game = Holdme(load_players(path))
            #   ,handList=[['2_1','2_1'],['4_1','5_1'],['14_1','5_1'],['8_1','9_1'],['10_1','11_1']],
            #   communityCardsList=['8_1','9_1','10_1','5_1','5_1'])
game.check_game()

def login_page() -> str:
    screen.fill(SCREEN_COLOR)
    draw_table(0)
    introduction()
    while True:
        # recieve input
        result = interact(buttonList = loginPageButtons,inputList=loginPageInputs)
        # login
        if result['choice'] == SIGN_IN and login(result[USERNAME],result[PASSWORD]):
            return result[USERNAME]
        # sign up
        elif result['choice'] == SIGN_UP and result[PASSWORD] == result[C_PASSWORD]:
            sign_up(result[USERNAME],result[PASSWORD])

def game_page():
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
    try:
        username = login_page()
        game.init_player(username)
        game_page()
    except QuitGame:
        save_game(game.update_players_info())
        pygame.quit()
        quit()