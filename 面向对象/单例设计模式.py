"""
内置方法__new__用来给实例分配空间，创建对象时会被自动调用
该方法必须返回所分配空间的地址引用super().__new__(cls)，否则无法执行初始化方法__init__
该方法是obkject类的静态方法

"""
class Single(object):

    # 记录实例
    instance = None

    # 记录初始化标记
    init_flag = False

    def __new__(cls, *args, **kwargs):
        # 如果instance为None,说明是第一次初始化，
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        # instance不为空，直接返回instance,不要重新分配空间

        return  cls.instance

    def __init__(self):
        if Single.init_flag:
            return
        print("初始化对象...")
        Single.init_flag = True


s1 = Single()
s2 = Single()
print(s1)
print(s2)