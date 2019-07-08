# 1. 输入一行字符,统计其中有多少个单词,每两个单词之间以空格隔开。
# 如输入: This is a python program. 输出：There are 5 words in the line.

string = input("pls input a string:")

str_list = string.split(' ')
print("There are {} words in the line.".format(str_list.__len__()))


