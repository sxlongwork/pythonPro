
# 要注意文件本身自带的编解码和写入读出的手动编解码是两回事
with open("1.txt",mode="wb") as f1:
    str1 = "xianqian嘿嘿"
    f1.write(str1.encode("utf-8"))


with open("1.txt", mode="rb") as f2:
    data = f2.read()
    # data = f2.read().decode("utf-8")
print(data)
