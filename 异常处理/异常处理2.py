'''
try...except...finally
try:
    语句t
except 错误码 as e:
    语句1
except 错误码 as e:
    语句2
...
finally:
    语句n


作用：无论语句t是否有错误都会执行最后的语句n

可用于关闭一些文件流f.close()
'''

try:
    print(int("aaa"))
except NameError as e:
    print("name error")
except ValueError as e:
    print("value error")
finally:
    print("this coomand must be excute..")

print("***")