# dict
# 字典，无序，不能通过下标访问元素，存储键值对

dict1 = {
    "name": "xiaoxian",
    "sex": "gril",
    "age": 26
}
# print(dict1)
# print(type(dict1))
# print(len(dict1))

# 添加元素到字典
dict1["phonenum"] = 1234567890
# dict1[{1:2, 2:3}] = "list"
# print(dict1)

# 修改字典元素
dict1["age"] = 20

# 从字典中删除元素
dict1.pop("sex")
# dict1.clear()     # 清空字典，dict1 = {}
# del dict1         # 删除字典，dict1不存在了

# 查询值
# print(dict1["name"])
#
# print(dict1)
# for i in dict1.keys():
#     print(i)
# print(dict1)

# dic practice
dict1 = {
    '张三': 2,
    '田七': 4,
    '李四': 3,
    '马六': 2,
    '王五': 1,
    '陈八': 2,
    '赵九': 2,
}
# print(dict1)
# 打印出所有value为2的key

# for item in dict1.items():
#     if item[1] == 2:
#         print(item[0])
# print(dict1[:3])      # 字典不是序列，不能切片

# 小结:
# 字典是否属于序列?
'''
字典不是序列,不能通过下标遍历，不能切片，拼接等
'''
# 字典能否切片?
'''
字典不能切片
'''
# "我要打印字典的第2个到第5个键值对"，这种说法是否正确?
'''
不正确,字典是无序的，
'''
# 字典是属于可变数据类型还是不可变数据类型?
'''
字典是可变数据类型，可以增删改查元素
'''
# "字典里面可以嵌套字典，也可以嵌套列表或元组等其它数据类型"，这种说法是否正确?
'''
正确,但是字典的键是不可变数据类型，不能添加类型为list,tuple，dict等可变数据类型的键;值可以为任何类型
'''


dict1 = {"name": "xiaoming", "age": 20, "sex": "man"}
# print(dict1.keys())     # .keys()获取所有的键
# for key in dict1.keys():
#     print(key)

# print(dict1.values())     # .values()获取所有的值
# for value in dict1.values():
#     print(value)

# print(dict1.items())        # .items()获取所有的键值对
# for i in dict1.items():
#     print(i[0], i[1])

