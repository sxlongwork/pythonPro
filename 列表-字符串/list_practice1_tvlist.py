# practice

import random
tvlist = [
    "戏说西游记:讲述了西游路上的三角恋.",[
        "孙悟空:悟空爱上了白骨精......",
        "唐三藏:唐僧只想取经......",
        "白骨精:她爱上了唐僧......",
        ],
    "穿越三国:王二狗打怪升级修仙史",[
        "王二狗:开局一把刀,一条狗......",
        "吕布:看我方天画鸡......",
        "貂蝉:油腻的师姐,充值998就送!",
        ],
    "金瓶梅:你懂的",[
        "西门大官人:你懂的......",
        "潘金莲:你懂的......",
        "武大郎:你懂的......",
        "武松:你懂的......",
        ],
    "大明湖畔:我编不下去了......",[
        "夏雨荷:xxxxxx",
        "乾隆:xxxxxx",
        "容么么:xxxxxx",
    ],
]

index = random.randrange(0, tvlist.__len__(), 2)

print("今日的通告:")
print(tvlist[index])
print("可接的角色有:")
for i, j in enumerate(tvlist[index+1]):
    print("\t"+str(i+1), j)
select = int(input("请问你要接哪个角色(请输入数字):"))
print("恭喜你,你接了{}这个角色,相信我们的合作会让这部剧大火".format(tvlist[index+1][select-1].split(":")[0]))

