import userinfo
import dboper
import person



# 初始化userinfo数据库，及用户表user
# dbop = dboper.DbOper()

# dbop.initdata()

# 创建用户
user1 = userinfo.User("xianqian", "woman", 23, "18711112222")
# print(user1.name, user1.sex, user1.age, user1.phonenumber)
p = person.Person()
p.register(user1)
print(user1.state)
p.login(user1)
print(user1.state)
user2 = userinfo.User("xiaoming", "man", 23, "18711112222")
p.login(user2)

