# 运行
  1. 解释器(interpreter)版本至少为 python 3.10
  2. 安装依赖 cmd内: pip install pygame（已添加至环境变量） 或 python -m pip install pygame(未添加至环境变量)
  3. 运行 main.py (.\card_game\code\main.pyw)

# pygame 与 Holdem 模块的交互
  1.holdem 中的玩家座位，即起始顺序，与 pygame 中绘画玩家列表里的索引(index)一致
  2.使用图形视窗 或 文本界面(未实现)时，holdem_page()接收 pygame 或 命令行打印 的相关函数，于 Holdem 模块内进行操作，可以打印数据

# 檢驗手牌强度
  https://suffe.cool/poker/evaluator.html
  https://github.com/ihendley/treys