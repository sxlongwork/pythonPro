# str的切片，倒序

str1 = "abcdefg"
# 切片
print(str1[2:5])        # cde
print(str1[0:2])        # ab
print(str1[0:-1])       # abcdef
print(str1[2:-2])       # cde
print(str1[:])          # abcdefg
print(str1[:3])         # abc
print(str1[3:])         # defg
print(str1[1:5:2])      # bd
print(str1[:3:-1])      # gfe
print(str1[::-2])       # geca

print("================")
# 倒序
str2 = "123456789"
print(str2[::-1])   # 987654321










