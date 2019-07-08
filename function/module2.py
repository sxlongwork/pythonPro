# import
# import 模块名(py文件名)
# from 模块名 import *(导入py文件的所有内容，包括变量，函数，类等)
# from 模块名 import 函数名(导入需要用到的函数)
# from 模块名 import 函数名 as 新的名称(原函数名与本地文件内的函数名重复时，可为原函数设置别名使用)

from hello import my_print, get_max as _get_max

my_print("xianqian", 23)
_get_max(3,4)


def get_max(a, b):
    if a >b:
        print("本地a")
    else:
        print("本地b")

get_max(3, 6)
_get_max(3, 4)

