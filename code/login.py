import json
import os

path = os.path.dirname(__file__).replace('code','data') + '\\player.json'

def load_players(path = path) -> list:
    '''return a list include player data [{username:...,},{...}...]'''
    with open(path,mode='r',encoding='utf-8') as fp:
        return json.load(fp)['player_data']

def sign_in(username,password):
    """return player info after login successful,\n
       else return False"""
    for player in load_players():
        if player['username'] == username and player['password'] == password:
            del player['password']
            return player
    return False

def sign_up(username,password,c_password):
    content = load_players()
    # username exist
    for user in content:
        if user['username'] == username:
            return False
    # invalid password
    if not check_password(password) or password != c_password:
        return False
    content.append({
        "type": 1,
        "username":username,
        "password":password,
        "chip": 1000
    })
    with open(path,mode='w',encoding='utf-8') as fp:
        json.dump({'player_data':content},fp,indent=4)
    return True

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

def get_bot():
    botList = []
    for bot in load_players():
        del bot['password']
        if bot['type'] == 0:
            botList.append(bot)
    return botList

def save_game(players_info:list[dict]):
    """save the player data to json"""
    for player in load_players():
        if player['username']
    with open(path,mode='w',encoding='utf-8') as fp:
        json.dump({'player_data':players_info},fp,indent=4)

# print(get_bot())