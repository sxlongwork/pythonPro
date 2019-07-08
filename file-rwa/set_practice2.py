# set

set1 = {"xiaowang", 26, "girl", 26}
# print(set1)
# print(type(set1))
# print(set1.__len__())

set2 = {"xianqian", 26, "girl", 1.6}

# 交集
# print(set1.intersection(set2))
# print(set2.intersection(set1))

# 并集
# print(set1.union(set2))
# print(set2.union(set1))

# 补集
# print(set1.difference(set2))
# print(set2.difference(set1))

math = ["张三", "田七", "李四", "马六"]
english = ["李四", "王五", "田七", "陈八"]
art = ["陈八", "张三", "田七", "赵九"]
music = ["李四", "田七", "马六", "赵九"]

# 同时选修数学和英语的
print(set(math).intersection(set(english)))
# 选修了英语，没有选修音乐的
print(set(english).difference(set(music)))
# 选修了数学和英语，没有选修艺术的
print(set(math).intersection(set(english)).difference(set(art)))



