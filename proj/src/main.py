import sys

def read_file(input_file):
    # if the file is found, print success
    # otherwise, print error
    try:
        with open(input_file, "r") as f:
            print("File found!")
    except FileNotFoundError:
        print("File not found!")
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