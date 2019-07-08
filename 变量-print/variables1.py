# variables  了解变量

import keyword
print(keyword.kwlist)
keyWord = input("pls input a string:")
flag = keyword.iskeyword(keyWord)
if flag:
    print("true")
else :
    print("false")

