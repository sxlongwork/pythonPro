f = open("2.txt", "w+")

f.write("11111\n")
f.write("22222\n")
f.write("33333\n")

print(f.tell())

f.write("aaa")
f.seek(0)
# print(f.tell())
f.write("bbb")

f.write("ccc")

# print(f.tell())
data = f.readline()
# print(f.tell())

print("--------------")
print(data)

# print(f.tell())
# f.write("ddd")

f.close()

# help(open)
