from Main_Assignment_Python_Track.ExcelUtility import ExcelUtils


class Admin(ExcelUtils):
    def __init__(self):
        ExcelUtils()

    def admin_login(self):

        admin_name = str(input("Enter the admin Username"))
        admin_password = str(input("enter Password"))
        for i in range(1, ExcelUtils.Total_row + 1):

            if ExcelUtils.sheet.cell(i, 1).value == admin_name:
                if ExcelUtils.sheet.cell(i, 2).value == admin_password:
                    return"Login Successful"
                else:
                    return "wrong_Password"
        return "Wrong Admin_Username"

    def EditMovie(self):
        movie_name = str(input("Enter Movie name"))
        for i in range(1, ExcelUtils.Total_main_database_row+1):
            if ExcelUtils.database.cell(i, 1).value == movie_name:
                print("okay")




