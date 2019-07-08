# 练习: 打印1-1000的质数（只能被1和自己整除的数)

count = 0
for i in range(1, 1001):
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(i, end=" ")