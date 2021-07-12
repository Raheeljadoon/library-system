from Names import book_title
class Abc:
        
    def search_book(self,user_input):
            self.user_input = user_input
            user_input = (input("enter book id to find"))
            return user_input


    def __init__(self):
            if self.search_book("") in book_title:
                print("availaible")
            
            else :
                print("not")

abc = Abc()

