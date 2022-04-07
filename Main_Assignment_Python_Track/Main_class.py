from Main_Assignment_Python_Track.Admin_Class import Admin
from Main_Assignment_Python_Track.ExcelUtility import ExcelUtils
from Main_Assignment_Python_Track.User_class import User
from Main_Assignment_Python_Track.register_user import Registration


while True:
    user_input = int(input("******Welcome to BookMyShow******* \n1. Login \n2. Register new account\n3.Exit\n"))
    if user_input == 1:
        admin_object = Admin()
        result = admin_object.admin_login()
        print(result)
        while True:
            admin_input = 0
            if result == "Login Successful":
                admin_input = int(input("1.Admin Login:\n******Welcome Admin*******\n"
                                   "1. Add New Movie Info\n2. Edit Movie Info\n3. Delete Movies\n"
                                     "4.Logout\n"))
            if admin_input == 1:
                admin_object.add_movie()
            if admin_input == 2:
                admin_object.editmovie()
            if admin_input == 3:
                admin_object.deleteMovie()
            if admin_input == 4:
                break
            else:
                break
    if user_input == 2:
        # que = str(input("New _user ? Type yes to register"))
        # if que.islower() == "yes":
        register = Registration()
        while True:
            print("User Login:\n******Welcome to BooyMyShow*******")
            user_id = str(input("Username"))
            user_password = str(input("Password"))
            user_object = User()
            result = user_object.user_login(user_id, user_password)
            if result == "Login Successful":
                print(f"******Welcome {user_id}******* ")
                for i in range(2, ExcelUtils.Total_main_database_row+1):
                    print(f'{i-1}.{ExcelUtils.database.cell(i,1).value}')
                    if i == ExcelUtils.Total_main_database_row:
                        print(f"{i}.Logout")
                selected_movie = int(input("Enter movie "))
                print(f"******Welcome {user_id}******* ")
                for i in range(1,ExcelUtils.Total_main_database_Column):
                    print(f'{ExcelUtils.database.cell(1,i).value}:{ExcelUtils.database.cell(user_input+1,i).value}')
                print("1.  Book Tickets \n2.  Cancel Tickets \n3.  Give User Rating\n4.  Exit")
                user_input = int(input("Enter choice"))
                if user_input == 1:
                    user_object.book_ticket(selected_movie)
                if user_input == 2:
                    user_object.cancel_ticket(selected_movie)
                if user_input == 3:
                    user_object.user_rating(selected_movie)
                if user_input == 4:
                    break

















