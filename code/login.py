import json
import os

path = os.path.dirname(__file__).replace('code','data') + '\\player.json'

def load_players(path = path) -> list:
    '''return a list include player data [{username:...,},{...}...]'''
    with open(path,mode='r',encoding='utf-8') as fp:
        return json.load(fp)['player_data']

def login(username,password):
    content = load_players()
    for user in content:
        if user['username'] == username and user['password'] == password:
            return True
    return False

def sign_up(username,password):
    content = load_players()
    # username exist
    for user in content:
        if user['username'] == username:
            return False
    # invalid password
    if not check_password(password):
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
    return letter and digit

def get_player(username):
    a = []
    for player in load_players():
        if player['username'] == username:
            # insert player to the middle seat
            playersList.insert(2,'1')
            break
        else:
            self.__playersList.append(Bot(player['username'],player['chip']))
    self.__playersList = self.__playersList[:5]

def save_game(players_info):
    """save the player data to json"""
    with open(path,mode='w',encoding='utf-8') as fp:
        json.dump({'player_data':players_info},fp,indent=4)