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

    def editmovie(self):
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
                    print(f'{editable} is Edited Successfully')
        except WrongColumName:
            print("Please Enter Correct Column name")
        except Exception:
            print()

    def add_movie(self):
        try:
            for i in range(1, ExcelUtils.Total_main_database_row):
                print("Please fill the below Requirements")
                local_dict = {"Title": "A", "Genre": "B", "Length": "C", "Cast": "D", "Director": "E",
                              "Admin_rating": "F", "Timing": "G", "No_of Shows": "H", "First Show": "I",
                              "Interval Time": "J", "Gap Between Shows": "K", "Capacity": "L"}
                for j in local_dict:
                    edit = str(input(f'{j}:'))
                    cell = ExcelUtils.database[f'{local_dict[j]}{ExcelUtils.Total_main_database_row + 1}']
                    cell.value = edit

            ExcelUtils.workbook.save(ExcelUtils.url)
            print("Movie added Successfully")
        except Exception:
            print("Something Went Wrong")

    def deleteMovie(self):
        try:
            movie_name = str(input("Enter the Movie you want to delete"))
            index = 0
            for i in range(1, ExcelUtils.Total_main_database_row):
                if ExcelUtils.database.cell(i, 1).value == movie_name:
                    index = i
            ExcelUtils.database.delete_rows(index, 1)
            ExcelUtils.workbook.save(ExcelUtils.url)
            print(f'{movie_name} is deleted successfully')
        except Exception:
            print("Something Went Wrong")

    def calculate_timing(self):
        local_dict = {"length":"C", "No_of_show":"H", "first_show":"I", "Interval time":"J", "Gap":"K"}
        retained_dict={}
        for i in local_dict.keys():
             values = ExcelUtils.database[f'{local_dict[i]}{ExcelUtils.Total_main_database_row}'].value
             if values not in retained_dict:
                 retained_dict[i] = values
        timing_list = []
        total_movie_length = float(retained_dict["first_show"]) + float(retained_dict["length"]) + float(
            retained_dict["Interval time"])
        # for j in range(0, int(retained_dict["No_of_show"])):
        #     start_time =






o = Admin()
o.calculate_timing()