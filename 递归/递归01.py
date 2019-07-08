'''
递归：一个函数，再内部调用自身

方式：
1.写出临界条件
2.找出这一次和上一次的关系
3.假设当前函数已经能用，调用自身计算上一次的结果，再求出本次的结果

'''

# 计算1+2+3+...+n的和
num = int(input("number:"))

def get_sum(num):
    if num > 1:
         return get_sum(num-1) + num
    else:
        return 1

print(get_sum(num))