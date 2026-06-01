class book:
    def __init__(self, title, author, no_of_pages):
        self.title=title
        self.author=author
        self.no_of_pages=no_of_pages

    def book_details(self):
        print("The book is ", self.title, "by", self.author, "having", self.no_of_pages, "pages.")

    def book_size(self):
        if self.no_of_pages>300:
            print("The book is long.")
        else:
            print("The book is short.")

b1=book("sherlock holmes", "aurthor conan doyle", 200)
b1.book_details()
b1.book_size()
