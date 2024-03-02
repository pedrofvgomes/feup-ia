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
        C1 - read number of books, signup time, and books per day
        C2 - read book IDs
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
            return libraries
        
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

                # change state
                state = "B"

            # read book scores
            case "B":
                # split line and create Book objects
                for book in line.split(" "):
                    books.append(Book(int(book)))

                # change state
                state = "C1"

            # read library information
            case "C1":                
                # split line
                temp = line.split(" ")

                # assign values
                n = int(temp[0])
                t = int(temp[1])
                m = int(temp[2])

                # create library object
                libraries.append(Library([], t, m))

                # change state
                state = "C2"

            # read book IDs
            case "C2":
                # split line and add books to library
                for book in line.split(" "):
                    libraries[-1].books.append(books[int(book)])

                # if n is different from the number of books in the library, print error
                if len(libraries[-1].books) != n:
                    print("Error: Number of books in library " + str(len(libraries)) + " is not equal to " + str(n))
                    return

                # change state
                state = "C1"

            # default case, return
            case _:
                return
