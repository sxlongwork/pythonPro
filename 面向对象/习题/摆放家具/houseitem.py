class HouseItem:
    """
    家具类
    属性：名字，占地面积
    """
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return '%占地面积为%.2f' % (self.name, self.area)
