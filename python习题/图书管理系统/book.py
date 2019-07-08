class book(object):
    def __init__(self, name, author, publish_date="", is_borrowed=0):
        self.name = name
        self.author = author
        self.publish_date = publish_date
        self.is_borrowed = is_borrowed

