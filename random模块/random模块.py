# randomg模块
# 用于产生随机数
import random

# random.random()产生0~1之间的随机数
print(random.random())

# 产生a~b或b~a之间的随机数
print(random.uniform(3,1))

# 产生整数a<=number<=b
print(random.randint(1,4))

# 产生一个范围的整数a,b,步长
print(random.randrange(1, 10, 2))

# 在字符串中随机取一个字符，random.choice(sequence)
print(random.choice("abcd"))

# 在前面的字符串中随机选取n个字符，结果是列表
print(random.sample("abcdefgh", 3))

# 将list中的数据顺序随机打乱，重新洗牌，
list1 = [1, 2, 3, 4]
random.shuffle(list1)
print(list1)