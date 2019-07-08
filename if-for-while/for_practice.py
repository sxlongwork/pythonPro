# 请利用循环依次对list中的每个名字打印出Hello, xxx!：
L = ['Bart', 'Lisa', 'Adam']

for i in L:
    print("Hello, %s!" % i)

i = 0
while i < len(L):
    print("Hello, %s!" % L[i])
    i += 1

