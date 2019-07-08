# 元组

# 元组定义

tuple1 = (1, 2, )   # 使用小括号定义
print(tuple1)

tuple2 = ("2")        # 定义单个元素的列表时，元素后面一定要加上","，否则会被认为是其他类型,如int, str
print(type(tuple2))

# 元组方法
tuple3 = ("one", "two", "three", "one", )
print(tuple3.index("one"))  # index(e)，e为元素，不是下标，统计e元素在元组中第一次出现的下标
print(tuple3.count("one"))  # count(e)，e为元素，不是下标，统计e元素在元组中出现的次数

# 元组的切片
tuple4 = [1, 2, 3, 4, ]
print(tuple4[1:3])
print(tuple4[::-1])

# 元组的拼接
tuple5 = (1, 2, )
tuple6 = (3, 4, )
print(tuple5 + tuple6)

