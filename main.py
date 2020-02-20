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

# return array of arrays of order to signup libraries
def sort_by_total_score()->list:
    orders = []             # array of all the orders
    library_scores = []     # scores of each library
    library_order = []      # index of libraries, parallel to library_scores
    for i, lib in libraries.items():
        library_scores.append(lib.total_score)
        library_order.append(i)

    zipped = list(zip(library_scores, library_order))
    # sort by descending order
    zipped.sort(reverse = True)
    s, o = zip(*zipped)
    orders.append(o)
    # include ascending order
    zipped.sort()
    s, o = zip(*zipped)
    orders.append(o)

    return orders

def sort_by_signup()->list:
    library_signup_time =[]
    library_id = []
    result = []
    #Put the all the signup time of all libraries into a list
    for key in libraries:
        library_signup_time.append(libraries[key].signup_process)
        library_id.append(key)
    #sort the order of list based on signup time, result in a list of library id
    result.append([x for _,x in sorted(zip(library_signup_time,library_id))])
    result.append([x for _,x in sorted(zip(library_signup_time,library_id), reverse=True)])
    return result

def sort_by_rate() ->list:
    library_rate =[]
    library_id = []
    result = []
    #Put the all the shipping rate of all libraries into a list
    for key in libraries:
        library_rate.append(libraries[key].shipping_rate)
        library_id.append(key)
    #sort the order of list based on shipping rate, result in a list of library id
    result.append([x for _,x in sorted(zip(library_rate,library_id))])
    result.append([x for _,x in sorted(zip(library_rate,library_id), reverse=True)])
    return result

def print_submission_file(submission: str, num : int, input_order : list, libs : dict):
    # libs: dictionary keyed by library ID, values are books inputed in order
    file = open("submissions/" + submission, "w")
    # file.write(str(num) + "\n")
    n = len(libs)
    file.write(str(n) + "\n")
    for x, i in enumerate(input_order):
        if x >= n:
            break
        try:
            n_books = len(libs[i])
        except:
            continue
        if n_books == 0:
            continue
        # write library index and number of books of from this library
        file.write(str(i) + " " + str(n_books) + "\n")
        # write in index of order of books inputed
        for b in libs[i]:
            file.write(str(b) + " ")
        file.write("\n")
    print("file closing")
    file.close()

if __name__ == "__main__":
    # main()
    # filename = "a_example.txt"
    # filename = "b_read_on.txt"
    # filename = "c_incunabula.txt"
    filename = "d_tough_choices.txt"
    # filename = "e_so_many_books.txt"
    # filename = "f_libraries_of_the_world.txt"
    read_data("tests/" + filename)
    sign_up_by_total_score = sort_by_total_score()
    sign_up_by_signup = sort_by_signup()
    sign_up_by_rate = sort_by_rate()
    # print(sign_up_by_total_score)
    # print(sign_up_by_signup)
    # print(sign_up_by_rate)
    all_orders = sign_up_by_total_score
    for l in sign_up_by_signup:
        all_orders.append(l)
    for l in sign_up_by_rate:
        all_orders.append(l)

    max_score = 0
    max_result = {}
    max_order = []
    max_num = 0
    for o in all_orders:
        score, result, num = gbook.computeScore(o, libraries)
        if max_score < score:
            max_order = o
            max_score = score
            max_result = result
            max_num = num
    # print(max_score, max_result, max_order)
    print_submission_file(filename, num, max_order, max_result)
    print(max_score)

    # print(str(gbook.days) + " " + str(gbook.library))
    # print(str(total_num_books) + " " + str(num_libraries) + " " + str(total_days))
    # print(book_scores)
    # for lib in libraries.values():
    #     print(str(lib.num_books) + " " + str(lib.signup_process) + " " + str(lib.shipping_rate))
    #     print(lib.book_ids)
