import sys

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
                print("A")

            # read book scores
            case "B":
                print("B")

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