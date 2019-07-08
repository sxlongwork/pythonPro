
def get_max(a, b):
    if a > b:
        return a
    else:
        return b


def get_three_max(a, b, c):
    aa = get_max(a, b)
    bb = get_max(aa, c)
    return bb


c = get_three_max(422, 65, 10)

# print(c)

age =12


def change_age(a):
    global age
    age = a


change_age(34)
print(age)
