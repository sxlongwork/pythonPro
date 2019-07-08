"""
定义一个游戏Game类
属性：
    类属性，记录历史最高分，top_score
    实例属性，游戏者的名字，player_name
方法：
    静态方法，显示帮助信息，show_help
    类方法，显示历史最高分，show_top_score
    实例方法，开始游戏，start_game
"""
class Game(object):

    top_score = 0

    def __init__(self, name):
        self.player_name = name

    @staticmethod
    def show_help():
        print("游戏帮助信息......")

    @classmethod
    def show_top_score(cls):
        print("历史最高分:%d" % cls.top_score)

    def start_game(self):
        print("%s开始游戏..." % self.player_name)

# 查看游戏帮助信息
Game.show_help()

# 查看历史最高分
Game.show_top_score()

# 创建对象，开始游戏
xiaoming = Game("小明")
xiaoming.start_game()

"""
总结如何选择使用哪种方法
1.只需要访问实例属性时，可以定义为实例方法
    在实例方法内部，可以通过类名.类属性名的方法访问类属性
2.只要访问类属性时，可以定义为类方法
3.不需要访问类属性，也不需要访问实例属性时，可以定义为静态方法

既要访问实例属性，也要访问类属性时，定义为实例方法
"""

