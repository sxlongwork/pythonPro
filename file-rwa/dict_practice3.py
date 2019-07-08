# 编写一个Python脚本来打印一个字典，其中键是1到15之间的数字(都包括在内)，值是键的平方。

d = dict()

for key in range(1, 16):
    d[key] = key**2
print(d)

# 编写一个Python脚本，检查给定键是否已经存在于字典中
key = "name"
d = {}
for i in d.keys():
    if key == i:
        print(True)
    else:
        print(False)

# 随机生成1000个整数
# 数字范围[20,100]
# 升序输出所有不同的数字及其每个数字的重复次数