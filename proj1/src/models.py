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
        self.books = []  # This will contain instances of Books
    
    def add_book(self, book):
        self.books.append(book)
    
    def __repr__(self):
        return f"Library(ID: {self.id}, Signup Time: {self.signup_time}, Books/Day: {self.books_per_day}, Books: {len(self.books)})"

    # Additional method to sort the books by their score, which will be used in the greedy algorithm.
    def sort_books(self):
        self.books.sort(key=lambda x: x.score, reverse=True)
        
        
# this class will be used in the Genetic Algorithm approach
class Chromosome:
    def __init__(self, libraries):
        self.libraries = libraries
        self.score = 0