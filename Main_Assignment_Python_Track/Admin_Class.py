from Main_Assignment_Python_Track.ExcelUtility import ExcelUtils
import datetime



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
                    local_dict = {"Title": "A", "Genre": "B", "Length in hours": "C", "Cast": "D", "Director": "E",
                                  "Admin_rating": "F", "No_of Shows": "H", "First Show": "I",
                                  "Interval Time in minutes": "J", "Gap Between Shows in minutes": "K", "Capacity": "L"}
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
            #for i in range(1, ExcelUtils.Total_main_database_row):
            print("Please fill the below Requirements")
            local_dict = {"Title": "A", "Genre": "B", "Length": "C", "Cast": "D", "Director": "E",
                            "Admin_rating": "F", "No_of Shows": "H", "First Show": "I",
                            "Interval Time": "J", "Gap Between Shows": "K", "Capacity": "L", "Available Seats":"N"}
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
            print("Something Went Wrong or may movie is not present")

    def calculate_timing(self):
        try:
            ExcelUtils()
            local_dict = {"length":"C", "No_of_show":"H", "first_show":"I", "Interval time":"J", "Gap":"K"}
            retained_dict={}
            for i in local_dict.keys():
                values = ExcelUtils.database[f'{local_dict[i]}{ExcelUtils.Total_main_database_row}'].value
                if values not in retained_dict:
                     retained_dict[i] = values
            timing_list = []
            start_time = datetime.timedelta(hours=int(retained_dict["first_show"]))
            interval_time = datetime.timedelta(hours=0 ,minutes=int(retained_dict["Interval time"]))
            movie_length_list = retained_dict["length"].split('.')
            movie_length = datetime.timedelta(hours=int(movie_length_list[0]), minutes=int(movie_length_list[1]))
            gap = datetime.timedelta(hours=0,minutes=int(retained_dict["Gap"]))

            for i in range(0, int(float(retained_dict["No_of_show"]))):
                timing_list.append(f'{start_time}-{start_time + movie_length + interval_time}')
                start_time = start_time + movie_length + interval_time + gap
            timing_list = ",".join(map(str, timing_list))
            time_column = ExcelUtils.database[f'G{ExcelUtils.Total_main_database_row}']
            time_column.value = timing_list
            ExcelUtils.workbook.save(ExcelUtils.url)
            print("time slots added successfully")
        except Exception as e:
            print(e)


