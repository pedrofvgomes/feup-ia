import sys
from models import Library, Book

def read_file(input_file):
    # if the file is found, print success
    # otherwise, print error
    try:
        f = open(input_file, "r")
        print("File found!")
    except FileNotFoundError:
        print("File not found!")
        return
    
    """
    STATE MANAGEMENT:
    A - read number of books, libraries, and days
    B - read book scores
    C - read library information
    """
    state = "A"

    """
    DATA STRUCTURES
    - books - list of book scores, that will be used to assign to libraries
    - libraries - list of libraries, that'll be returned
    """
    books = []
    libraries = []

    """
    VARIABLES 
    - num_books - number of books in the library
    - num_libraries - number of libraries in the library
    - num_days - number of days to scan the library
    """
    num_books = 0
    num_libraries = 0
    num_days = 0

    # print lines until the file ends
    while True:
        # try to read line
        line = f.readline()

        # file ended
        if not line:
            print("File reading complete!")
            return
        
        # handle line
        match state:
            # read number of books, libraries, and days
            case "A":
                # split line
                temp = line.split(" ")

                # assign values
                num_books = int(temp[0])
                num_libraries = int(temp[1])
                num_days = int(temp[2])

                # print values
                print("Number of books: " + str(num_books))
                print("Number of libraries: " + str(num_libraries))
                print("Number of days: " + str(num_days))

                # change state
                state = "B"

            # read book scores
            case "B":
                # split line and create Book objects
                for book in line.split(" "):
                    books.append(Book(int(book)))

                # print book scores
                print("Book scores: ", [str(book) for book in books])

                # change state
                state = "C"

            # read library information
            case "C":
                print("C")
            
            # default case, return
            case _:
                return

def main():
    # take the first argument as the input file
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_file>")
        return
    
    input_file = sys.argv[1]
    print("Reading '" + input_file + "'...")
    
    libraries = read_file(input_file)

if __name__ == "__main__":
    main()