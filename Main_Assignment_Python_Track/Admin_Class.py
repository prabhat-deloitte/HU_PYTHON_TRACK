from Main_Assignment_Python_Track.ExcelUtility import ExcelUtils


class WrongColumName(Exception):
    pass


class Admin(ExcelUtils):
    def __init__(self):
        super().__init__()
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
        try:
            movie_name = str(input("Enter Movie name"))
            for i in range(1, ExcelUtils.Total_main_database_row+1):
                if ExcelUtils.database.cell(i, 1).value == movie_name:
                    local_dict = {"Title": "A", "Genre": "B", "Length": "C", "Cast": "D", "Director": "E",
                                  "Admin_rating": "F", "Timing": "G", "No_of Shows": "H", "First Show": "I",
                                  "Interval Time": "J", "Gap Between Shows": "K", "Capacity": "L"}
                    print(list(local_dict.keys()))
                    editable = str(input("enter what you want to edit "))
                    if editable not in local_dict:
                        raise WrongColumName
                    edit = str(input("enter the edit "))
                    editing_cell = ExcelUtils.database[local_dict[editable]+f'{i}']
                    editing_cell.value = edit
                    ExcelUtils.workbook.save(ExcelUtils.url)
        except WrongColumName:
            print("Please Enter Correct Column name")
        except Exception:
            print("something went Wrong")

    def add_movie(self):
        print("hello")



