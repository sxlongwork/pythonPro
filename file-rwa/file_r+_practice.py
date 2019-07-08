# r+ mode

f = open("httpd.conf", mode="r+")

# # f.read()
# f.readline()
# f.seek(f.tell())
# # f.seek(f.tell())
# f.write("hello world\n")

for i in range(41):
    f.readline()

f.seek(f.tell())
f.write("Listen 8080\n")


f.close()

# r+模式下,如果直接写，会从0位置处开始写，并且覆盖原位置的字符，写多少字符就覆盖多少字符,如果写入换行符，会覆盖原有的两个字符

# r+模式下，使用了read()或readline()或readlines()后再写字符，会在文件最后写入，readline()读取后，会换行写；
# read()或readlines()读取后会在同一行写






