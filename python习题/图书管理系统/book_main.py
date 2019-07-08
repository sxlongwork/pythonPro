import book


class BookMange(object):
    books = []
    # 初始化菜单

    @staticmethod
    def menu():
        print("""欢迎来到图书管理系统
1 查询
2 增加
3 借阅
4 归还
5 退出
        """)
        while True:
            user_select = input("请输入您的选择:")
            if user_select in ("1", "2", "3", "4"):
                if user_select == "1":
                    BookMange.show_books()

                break
            elif user_select == "5":
                print("欢迎再次访问图书管理系统")
                exit()
            else:
                print("输入有误，请重新输入")

    # 查询
    @classmethod
    def show_books(cls):
        if len(cls.books) == 0:
            print("当前系统中没有任何书籍")
        else:
            print("*" * 50)
            print("书名\t\t作者\t\t发布日期\t\t借出状态")
            for data in cls.books:
                print(data.name, data.author, data.publish_date, data.is_borrowed, sep="\t\t")
            print("*"*50)


if __name__ == "__main__":
    # bookmange = BookMange()
    BookMange.menu()