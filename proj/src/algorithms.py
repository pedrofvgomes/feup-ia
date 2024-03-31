import os
import random, math
from models import Book, Library


def read_input_file(input_file):
    error = [], [], 0
    
    file = open(input_file, 'r')
    lines = file.readlines()
    
    a = lines[0]
    b = lines[1]
    
    lines = [line.strip() for line in lines[2:]]
    
    if len(a.strip().split(' ')) != 3:
        return error
    else:
        a = a.strip().split(' ')
        num_books = int(a[0])
        num_libraries = int(a[1])
        num_days = int(a[2])
        
    if len(b.strip().split(' ')) != num_books:
        return error
    
    else:
        b = b.strip().split(' ')
        books = []
        for book in b:
            books.append(Book(len(books), int(book)))
            
    if num_libraries*2 != len([line for line in lines if len(line)]):
        return error
    
    libraries = []
    added_lib = False
    for line in lines:
        if len(line):
            line = line.split(' ')
            if not added_lib:
                libraries.append(Library(len(libraries), int(line[1]), int(line[2])))
                added_lib = True
            else:
                for book_id in line:
                    libraries[-1].add_book(books[int(book_id)])
                added_lib = False
                    
    return num_days, libraries

def apply_greedy_algorithm(input_file):
    # Read input data
    D, libraries = read_input_file(input_file)

    # Sort libraries based on a heuristic: a ratio of the total score of books to the signup time.
    for library in libraries:
        library.sort_books()  # Sort books in each library based on scores
    libraries.sort(key=lambda lib: sum(book.score for book in lib.books) / lib.signup_time, reverse=True)

    # Days remaining to sign up libraries and scan books
    days_remaining = D
    signup_process = []  # To keep track of the signup process
    books_scanned = set()  # To keep track of the books that have been scanned
    total_score = 0  # Initialize total score

    # Loop through each library and determine if it can be signed up within the remaining days
    for library in libraries:
        if days_remaining <= 0 or days_remaining < library.signup_time:
            break  # No more days left to sign up new libraries
        days_remaining -= library.signup_time
        
        # Calculate the number of books that can be scanned from this library
        books_to_scan = []
        for book in library.books:
            if len(books_to_scan) < days_remaining * library.books_per_day and book.id not in books_scanned:
                books_to_scan.append(book)
                books_scanned.add(book.id)
                total_score += book.score
        signup_process.append((library, books_to_scan))

    # Write the results to the output file
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_path = f'proj/output/{base_name}_greedy.txt'
    
    ### FIXME: BY PEDRO - remover isto se usarmos a helper function
    if not os.path.exists('proj/output'):
        os.makedirs('proj/output')
    ###
    
    with open(output_path, 'w') as file:
        # Write the number of libraries to sign up
        file.write(f"{len(signup_process)}\n")
        for library, books in signup_process:
        # Write the library ID and the number of books to scan
            file.write(f"{library.id} {len(books)}\n")
            # Write the book IDs in the order they are scanned
            book_ids = ' '.join(str(book.id) for book in books)
            file.write(book_ids + "\n")

    print(f'Greedy algorithm applied for {base_name} with total score: {total_score}')

def apply_simulated_annealing(input_file):
    D, libraries = read_input_file(input_file)

    current_solution = initial_solution(D, libraries)
    current_score = score_solution(current_solution, D)
    
    T = 1.0
    T_min = 0.001
    alpha = 0.9

    while T > T_min:
        i = 1
        while i <= 100:
            new_solution = neighbor_solution(current_solution, libraries, D)
            new_score = score_solution(new_solution, D)
            
            # Calculate change in score
            delta = new_score - current_score
            
            # Acceptance probability
            acceptance_probability = math.exp(delta / T) if delta < 0 else 1
            
            # Decide if we should accept the new solution
            if acceptance_probability > random.random():
                current_solution = new_solution
                current_score = new_score
            
            i += 1
        
        T *= alpha  # Cool down the temperature

    # Output the best solution found
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_path = f'proj/output/{base_name}_simulated_annealing.txt'
    write_solution(output_path, current_solution)

    print(f'Simulated Annealing applied for {base_name} with a total score of {current_score}')
    
"""
HILL CLIMBING ALGORITHM
- Description:
    - Start with an initial solution and iteratively make small changes to it to find a better solution.
    - If the new solution is better than the current solution, accept it.
    - If the new solution is worse than the current solution, accept it with a probability based on the temperature.
- Pros:
    - Simple to implement.
    - Can find good solutions quickly.
- Cons:
    - Can get stuck in local optima.
    - Requires fine-tuning of parameters.
"""
def apply_hill_climbing(input_file):
    D, libraries = read_input_file(input_file)
    
    current_solution = initial_solution(D, libraries)
    current_score = score_solution(current_solution, D)
    
    best_solution = current_solution
    best_score = current_score
    
    while True:
        neighbor_sol = neighbor_solution(current_solution, libraries, D)
        neighbor_score = score_solution(neighbor_sol, D)
        
        if neighbor_score > current_score:
            current_solution = neighbor_sol
            current_score = neighbor_score
            
            if current_score > best_score:
                best_solution = current_solution
                best_score = current_score
        else:
            break
    
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_path = f'proj/output/{base_name}_hill_climbing.txt'
    write_solution(output_path, best_solution)
    
    print(f'Hill Climbing applied for {base_name} with a total score of {best_score}')

# Helper functions

def initial_solution(D, libraries):
    # Start with no libraries signed up
    solution = []
    days_remaining = D
    for library in libraries:
        if days_remaining - library.signup_time >= 0:
            solution.append((library, []))
            days_remaining -= library.signup_time
    random.shuffle(solution)  # Shuffle the initial solution
    return solution

def neighbor_solution(solution, libraries, D):
    # Make a random change in the solution to generate a neighbor
    if not solution:
        return solution
    
    neighbor = solution[:]
    idx = random.randrange(len(neighbor))
    library, _ = neighbor[idx]
    
    # Randomly decide to change the order of the library signup or change the books
    if random.random() < 0.5:
        # Swap two libraries' positions
        idx_swap = random.randrange(len(neighbor))
        neighbor[idx], neighbor[idx_swap] = neighbor[idx_swap], neighbor[idx]
    else:
        # Change the books to scan in the library
        random_books = random.sample(library.books, min(len(library.books), library.books_per_day * (D - library.signup_time)))
        neighbor[idx] = (library, random_books)
    
    return neighbor

def score_solution(solution, D):
    score = 0
    books_scanned = set()
    days_remaining = D
    for library, books in solution:
        days_remaining -= library.signup_time
        if days_remaining <= 0:
            break
        # Calculate how many books can actually be scanned
        num_scanned_books = min(days_remaining * library.books_per_day, len(books))
        for book in books[:num_scanned_books]:
            if book.id not in books_scanned:
                score += book.score
                books_scanned.add(book.id)
    return score

def write_solution(output_path, solution):
    if not os.path.exists('proj/output'):
        os.makedirs('proj/output')
    with open(output_path, 'w') as f:
        f.write(f"{len(solution)}\n")  # Write the number of libraries
        for library, books in solution:
            f.write(f"{library.id} {len(books)}\n")  # Write library id and the number of books
            book_ids = ' '.join(str(book.id) for book in books)
            f.write(f"{book_ids}\n")  # Write the book ids