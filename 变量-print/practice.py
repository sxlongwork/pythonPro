# practice1 in 2019 04 22

name = input("\033[31;1;31m what is your name:\033[0m")
sex = input("\033[31;1;32m what is your sex:\033[0m")
job = input("\033[31;1;33m what is your job:\033[0m")
phone_number = input("\033[31;1;34m what is your phone number:\033[0m")

# print("\033[31;1;35m ---------- information of %s ----------\033[0m" % name)
# print("\033[31;1;35m name: %s\033[0m" % name)
# print("\033[31;1;35m sex: %s\033[0m" % sex)
# print("\033[31;1;35m job: %s\033[0m" % job)
# print("\033[31;1;35m phonenum: %s\033[0m" % phone_number)

print('''
\033[31;1;35m ---------- information of {0} ----------\033[0m
\033[31;1;35m name: {0}\033[0m
\033[31;1;35m sex: {1}\033[0m
\033[31;1;35m job: {2}\033[0m
\033[31;1;35m phonenum: {3}\033[0m
'''.format(name, sex, job, phone_number))

# 通过关键字参数
# print('{name},{age}'.format(age=18, name='chuhao'))
