import functools

print(int("1010")) # 将一个字符串转换为int型整数，默认是十进制
print(int("1010",base=2)) # base=2，表示将"1010"看成是2进制再转换

# 偏函数：将一个参数固定，形成一个新的函数
def int2(str, base = 2):
    return int(str, base)


print(int2("0111"))

# 使用functools.partial生成偏函数
int2 = functools.partial(int, base =2)

print(int2("1011"))     # int2函数就默认将参数当作二进制再转换