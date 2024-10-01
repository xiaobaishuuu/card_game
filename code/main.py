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
    game.check_game()
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
        if r >= 5:
            draw_winner(game.winnerList,game.communityCardsList)
            return True
        game.holdem(interact,draw_players)
        pygame.display.flip()

def other_game_page():...

if __name__ == '__main__':
    try:
        player_info = login_page()
        while True:
            # game = choose_game()  選擇游戲，基於baseGame，但時間不夠不實現了
            # game = 'holdem'
            # if game == 'holdem':
            game = Holdme()
            game.init_player(get_bot(),player_info)
            if holdem_page():
                save_game(game.save_game())
    except QuitGame:
        if 'game' in locals():
            save_game(game.save_game())
        pygame.quit()
        quit()