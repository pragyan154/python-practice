class Book:
    def __init__(self, title, pages, author , price:int):
        self.title=title 
        self.pages=pages 
        self.author=author 
        self.price= price

    def display(self):
        print(" Title is %  pages % In price isn" , (self.title, self.pages, self.price))

    def __str__(self)-> str:
        return " Title is %s \n pages %d \n price is %d\n" %(self.title, self.pages, self.price)

    def __eq__(self, value):
        if not isinstance(value,Book):
            raise TypeError (f"(value? is not the instance of Book") 
        else:
            return self.title == value.title and self.author == value.author
    # return the title
    def gettitle(self):
        return self.title
    # set undate the value
    def setTitle(self, newTitle):
        self.title= newTitle
if __name__ =="__main__":   
    b1 = Book("Title1", 99, "jijdiqdj" , 10)
    b2 = Book("Title", 199, "jijdiqdj", 10)
    if b1 == b2:
        print("Same book")
    print(b1)
    b1.setTitle("ienoinsdaiodoi")
    print(b1)