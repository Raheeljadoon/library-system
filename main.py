import random
import string
from Names import book_title , author_name , publisher_name

class Books :
    def __init__(self,Id,title,author,year,publisher,availaible_copies,publication_date,*args) :
        self.book_id = Id
        self.book_title = title
        self.book_author = author
        self.book_year = year
        self.book_publisher = publisher
        self.book_availaible = availaible_copies
        self.publication_date = publication_date


    def Book_id(self):
        
        self.book_id = random.randint(0,50)
        return ("book id is : ",self.book_id)


    def Title(self):
        self.book_title = random.choice(book_title)
        return("book title is : ",self.book_title)
        

    def Author(self):
        self.book_author = random.choice(author_name)
        return("book author is : ",self.book_author)


    def Year(self):
        self.book_year = random.randint(2005,2020)
        return("book publish year is :",self.book_year)

    def Publisher(self):
        self.book_publisher = random.choice(publisher_name)
        return("book publisher is :",self.book_publisher)


    def Availaible_copies(self):
        self.book_availaible = random.randint(1,5)
        return("availaible copies are : ",self.book_availaible)


    def Publication_date(self):
        def gen_Publication_Date(number):
            for item in range(number):
                yield random.randrange(2005,2020), random.randrange(1, 12), random.randrange(1, 29)

        date_Time = gen_Publication_Date(1)

        for year, month, date in date_Time:
            # print("Date of publication is :", year ,"/", month ,"/", date)
            a = year , month , date
            self.publication_date = a

        return self.publication_date 

    def Combine(self):
        
          
        self.book_id = random.randint(0,50)
       

        self.book_title = random.choice(book_title)

        self.book_availaible = random.randint(1,5)

        self.book_publisher = random.choice(publisher_name)

        self.book_author = random.choice(author_name)

        def gen_Publication_Date(number):
            for item in range(number):
                yield random.randrange(2005,2020), random.randrange(1, 12), random.randrange(1, 29)

        date_Time = gen_Publication_Date(1)

        for year, month, date in date_Time:
            # print("Date of publication is :", year ,"/", month ,"/", date)
            a = year , month , date
            self.publication_date = a

        
       

        return ("book id is ",self.book_id,"book title is ",self.book_title,"book author is ",self.book_author,"availaible copies are ",self.book_availaible,"book publication date is ",self.publication_date,)
        



class BooksList(Books) :
      pass

class User :
    pass


class UserList :
    pass



class Loans :
    pass




book = Books("","","","","","","")

books_list = []  
for x in range(5):
    book.Combine()
    
   
    books_list.append(book.Combine())
    
    


# print(books_list)
setss = set(books_list)
print(setss)

if "Steven" in setss:
    print("yes ")
else :
    print("no")

