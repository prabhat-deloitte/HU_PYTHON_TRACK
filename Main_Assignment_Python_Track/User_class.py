from Main_Assignment_Python_Track.ExcelUtility import ExcelUtils


class User(ExcelUtils):
    def User_login(self):
        ExcelUtils()
        user_name = str(input("Enter the User details"))
        user_password = str(input("enter Password"))
        for i in range(1, ExcelUtils.Total_user_row + 1):
            if ExcelUtils.user_sheet.cell(i, 1).value == user_name:
                if ExcelUtils.user_sheet.cell(i, 2).value == user_password:
                    return "Login Successful"
                else:
                    return "wrong_Password"
        return 'Wrong_username'