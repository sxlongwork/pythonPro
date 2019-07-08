# file w写模式

# 文件不存在会自动创建,每次执行都会覆盖原文件内容
file2 = open("file2", "w")

# 只写模式不能读，io.UnsupportedOperation: not readable
# data = file2.read()


# 1. 将文件写入缓冲区
file2.write("xianqian\n")
file2.write("i miss you dear!")

# 2. 刷新缓冲区
# 直接将内部缓冲区的数据立刻写入文件，而不是被动的等待，一直等到文件关闭（f.close()）才刷新缓冲区
# 写满缓冲区，也会自动刷新
# 遇到"\n"也会刷新缓存区
file2.flush()


# file2.truncate()  # 不删除
# file2.truncate(8) # 保留前8个字符"xianqian",之后的字符全部删除
file2.truncate(0)   # 数字为0,全部删除

# 执行close()会刷新缓冲区
file2.close()

# with 方式写文件
# with open("file2", mode="w") as f:
#     data = f.write("*********")

