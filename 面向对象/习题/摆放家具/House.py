import houseitem

class House:
    def __init__(self, housetype, area):
        self.housetype = housetype
        self.area = area
        self.free_area = area
        self.houseitemlist = []

    def add_item(self, houseitem):
        if self.free_area < houseitem.area:
            print("不能添加家具了，房子没有剩余空间了")
        else:
            self.houseitemlist.append(houseitem.name)
            self.free_area -= houseitem.area

    def __str__(self):
        return '户型:%s\t总面积:%.2f\t剩余面积:%.2f\t家具列表:%s' \
               % (self.housetype, self.area,
                  self.free_area, self.houseitemlist)


bed = houseitem.HouseItem('席梦思', 3.5)
chest = houseitem.HouseItem('衣柜', 2.0)
table = houseitem.HouseItem('餐桌', 1.5)

house = House('一室一厅', 30)
house.add_item(bed)
house.add_item(chest)
house.add_item(table)

print(house)

