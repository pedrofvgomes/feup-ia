class Book:
    def __init__(self, id, score):
        self.id = id
        self.score = score
    
    def __repr__(self):
        return f"ID: {self.id} - Score: {self.score}"


class Library:
    def __init__(self, id, signup_time, books_per_day):
        self.id = id
        self.signup_time = signup_time
        self.books_per_day = books_per_day
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def __repr__(self):
        return f"Library(ID: {self.id}, Signup Time: {self.signup_time}, Books/Day: {self.books_per_day}, Books: {len(self.books)})"
