from Main_Assignment_Python_Track.Admin_Class import Admin
from Main_Assignment_Python_Track.ExcelUtility import ExcelUtils
from Main_Assignment_Python_Track.User_class import User

while True:
    user_input = int(input("******Welcome to BookMyShow******* \n1. Login \n2. Register new account\n3.Exit"))
    if user_input == 1:
        admin_object = Admin()
        result = admin_object.admin_login()
        while True:
            if result == "Login Successful":
                user_input = int(input("1.Admin Login:\n******Welcome Admin*******\n"
                                       "1. Add New Movie Info\n2. Edit Movie Info\n3. Delete Movies\n4.Logout"))
            if user_input == 2:
                admin_object.EditMovie()
            if user_input == 4:
                break




