import math     # ceil()

class Library():
    # book_ids: array of IDs of books inside this library
    # scores: list of scores for all books; should remain unchanged
    def __init__(self, num_books, signup_process, shipping_rate, book_ids, scores):
        self.num_books = num_books
        self.signup_process = signup_process
        self.shipping_rate = shipping_rate
        self.book_ids = book_ids

        # initialize scores for books in this library
        self.scores = []
        for i in self.book_ids:
            self.scores.append(scores[i])

        # calculate sum of self.scores
        self.total_score = 0
        for i in self.scores:
            self.total_score += i

        # calculate total days required to signup and ship ALL books
        self.total_days = self.signup_process + math.ceil(self.num_books / self.shipping_rate)

    def print_basic_data(self):
        print("self.book_ids: " + str(self.book_ids))
        print("self.scores: " + str(self.scores))
        print("self.total_days: " + str(self.total_days))

if __name__ == "__main__":
    scores = [1, 2, 3, 6, 5, 4]
    lib1 = Library(5, 2, 2, [0, 1, 2, 3, 4], scores)
    lib1.print_basic_data()
    lib2 = Library(4, 3, 1, [0, 2, 3, 5], scores)
    lib2.print_basic_data()
