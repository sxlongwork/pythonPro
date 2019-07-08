
f = None
try:
    f = open("1.txt", mode="r")
    data = f.read()
except FileNotFoundError as e:
    print("没有1.txt这个文件")
    exit(-1)
finally:
    if f:
        f.close()

print(data)



