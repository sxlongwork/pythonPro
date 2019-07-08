# dict的定义
# 存储键值对， 键是唯一不可变的，值可以变，后面的覆盖前面的

dict1 ={
    "name": "xiaoming",
    "age": 19,
    "sex": "man"
}
print("字典类型和长度".center(30, "="))
print(len(dict1))
print(type(dict1))

# dict的常见操作
# 添加成员，直接赋值新的成员
print("添加成员".center(30, "="))
dict1["phonenumber"] = "1234567890"
print(dict1)

# 删除成员
print("删除成员".center(30, "="))
del dict1["phonenumber"]
print(dict1)
dict1.pop("sex")
print(dict1)

# 查询成员
# 通过键找值
print("查询成员".center(30, "="))
value = dict1.get("name")
print(value)
list1 = dict1.keys()
list2 = dict1.values()
print(list1)
print(list2)

# 修改
print("修改成员".center(30, "="))
dict1["name"] = "xianowang"
print(dict1)



