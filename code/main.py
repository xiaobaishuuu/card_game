from card_game import *
from holdem import *
from login import *

def login_page(login = False) -> dict:
    '''return real player info after login '''
    screen.fill(SCREEN_COLOR)
    draw_table(0)
    introduction()
    while not login:
        # recieve input
        result = interact(buttonList = loginPageButtons,inputList=loginPageInputs)
        # sign in
        if result['choice'] == SIGN_IN:
            login = sign_in(result[USERNAME],result[PASSWORD])
        # sign up
        elif result['choice'] == SIGN_UP:
            sign_up(result[USERNAME],result[PASSWORD],result[C_PASSWORD])
    return login

def holdem_page():
    screen.fill(SCREEN_COLOR)
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        draw_table()
        # draw_blind()
        draw_players(game.get_players_info('username'),game.get_players_info('chip'))
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
        player_info = login_page()
        game = Holdme(small_blind=9)
        game.init_player(get_bot(),player_info)
        game.check_game()
        holdem_page()
    except QuitGame:
        save_game(game.save_game())
        pygame.quit()
        quit()