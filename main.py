from Library import Library
from Gbook import Gbooks

# world parameters:
libraries = {}  # dictionary of all the libraries
total_num_books = 0
num_libraries = 0
total_days = 0
book_scores = []

def main():
    scores = [1, 2, 3, 6, 5, 4]
    lib1 = Library(5, 2, 2, [0, 1, 2, 3, 4], scores)
    lib1.print_basic_data()
    lib2 = Library(4, 3, 1, [0, 2, 3, 5], scores)
    lib2.print_basic_data()

# takes one filepath i.e. "tests/a_example.txt" and initializes the world (GBooks and Libraries) based on the data
# file data format:
#   total_num_books, num_libraries, total_days
#   list of book scores ordered by ID
#0: num_books, signup_process, shipping_rate
#0: list of book IDs ordered by shipping order
#1: num_books, signup_process, shipping_rate
#1: list of book IDs ordered by shipping order
#...
def read_data(filepath):
    file = open(filepath, "r")
    # get world parameters
    global total_num_books, num_libraries, total_days, book_scores, gbook
    line = file.readline().split(" ")
    total_num_books, num_libraries, total_days = [int(i) for i in line]
    gbook = Gbooks(total_days, num_libraries)
    line = file.readline().split(" ")
    book_scores = [int(i) for i in line]

    # initialize libraries
    for i in range(num_libraries):
        line = file.readline().split(" ")
        num_books, signup_process, shipping_rate = [int(i) for i in line]
        line = file.readline().split(" ")
        libraries[i] = Library(num_books, signup_process, shipping_rate, [int(i) for i in line], book_scores)

def brute_force():
    pass

if __name__ == "__main__":
    # main()
    read_data("tests/a_example.txt")
    print(str(gbook.days) + " " + str(gbook.library))
    print(str(total_num_books) + " " + str(num_libraries) + " " + str(total_days))
    print(book_scores)
    for lib in libraries.values():
        print(str(lib.num_books) + " " + str(lib.signup_process) + " " + str(lib.shipping_rate))
        print(lib.book_ids)
