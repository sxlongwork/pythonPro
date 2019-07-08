# 把九九乘法表写进文件

file3 = open("九九乘法表", "w")
for i in range(1, 10):
    for j in range(1, i+1):
        file3.write("{}*{}={}\t".format(j, i, i*j))
    file3.write("\n")
file3.close()
