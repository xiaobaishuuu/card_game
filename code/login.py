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
    for user in content:
        if user['username'] == username:
            return False
    content.append({
        "username":username,
        "password":password,
        "chip": 1000
    })
    with open(path,mode='w',encoding='utf-8') as fp:
        json.dump({'player_data':content},fp,indent=4)
    return True

def check_password(password):
    pass
# def save_players(self,playersList):
#     """save the player data to json"""
#     #get all player Id
#     players_dict = {player.Id: player for player in iter(playersList)}
#     for ori_player in self.__playersData:  #ori = original
#         # find and replace player data
#         if ori_player['Id'] in players_dict:
#             ori_player['chip'] = players_dict[ori_player['Id']].chip
#     with open(self.__playersDataPath,mode='w',encoding='utf-8') as fp:
#         json.dump({'player_data':self.__playersData},fp,indent=4)

# print(sign_up('Felix','00000'))