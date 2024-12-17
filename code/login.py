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
        # 拒绝机器人登录
        if player[kw.USERNAME] == username and player[kw.PASSWORD] == password and player[kw.TYPE]:
            del player[kw.PASSWORD]
            return player
    return False

def sign_up(username,password,c_password,real_player:bool = True):
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

def get_bot():
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

if __name__ == '__main__':
    print(load_players())

    # 原始列表
    data = [
        {'type': 0, 'username': 'Peter', 'password': '832jce83912deddwa', 'chip': 600000},
        {'type': 0, 'username': 'Amy', 'password': '832jce83912deddwa', 'chip': 300000},
        {'type': 0, 'username': 'Tom', 'password': '832jce83912deddwa', 'chip': 500000},
        {'type': 0, 'username': 'John', 'password': '832jce83912deddwa', 'chip': 500000},
        {'type': 0, 'username': 'Alex', 'password': '832jce83912deddwa', 'chip': 500000},
        {'type': 0, 'username': 'Sam', 'password': '832jce83912deddwa', 'chip': 500000},
        {'type': 1, 'username': 'rex', 'password': '1234abcd', 'chip': 500000}
    ]

    # 按 chip 降序排列
    sorted_data = sorted(data, key=lambda x: x['chip'], reverse=True)



    # 添加名次（允許名次共享，後續名次連續）
    ranked_data = []
    current_rank = 1
    previous_chip = None
    shared_rank_count = 0  # 記錄共享排名的用戶數量

    for item in sorted_data:
        # 如果籌碼不同，更新名次
        if previous_chip is None or item['chip'] != previous_chip:
            current_rank += shared_rank_count  # 更新名次為當前名次加上共享排名的數量
            shared_rank_count = 1  # 重置共享排名計數
        else:
            shared_rank_count += 1  # 如果籌碼相同，增加共享排名的用戶數量

        # 添加到結果
        ranked_data.append([current_rank, item['username'], item['chip']])
        previous_chip = item['chip']  # 記錄當前籌碼

    # 打印結果
    print(ranked_data)