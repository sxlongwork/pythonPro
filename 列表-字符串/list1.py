# list 定义

numbers = ["one", "two", "three", "four", "five"]
# print(type(numbers))
# print(numbers)
# 列表遍历
# for i in numbers:
#     print(i, end=" ")
# print()
#
# for i, j in enumerate(numbers):
#     print(i, j)

# 列表切片
# print(numbers[1:2])
# print(numbers[:3])
# print(numbers[:])
# print(numbers[::2])
# print(numbers[1::-1])
# print(numbers[::-2])
# 列表倒序
print(numbers[::-1])
numbers.sort()
numbers.reverse()
print(numbers)

if 'five' in numbers:
    print('true')

