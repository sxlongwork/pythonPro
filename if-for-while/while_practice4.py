# while 循环求1000以内的质数

i = 2
while i < 1000:
    j = 2
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(i, end=" ")
    i += 1

