import easygui as g
import sys

while 1:
    g.msgbox("hi,欢迎进入第一个界面小游戏")

    msg="请问你希望在鱼C工作室学习到什么知识呢?"

    title="小游戏互动"
    choices=["谈恋爱","编程","OOXX","琴棋书画"]

    choice=g.choicebox(msg,title,choices)


    g.msgbox("你的选择是：" + str(choice) ,"结果")

    msg="你希望重新开始小游戏吗?"

    title="亲选择"

    if g.ccbox(msg,title):
        pass
    else:
        sys.exit(0)

        
