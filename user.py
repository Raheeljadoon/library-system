import random
from Names import first_names , sur_names , street_name , user_name
class User :
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
        
        self.user_name =  random.choice(user_name)
        return "user_name of user is ",self.user_name
        
    def First_Name(self):
        self.first_names = random.choice(first_names)
        return "user first name is ",self.first_names

    def Sur_Name(self):
        self.sur_names = random.choice(sur_names)
        return "user surname is ", self.sur_names

    def House_Number(self):
        self.house_number = random.randint(1,50)
        return "user house number is ",self.house_number


    def Street_Name(self):
        self.street_name = random.choice(street_name)
        return "user street name is ",self.street_name


    def Post_Code(self):
        self.postcode = random.randint(10000,99999)
        return "user postal code is ",self.postcode

    def Email_Address(self):
        self.email_address = self.user_name + "@gmail.com"
        return "user email address is ",self.email_address

    def Date_of_birth(self):
        def gen_Date_of_birth(number):
            for item in range(number):
                yield random.randrange(2000,2014), random.randrange(1, 12), random.randrange(1, 29)

        date_Time = gen_Date_of_birth(1)

        for year, month, date in date_Time:
           
            self.date_of_birth = year , month , date

        return "date of birth is ",self.date_of_birth







    def Change_first_name(self):
        self.first_names = random.choice(first_names)
        
        print("your name is ",self.first_names)

        self.user_new = input("please write new name  :")

        return "your new first name is",self.user_new 



    def Change_sur_name(self):
        self.sur_names = random.choice(sur_names)
        
        print("your surname is ",self.sur_names)

        self.user_new = input("please write new  surname  :")
        
        return "your new surname is",self.user_new 

      

    def Change_email_address(self):
        self.email_address = self.user_name + "@gmail.com"
        
        print("your email is ",self.email_address)

        self.user_new = input("please write new email  :")
        
        return "your new email  is",self.user_new 


    def Change_date_of_birth(self):
        print("your date of birth is ",self.date_of_birth )
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
        user_input = input("which user do you want to remove ")
        if user_input in first_names:
            first_names.remove(user_input)
        

            print(user_input," have been removed")

        else :
            print("user not found")


    def User_count(self):
        print("total user are ", len(first_names))


    def search_user_ByUsername(self):
            
        user_input = input("enter username  to find  :")
        return user_input


    def User_detail(self):
        self.user_name =  random.choice(user_name)
        if self.search_user_ByUsername() in user_name :
            print("user found \n detail are {0}{1}{2}{3}{4}{5}".format(self.First_Name(),self.Sur_Name(),self.Street_Name(),self.Post_Code(),self.Email_Address(),self.Date_of_birth()))

        else :
            print("no such username found")


      











user = User("","","","","","","","")
# print(user.User_Name())
# print(user.First_Name())
# print(user.Sur_Name())
# print(user.Street_Name())
# print(user.Post_Code())
# print(user.Email_Address())
# print(user.Date_of_birth())
# print(user.Change_first_name())
# print(user.Change_email_address())
# print(user.Change_date_of_birth())
# print(user.Change_sur_name())


user1 = Userlist("","","","","","","","")
user1.Instances_information()
user1.Remove_User()
user1.User_count()
user1.User_detail()