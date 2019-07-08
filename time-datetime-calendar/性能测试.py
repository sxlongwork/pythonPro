
# 计算CPU的处理时间

import time

time.clock()
sum = 0
for i in range(10000000):
    sum += i
print(time.clock())
