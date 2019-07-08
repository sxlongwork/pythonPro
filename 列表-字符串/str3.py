# str 的下标，遍历字符串中的每一个字符

for i in "abcde":
    print(i, end="")

print()
print(enumerate("abcde"))
for i, j in enumerate("abcde"):
    print(i, j)     # 打印：下标i 字符j

print("="*30)
name ="xianqian"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print("="*30)
for i in name:
    print(i, end="#")
print()

# enumerate可以让下标和字符对应起来
print("="*30)
for i, j in enumerate(name):
    print(i+1, j)

str1 = "abcdefg"
for i, j in enumerate(str1):
    if i >= 1 and i <= 5:
        print(j, end="")