import json
import os
import keywords as kw

path = os.path.dirname(__file__).replace('code','data') + '\\player.json'

def load_players(path = path) -> list[dict]:
    '''return a list include player data [{username:...,},{...}...]'''
    with open(path,mode='r',encoding='utf-8') as fp:
        return json.load(fp)[kw.PLAYER_DATA]

def sign_in(username,password):
    """return player info after login successful,\n
       else return False"""
    for player in load_players():
        if player[kw.USERNAME] == username and player[kw.PASSWORD] == password:
            del player[kw.PASSWORD]
            return player
    return False

def sign_up(username,password,c_password):
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
        kw.TYPE: 1,
        kw.USERNAME:username,
        kw.PASSWORD:password,
        kw.CHIP: 1000
    })
    with open(path,mode='w',encoding='utf-8') as fp:
        json.dump({kw.PLAYER_DATA:content},fp,indent=4)
    return True

def get_bot():
    '''all bot info but without password'''
    botList = []
    for bot in load_players():
        del bot[kw.PASSWORD]
        if bot[kw.TYPE] == 0:
            botList.append(bot)
    return botList

def save_game(players_info:list[dict]):
    """save the player data to json"""
    with open(path,mode='w',encoding='utf-8') as fp:
        json.dump({kw.PLAYER_DATA:players_info},fp,indent=4)