# 石头 剪刀 布
import random

player_score = 0
computer_score = 0

player_name = input('请输入玩家姓名：')
print('1.貂蝉 2.曹操 3.诸葛亮')
choice = eval(input( '请选择电脑角色：' ))

if choice==1:
    computer_name = '貂蝉'
elif choice==2:
    computer_name = '曹操'
elif choice==3:
    computer_name = '诸葛亮'
else:
    computer_name = '匿名'

print(player_name,'VS',computer_name)

while True:
    #step1:玩家出拳
    player_first = eval(input('-----请出拳：1石头 2剪刀 3布------\n'))
    if  player_first ==1:
        player_first_name = '石头'
    elif player_first ==2:
        player_first_name = '剪刀'
    elif player_first == 3:
        player_first_name = '布'
    else:
        player_first_name = '石头'
        player_first = 1

    #step2:电脑出拳
    computer_first = random.randint(1,3)   #包含3
    if computer_first == 1:
        computer_first_name = '石头'
    elif computer_first ==2:
        computer_first_name = '剪刀'
    else:
        computer_first_name = '布'
    print(player_name,'出拳:',player_first_name)
    print(computer_name,'出拳：', computer_first_name)

    if player_first == computer_first:
        print('平局')
    elif (player_first==1 and computer_first==2) or (player_first==2 and computer_first==3) or (player_first==3 and computer_first==1):
        print('玩家:',player_name,'胜')
        player_score += 1
    else:
        print('电脑:',computer_name,'胜')
        computer_score += 1

    answer = input('再来一局不?y/n')
    if answer!='y':
        break

print('----------------------------------------------')
print(player_name, player_score)
print(computer_name, computer_score)
print('----------------------------------------------')

if player_score == computer_score:
    print('总分平局')
elif player_score>computer_score:
    print(player_name,'胜利')
else:
    print(computer_name,'胜利')










