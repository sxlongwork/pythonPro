import pymongo

# 连接mongodb
mon = pymongo.MongoClient("mongodb://root:123456@192.168.211.118:27017")
# print(mon)
# 查询数据
# 指定数据库
mydb = mon["devops"]
# 指定集合collection
col = mydb["goods"]
# 查询所有数据
data = col.find()
# 遍历输出所有数据
for d in col.find():
    print(type(d))
    print(d)


