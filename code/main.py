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
        if   result['choice'] == kw.SIGN_IN:        # sign in
            login = sign_in(result[kw.USERNAME],result[kw.PASSWORD])
        elif result['choice'] == kw.SIGN_UP:        # sign up
            sign_up(result[kw.USERNAME],result[kw.PASSWORD],result[kw.C_PASSWORD])
        for input_box in loginPageInputs: input_box.content_init()
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
        draw_pot(game.pot)
        # draw_blind()
        # draw every player
        for seat in range(5): draw_players(seat,game.playersList[seat].username,game.playersList[seat].chip)
        r = game.gameRound
        if r >= 1:
            for seat in range(5):
                draw_hand(seat,game.playersList[seat].hand,game.playersList[seat].fold,(r == 1 and not game.winnerList),game.winnerList)
        draw_combo(game.get_players_info('combo'))
        # end game
        if game.winnerList:
            draw_winner(game.winnerList,game.communityCardsList)
            return True
        if r >= 2:
            draw_community(game.communityCardsList,range(0,3),r == 2)
        if r >= 3:
            draw_community(game.communityCardsList,range(3,4),r == 3)
        if r >= 4:
            draw_community(game.communityCardsList,range(4,5),r == 4)
        game.holdem(interact,
                    draw_players,
                    draw_hand,
                    draw_betting,
                    draw_consideration)
        pygame.display.flip()

def other_game_page():...

if __name__ == '__main__':
    try:
        player_info = login_page()
        for k,v in kw.CASINO_LEVEL.items():
            if player_info['chip'] > v:
                ante = round(v * 0.01)
                break
        while True:
            # game = choose_game()  選擇游戲，基於baseGame，但時間不夠不實現了
            # if game == 'holdem':
            game = Holdme(ante=ante,communityCardsList=['2_1','3_1','4_1','5_1','6_1'])
            game.init_player(get_bot(),player_info)
            if holdem_page():
                save_game(game.save_game())
    except QuitGame:
        if 'game' in locals():
            save_game(game.save_game())
        pygame.quit()
        quit()