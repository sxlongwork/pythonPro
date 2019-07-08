# while practice

# 打印100以内的偶数之和
# help(range)

# 方法一
i = 0
sum = 0
while i <= 100:
    sum += i
    i += 2
print("sum = %d" % sum)

# 方法二
i = 0
sum = 0
while i <= 100:
    if i%2 == 0:
        sum += i
    i += 1
print("sum = %d" % sum)

# 方法三
i = 0
sum = 0
while i <= 100:
    if i%2 == 1:
        i += 1
    else:
        sum += i
        i += 1
print("sum = %d" % sum)

