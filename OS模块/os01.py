'''
os:包含了操作系统的功能

'''
import os

# 获取操作系统类型， nt->windows  posix->Linux,unix,Mac
print(os.name)
# 打印操作系统详细内容，windows不支持
# print(os.uname())
# 获取操作系统中的环境变量
print(os.environ)
# 获取指定环境变量
os.environ.get('ALLUSERSPROFILE')


# 获取当前路径
print(os.curdir)    # .
# 获取当前工作目录
print(os.getcwd())
# 获取是上一次路径
print(os.pardir)    # ..

# 列出指定目录下的所有内容
# print(os.listdir("aaa"))

# 在当前路径下创建目录, 也可以写绝对路径
# os.mkdir("xx")
# 删除目录, 也可以写绝对路径
# os.rmdir("xxx")


# 获取文件属性
print(os.stat("os01.py"))
# 重命名
# os.remove("xxx", "xxxxx")
# 删除普通文件
# os.remove("xxx")

# print(os.path.getsize())


# 运行shell命令
# print(os.system("df -h"))
# data = os.popen("df -h").read()    # 要通过read()读取执行后的输出
# print(data)

# os.path
# print(os.path.abspath("file"))
print(type(os.path.join("path1", "path2")))    # 拼接path1与path2
#
# print(os.path.split("xxx"))     # 拆分路径
# print(os.path.basename("xxx"))  # 获取文件名
# print(os.path.dirname("xxx"))   # 获取文件所在的路径


# 判断是否是目录
print(os.path.isdir("path"))
# 判断文件是否存在
print(os.path.exists("aa"))
# 判断是否是文件
print(os.path.isfile("file"))
# 判断是否是链接文件
print(os.path.islink("file"))





