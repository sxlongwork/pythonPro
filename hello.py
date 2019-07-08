"""
hello module
"""

def my_print(name, age):
    print("{} is {} years old.".format(name, age))


def get_max(a, b):
    if a > b:
        return a
    else:
        return b


# if __name__ == "__main__":
#     print("main function")
# else:
#     print("module")
