class Book:
    def __init__(self, title, author, isbn, genre, copies: int):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.copies = copies
        self.genre = genre
        self.borrowed = False

    def __str__(self):
        return "Book ISBN: {}, Book Title: {}, Book Author: {}, Book Copies: {}, Book Borrowed: {}".format(
            self.isbn, self.title, self.author, self.copies, self.borrowed
        )


class User:
    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email

    def __str__(self):
        return "Name :{}, Password :{}, Email :{}".format(
            self.name, self.password, self.email
        )


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book: Book):
        self.books[book.isbn] = book

    def update_book(self, isbn, title=None, genre=None, copies=None, author=None):
        if isbn not in self.books:
            print("Book is not found")
            return
        if title:
            self.books[isbn].title = title
        if genre:
            self.books[isbn].genre = genre
        if author:
            self.books[isbn].author = author
        if copies:
            self.books[isbn].copes = copies

        print("Updated book information --> {}".format(self.books[isbn]))

    def delete_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]

    def search_book(self, item):
        pos = None
        for book in self.books.values():
            if (item == book.author) or (item == book.genre) or (item == book.title):
                return book
        return None
