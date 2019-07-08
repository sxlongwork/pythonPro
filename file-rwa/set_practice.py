# set practice

math = ["张三", "田七", "李四", "马六"]
english = ["李四", "王五", "田七", "陈八"]
art = ["陈八", "张三", "田七", "赵九"]
music = ["李四", "田七", "马六", "赵九"]

# 1. 求同时选修了math和music的人
print(set(math).intersection(set(music)))
# 2. 求同时选修了math,enlish和music的人
print(set(math).intersection(set(english)).intersection(set(music)))
# 3. 求同时选修了4种课程的人
print(set(math).intersection(set(english)).intersection(set(art)).intersection(set(music)))