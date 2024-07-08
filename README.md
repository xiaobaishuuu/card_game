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
  2.使用图形视窗(GUI) 或 文本界面(TUI)时，holdem()接收 pygame 或 命令行打印 的相关函数，于 Holdem 模块内进行操作，因为没个玩家下注后将更新并打印数据，否则将全部玩家下注和才打印数据

# taxas 机器人算法
  1.每一真实回合(记 A)，以 Monte Carlo 算法随机(100或以上)局，每一局(记 B)的完整的德州扑克中，(B)的每回合引用(A)的已知牌面，其他按未知牌面随机分发，最终得出(A)的获胜概率
  2.(B) 中机器人的评估方法为手牌组合与最高牌面
  3.主机器人(记 X)，进行模拟时为(保守型下注)，即 call 和 check ,其他机器人以手牌强度进行正态分布式随机下注额度，分为几个阶段，例如(差，中，好，极)，
    下注范围分别为自己筹码的 (0-24.5)% (25-49.5)% (50-74.5)% (75-100)%