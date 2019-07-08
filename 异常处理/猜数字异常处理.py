# 猜数字加入异常处理
import random


random_num = random.randint(1,100)
while True:
    try:
        guess_num = int(input("pls input a number(1~100):"))
    except ValueError as e:
        print("you must input a number,can not be other chracters.")
        continue
    else:
        pass

    if guess_num > random_num:
        print("too big.")
        continue
    elif guess_num < random_num:
        print("too small.")
        continue
    else:
        print("sucess")
        break
print("******")
