#G_book class for storing books sent to Google

import os
from Library import Library

class Gbooks:
    def __init__(self, days: int, num_lib:int ) -> int:
        self.days = days              #Save total time limit we have
        self.library = num_lib        #Total amount of libraries
        self.stored_books = {}             #The books inside G Books
        self.score = 0                #total scores this method got

    def computeScore(self, order, libraries) -> int:
        #Go through the libaries in given order
        for lib_num in order:
            self.days -= libraries[lib_num].signup_process  #days left after signup
            rate = libraries[lib_num].shipping_rate         #get the shipping rate of this library
            if self.days <= 0:
                break
            else:
                day_counter = 0
                length = len(libraries[lib_num].book_ids)
                count = 0
                rate_count = 0
                while(day_counter < self.days and count < length):
                    self.stored_books[libraries[lib_num].book_ids[count]] = libraries[lib_num].scores[count]
                    count += 1
                    rate_count += 1
                    if rate_count == rate:
                        day_counter +=1
                        rate_count = 0

        for key in self.stored_books:
            self.score += self.stored_books[key]

        return self.score

if __name__ == "__main__":
    scores = [1, 2, 3, 6, 5, 4]
    lib1 = Library(5, 2, 2, [0, 1, 2, 3, 4], scores)
    lib1.print_basic_data()
    lib2 = Library(4, 3, 1, [0, 2, 3, 5], scores)
    lib2.print_basic_data()

    World = {0:lib1,1:lib2}

    G_book_1 = Gbooks(7,2)
    print(G_book_1.computeScore([0,1], World))

    G_book_2 = Gbooks(7,2)
    print(G_book_2.computeScore([1,0], World))
