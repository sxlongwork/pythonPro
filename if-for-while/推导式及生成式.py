# 推导式
# 列表推导式
# 格式：[变量 for 变量 in 可迭代对象]

# 创建一个包含0~9元素的列表，使用常见创建方式
# list1 = []
# for i in range(10):
#     list1.append(i)
# print(list1)

# 使用列表推导式
# list2 = [x for x in range(10)]
# print(list2)
#
# list3 = [x for x in range(10)if x % 2 == 0]     # 借助if判断
# print(list3)
#
# list4 = [x*x for x in range(5)]         # x*x 为元素
# print(list4)
#
# list5 = [i+j for i in range(5) for j in range(5)]   # for双循环，也可以使用三循环
# print(list5)


# 字典推导式
dict1 = {k:v for k, v in {"name": "xiaoming", "age": 20}.items()}
print(dict1)

# 元组生成式
tuple1 = (x for x in range(10))
print(tuple1)       # <generator object <genexpr> at 0x000001552182FF10>，不能直接使用
for i in tuple1:
    print(i, end=" ")


# 当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型
# 方法是通过collections模块的Iterable类型判断
from collections import Iterable
print(isinstance('abc', Iterable)) # str是否可迭代


