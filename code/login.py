import json
import os
import keywords as kw

path = os.path.dirname(__file__).replace('code','data') + '\\player.json'

def load_players(path:str = path) -> list[dict]:
    '''return a list include player data [{username:...,},{...}...]'''
    with open(path,mode='r',encoding='utf-8') as fp:
        return json.load(fp)[kw.PLAYER_DATA]

def sign_in(username:str,password:str):
    """return player info after login successful,\n
       else return False"""
    for player in load_players():
        # 拒绝机器人登录
        if player[kw.USERNAME] == username and player[kw.PASSWORD] == password and player[kw.TYPE]:
            del player[kw.PASSWORD]
            return player
    return False

def sign_up(username:str,password:str,c_password:str,real_player:bool = True) -> bool:
    def check_password(password:str):
        letter = False
        digit = False
        if len(password) >= 8:
            for char in password:
                if char.isalpha():
                    letter = True
                if char.isdigit():
                    digit = True
                if letter and digit:
                    break
        return letter and digit
    content = load_players()
    # username exist
    for user in content:
        if user[kw.USERNAME] == username:
            return False
    # invalid password
    if not check_password(password) or password != c_password:
        return False
    content.append({
        kw.TYPE: int(real_player),  #type 1 is real player,0 is bot
        kw.USERNAME:username,
        kw.PASSWORD:password,
        kw.CHIP: 500000
    })
    with open(path,mode='w',encoding='utf-8') as fp:
        json.dump({kw.PLAYER_DATA:content},fp,indent=4)
    return True

def get_testing_data() -> dict:
    '''testing user data(non save)'''
    return {
        kw.TYPE: 1,  #type 1 is real player,0 is bot
        kw.USERNAME:'test_username',
        kw.CHIP: 1000000
    }

def get_bot() -> list[dict]:
    '''all bot info but without password'''
    botList = []
    for bot in load_players():
        del bot[kw.PASSWORD]
        if bot[kw.TYPE] == 0:
            botList.append(bot)
    return botList

def save_game(players_info:list[dict] = []):
    """save the player data to json"""
    ori_players_info = load_players()
    for ori_player in ori_players_info:
        for player in players_info:
            if ori_player[kw.USERNAME] == player[kw.USERNAME]:
                ori_player[kw.CHIP] = player[kw.CHIP]
    with open(path,mode='w',encoding='utf-8') as fp:
        json.dump({kw.PLAYER_DATA:ori_players_info},fp,indent=4)

def calculate_ranking(ori_data:dict) -> list[list]:
    sorted_data = sorted(ori_data, key=lambda x: x[kw.CHIP], reverse=True)
    ranked_data = []
    current_rank = 0
    previous_chip = None
    for item in sorted_data:
        if previous_chip is None or item[kw.CHIP] != previous_chip:
            current_rank += 1
        ranked_data.append([current_rank,item[kw.USERNAME], item[kw.CHIP]])
        previous_chip = item[kw.CHIP]
    return ranked_data

if __name__ == '__main__':
    pass
