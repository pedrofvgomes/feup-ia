from models import Library, Book

def read_file(input_file):
    error = [], [], 0
    
    file = open(input_file, 'r')
    lines = file.readlines()
    
    a = lines[0]
    b = lines[1]
    
    lines = [line.strip() for line in lines[2:]]
    
    if len(a.strip().split(' ')) != 3:
        print(len(a.strip().split(' ')))
        return error
    else:
        a = a.strip().split(' ')
        num_books = int(a[0])
        num_libraries = int(a[1])
        num_days = int(a[2])
        
    if len(b.strip().split(' ')) != num_books:
        print(b.strip().split(' '))
        print(num_books)
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
                    
    return books, libraries, num_days