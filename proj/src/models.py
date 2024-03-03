class Book:
    def __init__(self, id, score):
        self.id = id
        self.score = score

    def get_score(self):
        return self.score
    
    def __str__(self):
        return str(self.score)
    
class Library:
    def __init__(self, books, signup_time, books_per_day):
        self.books = books
        self.signup_time = signup_time
        self.books_per_day = books_per_day

    def get_books(self):
        return self.books
    
    def get_signup_time(self):
        return self.signup_time
    
    def get_books_per_day(self):
        return self.books_per_day