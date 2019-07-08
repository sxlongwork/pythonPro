class Tool(object):
    count = 0

    def __init__(self, name):
        self.name = name

        Tool.count += 1

    @classmethod
    def show_tool_count(cls):
        print("工具数量:%d" % cls.count)

    # def show_tool_count(self):
    #     print("----")


# 创建工具对象
tool1 = Tool("斧头")

# 调用类方法
Tool.show_tool_count()
# tool1.show_tool_count()
