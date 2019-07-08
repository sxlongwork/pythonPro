# 打印出所有value为2的key

dict1 = {
'张三': 2,
'田七': 4,
'李四': 3,
'马六': 2,
'王五': 1,
'陈八': 2,
'赵九': 2,
}

for i in dict1:
    if dict1[i] == 2:
        print(i)

for i in dict1.items():
    if i[1] ==2:
        print(i[0])
