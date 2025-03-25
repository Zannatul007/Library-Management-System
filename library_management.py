class Book(object):
    def __init__(self, isbn, title, author, genre, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre = genre
        self.copies = copies

    def __str__(self):
        return "ISBN: {},Title: {}, Author: {},Genre: {}, Copies: {}".format(
            self.isbn, self.title, self.author, self.genre, self.copies
        )


class Member:
    def __init__(self, mid, mname, memail, mpass, role="Member"):
        self.mid = mid
        self.mname = mname
        self.meamil = memail
        self.mpass = mpass
        self.role = role
        self.borrowed_books = []

    def borrow_book(self, book: Book):
        self.borrowed_books.append(book)

    def return_book(self, book: Book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)


class Library:
    def __init__(self):
        self.books_collection = {}
        self.member_collection = {}

    def add_books(self, book):
        self.books_collection[book.isbn] = book

    def update_book(self, isbn, title=None, author=None, genre=None, copies=None):
        if isbn not in self.books_collection:
            print("Book is not found")
            return
        if genre:
            self.books_collection[isbn].genre = genre
        if author:
            self.books_collection[isbn].author = author
        if title:
            self.books_collection[isbn].title = title
        if copies:
            self.books_collection[isbn].copies = copies

    def search_book(self, search_item):
        pos = None
        for isbn, book in self.books_collection.items():
            if (
                (book.title == search_item)
                or (book.author == search_item)
                or (book.genre == search_item)
            ):
                pos = isbn
        return self.books_collection[pos]

    def delete_book(self, isbn):
        if isbn in self.books_collection:
            del self.books_collection[isbn]
        else:
            print("Book is not found")

    def borrow_books(self, mid, isbn):
        if (isbn in self.books_collection) and (mid in self.member_collection):
            book = self.books_collection[isbn]
            if book.copies > 0:
                self.member_collection[mid].borrow_book(book)
                book.copies -= 1
            else:
                print("The copies of book is not available")
        else:
            print("Book or member is not found")

    def return_books(self, mid, isbn):
        if (isbn in self.books_collection) and (mid in self.member_collection):
            book = self.books_collection[isbn]
            if book in self.member_collection[mid].borrowed_books():
                self.member_collection[mid].return_book(book)
                book.copies += 1
            else:
                print("Book is not borrowed")
        else:
            print("Book or member is not found")

    def register_member(self, member: Member):
        if member.mid in self.member_collection:
            print("User already exists")
        else:
            self.member_collection[member.mid] = member

    def verify_member(self, member: Member, name, password):
        if member.mid in self.member_collection:
            if (member.mpass == password) and (member.name == name):
                return True
            else:
                print("Incorrect name or password")

    def update_member(self, mid, email=None, name=None):
        if mid not in self.member_collection:
            print("User not found")
            return
        if email:
            self.member_collection[mid].memail = email
        if name:
            self.member_collection[mid].mname = name

    def remove_member(self, mid):
        if mid in self.member_collection:
            del self.member_collection[mid]
        else:
            print("User not found")


class Admin(Member):

    def __init__(self, mid, mname, memail, mpass):
        super().__init__(mid, mname, memail, mpass, role="Admin")
        self.books_collection = {}
        self.member_collection = {}

    def add_book(self, library: Library, book: Book):
        library.add_books(book)

    def update_book(
        self, library: Library, isbn, title=None, author=None, genre=None, copies=None
    ):
        library.update_book(isbn, title, author, genre, copies)

    def search_book(self, library: Library, search_item):
        library.search_book(search_item)

    def delete_book(self, library: Library, book: Book):
        library.delete_book(book.isbn)
