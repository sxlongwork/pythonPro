# dict2 遍历字典


dict1 = {"name": "xianqian", "age": 25,"sex": "girl"}
print(type(dict1))
for i in dict1:
    print(i, dict1[i])


dict1[None] = "laotian"     # None可以作为键
dict1[None] = "laowen"      # None键也不能重复，重复时后面的还会覆盖前面的
dict1["grade"] = None       # 值可以为None
dict1["class"] = None       # 值可以重复
print(dict1)
