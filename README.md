
# 运行
  1. 解释器(interpreter)版本至少为 python 3.10
  2. 安装依赖 cmd内: pip install pygame（已添加至环境变量） 或 python -m pip install pygame(未添加至环境变量)
  3. 运行 main.py (.\card_game\code\main.py)

# 结构？？？ (不是最新)

                  player.json       keyword.py
    setting.py          |               |
        |            login.py       player.py
    button.py            |_____________|
        |                       |
     card_game.py             holdem.py
        |_______________________|
                    |
                  main.py


# pygame 与 Holdem 模块的交互
  1.holdem 中的玩家座位，即起始顺序，与 pygame 中绘画玩家列表里的索引(index)一致
  2.使用图形视窗 或 文本界面(未实现)时，holdem()接收 pygame 或 命令行打印 的相关函数，于 Holdem 模块内进行操作，可以打印数据

# 檢驗手牌强度
  https://suffe.cool/poker/evaluator.html
  https://github.com/ihendley/treys
  use lookup table (LUT)

  prime: 2 3 5 7 11 13 17 19 23 29 31 37 41
  rank : 2 3 4 5 6  7  8  9  10  J Q  K  A

  xxxAKQJT 98765432 CDHSrrrr xxPPPPPP
  00001000 00000000 01001011 00100101    King of Diamonds
  00000000 00001000 00010011 00000111    Five of Spades
  00000010 00000000 10001001 00011101    Jack of Clubs

# taxas 机器人算法(废弃)
  1.每一真实回合(记 A)，以 Monte Carlo 算法随机(100或以上)局，每一局(记 B)的完整的德州扑克中，(B)的每回合引用(A)的已知牌面，其他按未知牌面随机分发，最终得出(A)的获胜概率
  2.(B) 中机器人的评估方法为手牌组合与最高牌面
  3.主机器人(记 X)，进行模拟时为(保守型下注)，即 call 和 check ,其他机器人以手牌强度进行正态分布式随机下注额度，分为几个阶段，例如////////
