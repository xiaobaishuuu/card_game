from rendering import *
from holdem import *
from login import *

def login_page(login = False) -> dict:
    '''return real player info after login '''
    # non login
    if login: return get_testing_data()
    # login
    invalid = kw.C_PASSWORD
    attempts = 0
    temp_text = ''
    reminder_text = kw.SIGN_IN_INFO
    while not login:
        attempts += 1
        screen.fill(SCREEN_COLOR)
        draw_ranking(calculate_ranking(load_players()))
        draw_table(0)
        draw_introduction(attempts == 1)
        reminder = render_reminder(reminder_text,LOGIN_REMINDER_BG_COLOR,20)
        screen.blit(reminder,((SCREEN_WIDTH-reminder.get_width())/2,SCREEN_HEIGHT*250/SCREEN_HEIGHT))
        # recieve input
        result = interact(buttonList = loginPageButtons,inputList=loginPageInputs,invalidList=[invalid])
        # sign in
        if result['choice'] == kw.SIGN_IN:  # sign in
            reminder_text = kw.SIGN_IN_INFO
            if invalid == '':               # no sign in when Sign up
                invalid = kw.C_PASSWORD
                continue                    # skip to login
            login = sign_in(result[kw.USERNAME],result[kw.PASSWORD])
            temp_text = kw.SIGN_IN_SUCCESSE if login else kw.SIGN_IN_FAIL
            if invalid:
                draw_temp_reminder(temp_text,[SCREEN_WIDTH/2,(SCREEN_HEIGHT*350/SCREEN_HEIGHT)])
        # sign up
        elif result['choice'] == kw.SIGN_UP:# sign up
            reminder_text = kw.SIGN_UP_INFO
            temp_text = kw.SIGN_UP_SUCCESSE if sign_up(result[kw.USERNAME],result[kw.PASSWORD],result[kw.C_PASSWORD]) else kw.SIGN_UP_FAIL
            if not invalid:
                draw_temp_reminder(temp_text,[SCREEN_WIDTH/2,(SCREEN_HEIGHT*350/SCREEN_HEIGHT)])
            invalid = ''
        for input_box in loginPageInputs: input_box.content_init()
    return login

def holdem_page(game:Holdme):
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
        if r >= 2:
            draw_community(game.communityCardsList,range(0,3),r == 2 and not game.winnerList)
        if r >= 3:
            draw_community(game.communityCardsList,range(3,4),r == 3 and not game.winnerList)
        if r >= 4:
            draw_community(game.communityCardsList,range(4,5),r == 4 and not game.winnerList)
        if game.winnerList:
            draw_winner(game.winnerList)
            return True
        game.game_loop(interact,
                    draw_players,
                    draw_hand,
                    draw_betting,
                    draw_consideration)

def other_game_page():...

def main():
    try:
        player_info = login_page(login=False)  # login = true: non login
        samll_blind = 0
        while True:
            # game = choose_game()
            # if game == 'holdem':
            game = Holdme(small_blind=samll_blind)
            game.init_player(get_bot(),player_info)
            if holdem_page(game):
                player_info = game.save_game()[2]
                save_game(game.save_game())
            samll_blind += 1
    except QuitGame:
        if 'game' in locals():
            save_game(game.save_game())
        pygame.quit()
        quit()
    except Exception:
        main()

if __name__ == '__main__':
    # from pycallgraph import PyCallGraph
    # from pycallgraph.output import GraphvizOutput
    # with PyCallGraph(output=GraphvizOutput()):
    main()