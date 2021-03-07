#石头，剪刀，布小游戏
import random
game = ['剪刀','石头','布']
win = [
    ['石头','剪刀'],
    ['剪刀','布'],
    ['布','石头']
]
while 1:
    your_choice = input('输入‘结束’可以结束游戏噢，你的选择是(石头，剪刀，布):')
    if your_choice == '结束':
        break
    com_choice = game[random.randint(0,2)]
    if [your_choice,com_choice] in win:
        print('你出了{0},电脑出了{1},恭喜你获胜了！！'.format(your_choice,com_choice))
    elif your_choice == com_choice :
        print('你出了%s,电脑出了%s,平局啦，再试一次吧。' % (your_choice,com_choice))
    else:
        print('你出了{yours},电脑出了{coms},你输了，好可惜啊，再试试呗。'.format(coms=com_choice,yours=your_choice))

#三个骰子猜大小
'''
import random
condition = [1,2,3,4,5,6]

while 1:
    sum = 0
    choice = str(input('输入‘结束’可以结束游戏噢，你的选择是(大，小)：'))
    for i in range(3):
        sum += random.choice(condition)
    if choice == '结束':
        break
    elif choice == '大' and sum >= 12:
        print('骰子的点数为{},恭喜你,猜对了！'.format(sum))
    elif choice == '小' and sum < 12:
        print('骰子的点数为{},恭喜你,猜对了！'.format(sum))
    else:
        print('骰子的点数为{},猜错了噢，再试一次吧'.format(sum))
'''
