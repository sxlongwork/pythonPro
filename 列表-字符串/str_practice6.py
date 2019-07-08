# 练习: 一个袋子里有3个红球，3个绿球，6个黄球，一次从袋子里取6个球，列出所有可能组合

count = 0
for i in range(4):
    for j in range(4):
        print("红球取{}个，绿球取{}个，黄球取{}个".format(i, j, 6-i-j))
        count += 1
print("共有{}种组合！".format(count))