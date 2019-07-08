# while 循环

# 猜数字小游戏
import random
number = random.randint(1, 100)  # 获取1~100的随机数，包括1和100

while True:
    guess_num = int(input("pls type a number(1-100):"))
    if guess_num > number:
        print("you guess big.pls guesss again.")
        continue
    elif guess_num < number:
        print("you guess small.pls guess again")
        continue
    else:
        print("success,it's {}.".format(guess_num), "you will get a prize")
        flag = input("do you want play again?(y/n):")
        if flag == "y":
            number = random.randint(1, 100)
            continue
        else:
            break
