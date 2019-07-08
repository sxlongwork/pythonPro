# file a 追加模式

# 文件不存在会自动创建，每次执行会在文件末尾追加
file4 = open("file4", "a")

file4.write("I really miss you!\n")

file4.close()
