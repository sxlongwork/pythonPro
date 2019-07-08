# if 条件简化
import random

# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
# x = (1,)
# # if x:
# #     print("True")
# # else:
# #     print("False")

# a = random.randint(1, 3)   # random.randint(a, b) 随机产生[a, b]范围的数字，包含a和b
# print(a)

usernum = int(input("请出拳(1-剪刀,2-石头,3-布)："))

computernum = random.randint(1, 3)
print("用户出拳为%d,电脑出拳为%d" % (usernum, computernum))

# 判断胜负
# 胜利
if (usernum == 1 and computernum == 3) \
        or (usernum == 2 and computernum == 1) \
        or (usernum == 3 and computernum == 2):
    print("哈哈，电脑弱爆了")
elif usernum == computernum:
    print("平局")
else:
    print("不要走，决战到天亮")


