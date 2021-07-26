

import copy
# from loan import Loan
import random
import string
from Names import book_title , author_name , publisher_name , user_name , sur_names , first_names , street_name
# from user import User



class Books :
    def __init__(self,Id,title,author,year,publisher,availaible_copies,publication_date,*args) :
        self.book_id = Id
        self.book_title = title
        self.book_author = author
        self.book_year = year
        self.book_publisher = publisher
        self.book_availaible = availaible_copies
        self.publication_date = publication_date

    book_id = random.randint(0,50)
    book_publisher = random.choice(publisher_name)
    book_availaible = random.randint(1,5)
    book_title = random.choice(book_title)


    def Book_id(self):

        
        self.book_id = Books.book_id
        return "book id is : ",self.book_id


    def Title(self):
        self.book_title = Books.book_title
        return "book title is : ",self.book_title
        

    def Author(self):
        self.book_author = random.choice(author_name)
        return "book author is : ",self.book_author


    def Year(self):
        self.book_year = random.randint(2005,2020)
        return "book publish year is :",self.book_year

    def Publisher(self):
        self.book_publisher = Books.book_publisher
        return "book publisher is :",self.book_publisher


    def Availaible_copies(self):
        self.book_availaible = Books.book_availaible
        return "availaible copies are : ",self.book_availaible


    def Copies_After_Buy(self):
        
        self.book_availaible1 = self.book_availaible - 1

        return "remaining copies are ", self.book_availaible1


    def Copies_After_Return(self):
        self.book_availaible1 = self.book_availaible
        return "remaining copies are " , self.book_availaible1 + 1


    def Publication_date(self):
        def gen_Publication_Date(number):
            for item in range(number):
                yield self.book_year, random.randrange(1, 12), random.randrange(1, 29)

        date_Time = gen_Publication_Date(1)

        for year, month, date in date_Time:
            # print("Date of publication is :", year ,"/", month ,"/", date)
            self.publication_date = year , month , date
             

        return "publication date is ",self.publication_date 



        



class BooksList(Books) :
    def Instances_information(self):
        

        books_list = []  
        for x in range(1):
    
    
   
            books_list.append(book)



        for each_book in books_list:
            print(each_book.Title(),"\n",each_book.Book_id(),"\n",each_book.Author())
            print(each_book.Publisher(),"\n",each_book.Availaible_copies(),"\n",each_book.Year(),"\n",each_book.Publication_date())


    



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
                print("book detail are : book id is {0} book publisher is {1} book availaible copies are {2}".format(Books.book_id , Books.book_publisher,Books.book_availaible))

            else :
                print("Book is not availaible")
        elif user_choice == 2:

            if self.search_book_ByAuthor() in author_name:
                print("Book is availaible")
                print("book detail are :book title is {0} book id is {1} book publisher is {2} book availaible copies are {3}".format(Books.book_title,Books.book_id , Books.book_publisher,Books.book_availaible))

            else :
                print("Book is not availaible")

        elif user_choice == 3 :

            if self.search_book_ByPublisher() in publisher_name:
                print("book is availaible ")
                print("book detail are :book title is {0} book id is {1}  book availaible copies are {2}".format(Books.book_title,Books.book_id , Books.book_availaible))

            else:
                print("Book is not availaible")


    def Book_Remove(self):

        user_choice = input("which book do you want to remove \n")
        book_title.remove(user_choice)
        print("the book have been removed")

    
    def Total_books(self):
        return "total books availaible are : ",len(book_title)    


    def Total_booksName(self):
        return book_title



        


    

      

class User :

    first_name = random.choice(first_names)
    sur_name = random.choice(sur_names)
    user_name =  random.choice(user_name)
    postcode = random.randint(10000,99999)


    def __init__(self,user_name,f_name,s_name,house_number,street_name,postcode,email_address,date_of_birth) :
        self.user_name = user_name
        self.first_names = f_name
        self.sur_names = s_name
        self.house_number = house_number
        self.street_name = street_name
        self.postcode = postcode
        self.email_address = email_address
        self.date_of_birth = date_of_birth


    def User_Name(self):
        
        self.user_name =  User.user_name
        return "user_name of user is ",self.user_name
        
    def First_Name(self):
        self.first_names = User.first_name
        return "user first name is ",self.first_names

    def Sur_Name(self):
        self.sur_names = User.sur_name
        return "user surname is ", self.sur_names

    def House_Number(self):
        self.house_number = random.randint(1,50)
        return "user house number is ",self.house_number


    def Street_Name(self):
        self.street_name = random.choice(street_name)
        return "user street name is ",self.street_name


    def Post_Code(self):
        self.postcode = User.postcode
        return "user postal code is ",self.postcode

    def Email_Address(self):
        self.email_address = User.user_name + "@gmail.com"
        return "user email address is ",self.email_address

    def Date_of_birth(self):
        def gen_Date_of_birth(number):
            for item in range(number):
                yield random.randrange(2000,2014), random.randrange(1, 12), random.randrange(1, 29)

        date_Time = gen_Date_of_birth(1)

        for year, month, date in date_Time:
           
            self.date_of_birth = year , month , date

        return "date of birth is ",self.date_of_birth


    def Total_Usernames(self):
        return user_name

    



    def Change_first_name(self):
        self.first_names = User.first_name
        new_firstName = []
        
        
        print("your name is ",self.first_names)

        self.user_new = input("please write new name  :")

        for first_name in self.first_names:
            newfirstname = first_name.replace(self.first_names , self.user_new)
            new_firstName.append(newfirstname)

        return " New first name is",self.user_new 



    def Change_sur_name(self):
        self.sur_names = User.sur_name
        new_surName = []
        
        print("New surname is ",self.sur_names)

        self.user_new = input("please write new  surname  :")

        for sur_name in self.sur_names:
            newsurname = sur_name.replace(self.sur_names , self.user_new)
            new_surName.append(newsurname)

        
        return "your new surname is",self.user_new 

      

    def Change_email_address(self):
        self.email_address = User.user_name + "@gmail.com"
        
        print("your email is ",self.email_address)

        self.user_new = input("please write new email  :")
        
        return "your new email  is",self.user_new 


    def Change_date_of_birth(self):
        print(self.Date_of_birth() )
        self.new_dob = input("please put new date of birth seprated by comma  :")

        return "now date of birth is ",self.new_dob


class Userlist(User):

    def Instances_information(self):
        user_list = []  
        for instance in range(1):
    
    
   
            user_list.append(user)



        for each_user in user_list:
            print(each_user.User_Name(),"\n",each_user.First_Name(),"\n",each_user.Sur_Name())
            print(each_user.House_Number(),"\n",each_user.Email_Address(),"\n",each_user.Date_of_birth(),"\n",each_user.Post_Code())




    def Remove_User(self):
        user_input = input("which user do you want to remove by user firstname ")
        if user_input in first_names:
            first_names.remove(user_input)
        

            return user_input," have been removed"

        else :
            return"user not found"


    def User_count(self):
        print("total user are ", len(first_names))


    def search_user_ByUsername(self):
            
        self.user_input = input("enter username  to find user  :")
        


    
        
        if self.user_input in user_name :
            return "user found user first name is {0},sur name is {1} Email addres is {2}, Postal code is {3}".format(User.first_name,User.sur_name,self.user_input+"@gmail.com", User.postcode)
            

        else :
            return "no such username found"






class Loans (User,Books):
    def __init__(self,user_return,user_borrow):

    # def __init__(self, user_name, f_name, s_name, house_number, street_name, postcode, email_address, date_of_birth,name):
    #     super().__init__(user_name, f_name, s_name, house_number, street_name, postcode, email_address, date_of_birth)
        self.book_input_list = []
        self.User_input_forReturn = user_return
        self.user_input_forBorrow = user_borrow

       



      

    
        
       
    
    
    
    def Borrow_book(self):
        self.book_input_list = []
        self.total_book = 0
        

        for self.user_input_forBorrow  in range(0,1)  :
                while self.total_book < 5:
                    self.user_input_forBorrow = input("which book do you want to borrow  ")

                    
                

                    if self.user_input_forBorrow in book_title :
                        self.book_input_list.append(self.user_input_forBorrow)
                        print(self.Availaible_copies())
                        print("you borrowed the book")
                        book_title.remove(self.user_input_forBorrow)
                        print( self.Copies_After_Buy())
                    
                        self.total_book = self.total_book + 1
                        
                        


                        self.user_input_foragain = input("do you want to buy another book ! y or n ")
                        if self.user_input_foragain == "y":
                            continue
                        


                        elif self.user_input_foragain  == "n":
                            break

                        a = "total book you buy are ",self.total_book 


                    else :
                        print("The book you enter is not availaible")

                # print("the books you due are ",self.book_input_list)
                

                

                        

    

    def Total_Borrow_book(self):
    
             
        print("total borrowed books are ",len(self.book_input_list))


    

    def Return_book(self):
        self.User_input_forReturn = input("which book you wanted to return ")
        if self.User_input_forReturn in book_title :


            print("book have returned ! Thanks")
            book_title.append(self.User_input_forReturn)
            print(self.Copies_After_Return())

        else :
            print("you enter wrong book name ")





    def Over_due_books(self):
        
        


        if self.User_input_forReturn   in  self.book_input_list  :
            print("you dont have any overdue books")

        else :
            print("overdue books are ",self.user_input_forBorrow)

        
    


        
print("welcome to library managment system")
user_choice = int(input("what you want to do \n 1 : Books Information \n 2 : User Information \n 3 : Borrow Books"))

if user_choice == 1:
    book = Books("","","","","","","")
    book1 = BooksList("","","","","","","")

    user_choice1 = int(input("what you want to do \n 1: Show all books \n 2: Show one book complete information \n 3 : Search A book \n 4 : Remove A Book"))

    if user_choice1 == 1:

        print("\n",book1.Total_books(),"\n")
        print("books name are \n",book1.Total_booksName())

    elif user_choice1 == 2:

        book1.Instances_information()


    elif user_choice1 == 3 :
        book1.Search_result()

    elif user_choice1 == 4:
        book1.Book_Remove()

    
    # print(book.Book_id())
    # print(book.Publisher())
    # print(book.Title())User_Name()





elif user_choice == 2:


    user = User("","","","","","","","")
    user1 = Userlist("","","","","","","","")

    user_choice2 = int(input("what you want to do \n 1 : Show All Users username \n 2 : One User complete information \n 3 : Change User Information \n 4 : Remove User \n 5 : Search User "))

    if user_choice2 == 1 :
        print(user1.User_count())
        print(user.Total_Usernames())

    if user_choice2 == 2 :
        user1.Instances_information()
        user_choice2_1 = int(input("what you want to change \n 1 : Change user first name\n 2 : Change sur name \n 3 : Change email address \n 4 : Change date of birth"))
        if user_choice2_1 == 1 :

           print( user.Change_first_name())

        elif user_choice2_1 == 2:
            print(user.Change_sur_name())

        elif user_choice2_1 == 3:
            print(user.Change_email_address())

        elif user_choice2_1 == 4:
            print(user.Change_date_of_birth())

    if user_choice2 == 4 :
        print(user1.Remove_User())


    if user_choice2 == 5:
        print(user1.search_user_ByUsername())

    



elif user_choice == 3 :
    loan = Loans("","")
    user_choice3 = int(input("what you want to do \n 1 : Borrowed a Book \n 2 : Return a book \n 3 : Total Borrow book \n 4 : Check Overdue books"))

    if user_choice3 == 1 :
        loan.Borrow_book()

    elif user_choice3 == 2 :
        loan.Return_book()

    elif user_choice3 == 3 :
        loan.Total_Borrow_book()

    elif user_choice3 == 4 :
        loan.Over_due_books()



   
    # loan.Borrow_book()
    # loan.Return_book()
    # loan.Total_Borrow_book()
    # loan.Over_due_books()


# print(book.Availaible_copies())
# print(book.Copies_After_Buy())