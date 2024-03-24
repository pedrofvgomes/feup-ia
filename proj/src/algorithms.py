"""
PROBLEM FORMULATION

- List of libraries
    - Each library has a signup time
    - Each library has a maximum number of books that can be shipped each day
    - Each library has a list of books, each book has a score
- List of books
    - Irrelevant here, since the only books that matter are the ones in the libraries
- Number of days
    - We have this range to work with

- Objective: Maximize the score
- Constraints:
    - Signup processes can't overlap
    - Books can't be shipped after the deadline, neither can they be shipped before the signup process for their library is complete
    - Books can exist in multiple libraries, and thus can be scanned more than once, but their score is only counted once - SHOULDN'T HAPPEN
    - Libraries can scan books in parallel, only if they have gone through the signup process
"""

def scan_books(libraries, num_days):
    # this is the list where we'll store the IDs of the libraries that've been signed up,
    # and thus can scan books
    signed_up = []
    
    # this is the library ongoing signup process, associated to the days left in its process
    # when this variable is set, no other library can start its signup process
    signing_up = tuple()
    
    # this is the dictionary where we'll store the IDs of the libraries that are scanning books,
    # associated to a list of the books they've scanned (because multiple libraries can have the same book)
    scanned_books = {}    
    
    initial_days = num_days
    
    # LOOP THROUGH THE DAYS - THIS WILL BE EASY ONCE THE STATE SPACE IS ORGANIZED
    while num_days > 0:
        print(f'DAY {initial_days-num_days+1}')
        
        if signing_up and signing_up[1] == 0:
            signed_up.append(signing_up[0])
            signing_up = tuple()
        
        if not signing_up and len([lib for lib in libraries if lib.id not in signed_up]) > 0:
            new_lib = [lib for lib in libraries if lib.id not in signed_up][0]
            signing_up = (new_lib.id, new_lib.signup_time)
        
        ##
        if signing_up:
            print(f'Sign up library {signing_up[0]}')
        ##
        
        for lib in [l for l in libraries if l.id in signed_up]:
            if lib.id not in scanned_books:
                scanned_books[lib.id] = []
                               
            if len([book.id for book in lib.books if book.id not in scanned_books[lib.id]][:lib.books_per_day]) > 0:
                print(f'Scan books {[book.id for book in lib.books if book.id not in scanned_books[lib.id]][:lib.books_per_day]} from library {lib.id}')
            
            scanned_books[lib.id] += [book.id for book in lib.books if book.id not in scanned_books[lib.id]][:lib.books_per_day]
            
        num_days -= 1
        if signing_up:
            signing_up = (signing_up[0], signing_up[1] - 1)
            
        print('\n')
    
from utils import read_file
books, libraries, num_days = read_file(r'proj/data/b_read_on.txt')
scan_books(libraries, num_days)