import os
from collections import Iterable


# 查看文件状态
print(os.stat("os1_dir.py"))    # 查看文件状态信息
# if isinstance(os.stat("os1_dir.py"), Iterable):     #判断os.stat()返回值是否可迭代，如果可以则迭代输出
#     for i in os.stat("os1_dir.py"):
#         print(i)
print(os.stat("os1_dir.py")[6])     # 文件大小, 单位是字节
print(os.stat("os1_dir.py")[-4])    # 也是文件大小
print(os.stat("os1_dir.py").st_size)    # 也是文件大小
print(os.path.getsize(__file__))    # __file__代表程序文件本身
print(os.path.getsize("os1_dir.py"))    # 获取任意路径的文件的大小

