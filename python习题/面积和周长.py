# 2.#计算一个12.5m*16.7m的矩形房间的面积和周长

length = float(input("pls input length(m):"))
width = float(input("pls input width(m):"))

area = length * width
c = 2 * (length + width)

print("面积：{}".format(area))
print("周长：{}".format(c))