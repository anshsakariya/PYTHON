class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []
    def addBook(self,book):
        self.books.append(book)
        self.noBooks = len(self.books)
    def showInfo(self):
        print(f"The library has {self.noBooks} books.the boooks are ")
        for book in self.books:
           print(book)

l1=Library()
l1.addBook("harry potter1")
l1.addBook("harry potter2")
l1.addBook("harry potter3")
l1.addBook("harry potter4")
l1.showInfo()