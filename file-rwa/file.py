# file1 operation

# python文件的操作就三个步骤：
# 1. 先open打开一个要操作的文件
# 2. 操作此文件(读，写，追加等)
# 3. close关闭此文件

file1 = open("file1", "r")

data1 = file1.read()
file1.seek(0)
data2 = file1.readline()
file1.seek(0)
data3 = file1.readlines()

file1.close()

print("data1".center(50, "*"))
print(data1)
print("data2".center(50, "*"))
print(data2)
print("data3".center(50, "*"))
print(data3)
