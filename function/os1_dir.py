# os module

import os

# 查看目录与切换目录
print(os.getcwd())  # 查看当前目录，D:\pythonPro\function
os.chdir("D:\pythonPro\day01")      # 切换目录
print(os.getcwd())  # 再次查看， D:\pythonPro\变量-print
print("-"*30)

print(os.curdir)    # 打印当前路径.
print(os.pardir)    # 打印上级路径..
os.chdir(os.pardir) # 切换到上次目录
print(os.getcwd())  # 切换到上级目录后，打印当前路径
print(os.listdir(os.getcwd()))  # 打印列出当前目录的所有文件(包括目录)

