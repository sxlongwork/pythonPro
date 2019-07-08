# file r 只读模式

# 文件不存在会出错
file1 = open("file1", "r")

# 方法一
# data = file1.readlines()
# for i in data:
#         print(i.strip())

# 方法二
# for i, j in enumerate(file1.readlines()):

#     print(i+1, j.strip())
# 方法三
for i, j in enumerate(file1):
    print(i+1, j.strip())

file1.close()