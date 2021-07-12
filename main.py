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
        return "book id is : ",self.book_id


    def Title(self):
        self.book_title = random.choice(book_title)
        return "book title is : ",self.book_title
        

    def Author(self):
        self.book_author = random.choice(author_name)
        return "book author is : ",self.book_author


    def Year(self):
        self.book_year = random.randint(2005,2020)
        return "book publish year is :",self.book_year

    def Publisher(self):
        self.book_publisher = random.choice(publisher_name)
        return "book publisher is :",self.book_publisher


    def Availaible_copies(self):
        self.book_availaible = random.randint(1,5)
        return "availaible copies are : ",self.book_availaible


    def Publication_date(self):
        def gen_Publication_Date(number):
            for item in range(number):
                yield self.book_year, random.randrange(1, 12), random.randrange(1, 29)

        date_Time = gen_Publication_Date(1)

        for year, month, date in date_Time:
            # print("Date of publication is :", year ,"/", month ,"/", date)
            a = year , month , date
            self.publication_date = a

        return "publication date is ",self.publication_date 



        



class BooksList() :
    def Instances_information(self):
        book = Books("","","","","","","")

        books_list = []  
        for x in range(1):
    
    
   
            books_list.append(book)



        for each_book in books_list:
            print(each_book.Title(),"\n",each_book.Book_id(),"\n",each_book.Author())
            print(each_book.Publisher(),"\n",each_book.Availaible_copies(),"\n",each_book.Year(),"\n",each_book.Publication_date())

    # def Combine(self):
        
          
    #     self.book_id = random.randint(0,50)
       

    #     self.book_title = random.choice(book_title)

    #     self.book_availaible = random.randint(1,5)

    #     self.book_publisher = random.choice(publisher_name)

    #     self.book_author = random.choice(author_name)

    #     def gen_Publication_Date(number):
    #         for item in range(number):
    #             yield random.randrange(2005,2020), random.randrange(1, 12), random.randrange(1, 29)

    #     date_Time = gen_Publication_Date(1)

    #     for year, month, date in date_Time:
    #         # print("Date of publication is :", year ,"/", month ,"/", date)
    #         a = year , month , date
    #         self.publication_date = a

    #     return "Book id is ",self.book_id,"Book title is ",self.book_title,"Book author is ",self.book_author,"Availaible copies are ",self.book_availaible,"Book publication date is ",self.publication_date,"................."

    



    def search_book_ByTitle(self):
            
        user_input = input("enter book title to find  :")
        return user_input

    
    def search_book_ByAuthor(self):
            
        user_input = input("enter book author to find  :")
        return user_input


    def search_book_ByPublisher(self):
            
        user_input = input("enter book publisher to find  :")
        return user_input

    def search_book_ByPublication_date(self):
            
        user_input = int(input("enter book title to find  :"))
        return user_input



    


    def Search_result(self):
        user_choice =int(input("how do you want to search a book \n 1 : ByTitle\n 2 : ByAuthorNAme \n 3 : ByBookPublisher  \n"))
        if user_choice == 1:

            if self.search_book_ByTitle() in book_title :
                print("Book is availaible")
                print("book detail are : book id is {0} book publisher is {1} book availaible copies are {2}".format(self.book_id , self.book_publisher,self.book_availaible))

            else :
                print("Book is not availaible")
        elif user_choice == 2:

            if self.search_book_ByAuthor() in author_name:
                print("Book is availaible")

            else :
                print("Book is not availaible")

        elif user_choice == 3 :

            if self.search_book_ByPublisher() in publisher_name:
                print("book is availaible ")

            else:
                print("Book is not availaible")


    def Book_Remove(self):

        user_choice = input("which book do you want to remove \n")
        book_title.remove(user_choice)
        print("the book have been removed")

    
    def Total_books(self):
        print("total books availaible are : ",len(book_title))        



        


    

      

class User :
    pass


class UserList :
    pass



class Loans :
    pass



book = Books("","","","","","","")

# books_list = []  
# for x in range(1):
    
    
   
#     books_list.append(book)



# for each_book in books_list:
#     print(each_book.Title(),"\n",each_

# for x in range(5):
#     book.Combine()
    
   
#     books_list.append(book.Combine())

# print(books_list)


book1 = BooksList()
book1.Instances_information()

book1.Search_result()

book1.Book_Remove()

book1.Total_books()

