# 练习: 改写猜数字游戏，最多只能猜5次，5次到了没猜对就退出

import random
number = random.randint(1, 100)  # 获取1~100的随机数，包括1和100
count = 0
while count < 5:
    guess_num = int(input("pls type a number(1-100):"))
    if guess_num > number:
        print("you guess big.pls guesss again.")
    elif guess_num < number:
        print("you guess small.pls guess again")
    else:
        print("success,it's {}.".format(guess_num), "you will get a prize")
        flag = input("do you want play again?(y/n):")
        if flag == "y":
            number = random.randint(1, 100)
            count = 0
            continue
        else:
            break
    count += 1