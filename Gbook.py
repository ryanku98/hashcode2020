#G_book class for storing books sent to Google

import os
from Library import Library

class Gbooks:
    def __init__(self, days: int, num_lib: int):
        self.days = days              #Save total time limit we have
        self.library = num_lib        #Total amount of libraries
        self.stored_books ={}            #The books inside G Books
        self.score = 0               #total scores this method got

    def computeScore(self, order, libraries) -> int:
        self.score = 0
        self.stored_books = {}
        days_left = self.days
        result = {}
        total_books = 0
        #Go through the libaries in given order
        for lib_num in order:
            days_left -= libraries[lib_num].signup_process  #days left after signup
            rate = libraries[lib_num].shipping_rate         #get the shipping rate of this library
            books_used = []
            #if there is no more days left to process after signup, quit the loop
            if days_left <= 0:
                break
            #need to start compute the book sent by this library
            else:
                day_counter = 0     #number of days we have shipped books
                length = len(libraries[lib_num].book_ids)
                count = 0           #amount of books we have processed in this library
                rate_count = 0      #books we have processed a day
                #continue as long as we have days to process and there is book to ship
                while(day_counter < days_left and count < length):
                    #store the shipped books into a dictionary so we don't repeat
                    if libraries[lib_num].book_ids[count] not in self.stored_books.keys():
                        self.stored_books[libraries[lib_num].book_ids[count]] = libraries[lib_num].scores[count]
                        books_used.append(libraries[lib_num].book_ids[count])
                        total_books += 1
                        count += 1
                        rate_count += 1
                        #if we reached max shipping per day, move one ot next day & reset rate_counter
                        if rate_count == rate:
                            day_counter +=1
                            rate_count = 0
                    else:
                        count += 1
                result[int(lib_num)] = books_used

        #compute the score in Gbook for this method
        for key in self.stored_books:
            self.score += self.stored_books[key]

        return self.score, result, total_books

if __name__ == "__main__":
    scores = [1, 2, 3, 6, 5, 4]
    lib1 = Library(5, 2, 2, [0, 1, 2, 3, 4], scores)
    lib1.print_basic_data()
    lib2 = Library(4, 3, 1, [0, 2, 3, 5], scores)
    lib2.print_basic_data()

    World = {0:lib1,1:lib2}

    G_book_1 = Gbooks(7,2)
    print(G_book_1.computeScore([0,1], World))

    print(G_book_1.computeScore([1,0], World))
