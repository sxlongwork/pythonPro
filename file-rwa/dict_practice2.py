# dict practice2

city = {
    "北京": {
    "东城": "景点",
    "朝阳": "娱乐",
    "海淀": "大学",
    },
    "深圳": {
    "罗湖": "老城区",
    "南山": "IT男聚集",
    "福田": "华强北",
    },
    "上海": {
    "黄埔": "xxxx",
    "徐汇": "xxxx",
    "静安": "xxxx",
    },
}
# 1. 打印北京东城区的说明（也就是打印出"景点")
print(city["北京"]["东城"])
# 2. 修改北京东城区的说明，改为"故宫在这"
city["北京"]["东城"] = "故宫在这"
# 3. 增加北京昌平区及其说明
city["北京"]["昌平"] = "我们在这"
# 4. 修改北京海淀区的说明，将"大学"改为"清华","北大","北邮"三个学校的列表
city["北京"]["海淀"] = ["清华", "北大", "北邮"]
# 5. 在大学列表里再加一个"北影"
city["北京"]["海淀"].append("北影")
# 6. 循环打印出北京的区名,并在前面显示序号(以1开始)
for i, j in enumerate(city["北京"]):
    print(i+1, j)
# 7. 循环打印出北京海淀区的大学,并在前面显示序号(以1开始)
for i, j in enumerate(city["北京"]["海淀"]):
    print(i+1, j)
