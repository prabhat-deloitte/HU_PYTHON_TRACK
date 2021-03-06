from Main_Assignment_Python_Track.ExcelUtility import ExcelUtils
from Main_Assignment_Python_Track.User_class import User


class UserExists(Exception):
    pass


class Registration(User):

        def __init__(self):
            try:
                super().__init__()
                ExcelUtils()
                new_user = str(input("Enter New Username"))
                temp_username = new_user
                local_dict = {"Username": "A", "Password": "B", "Email": "C", "Phone": "D", "Age": "E"}
                for i in range(1, ExcelUtils.Total_user_row):
                    if ExcelUtils.user_sheet.cell(i,1).value == new_user:
                        raise UserExists
                for i in local_dict:
                    if i != "Username":
                        new_user = str(input(f'{i}:'))
                    cell = ExcelUtils.user_sheet[f'{local_dict[i]}{ExcelUtils.Total_user_row+1}']
                    cell.value = new_user

                ExcelUtils.workbook.save(ExcelUtils.url)
                ExcelUtils.workbook.close()
                print(f'{temp_username} added Successful')
            except UserExists:
                print("User already exists")
            except Exception:
                print("Something went Wrong")



