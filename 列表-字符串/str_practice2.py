# 给出一个字符串，在程序中赋初值为一个句子，例如"he threw three free throws"，自编函数完成下面的功能：
#
# 1）求出字符列表中字符的个数（对于例句，输出为26）

def get_str_length(string):
    count = 0
    for i in string:
        count += 1
    return count


str1 = "abcabcabcddddd22d"
# length = get_str_length(str1)
# print("length = %s " % length)


# 2）计算句子中各字符出现的频数(通过字典存储);  ---学完字典再实现
def get_chars_count(string):
    chars_dict = {}
    for i in string:
        if chars_dict.keys().__contains__(i):
            chars_dict[i] = chars_dict.get(i) + 1
        else:
            chars_dict[i] = 1
    return chars_dict


# print(get_chars_count(str1))

# 3)将统计的信息存储到文件《统计.txt》中;    --- 学完文件操作再实现
# open("统计.txt")
# help(open)

f = open("统计.txt", 'w')

str1_length = get_str_length(str1)
chars_count = get_chars_count(str1)
f.write(str1+"\n")
f.write("length= %s" % (str1_length)+"\n")
f.write(str(chars_count))

f.close()
