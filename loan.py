
from Names import book_title
from books import


class Loan():
    def Borrow_book(self):
        user_input = input("which book do you want to borrow")
        if user_input in book_title :
            print("book availaible copies are :", self.book_availaible)
            print("you borrowed the book")
            
        else:
            print("the book you are trying are not availaible")


loan  = Loan()
loan.Borrow_book()