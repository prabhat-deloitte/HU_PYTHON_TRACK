from Main_Assignment_Python_Track.ExcelUtility import ExcelUtils



class User(ExcelUtils):
    def __init__(self):
        super().__init__()
        ExcelUtils()

    def user_login(self, user_name, user_password):

        for i in range(1, ExcelUtils.Total_user_row + 1):
            if ExcelUtils.user_sheet.cell(i, 1).value == user_name:
                if ExcelUtils.user_sheet.cell(i, 2).value == user_password:
                    return "Login Successful"
                else:
                    return "Wrong_Password"
        return 'Wrong_username'

    def book_ticket(self, movie_index):
        try:
            ExcelUtils()
            print("Timing")
            timing = list(ExcelUtils.database[f'G{movie_index+1}'].value.split(","))
            for i in range(0, len(timing)):
                print(f'{i+1}. {timing[i]}')
            selected_time = int(input("Select Timing "))
            print(f'Timing: {timing[selected_time-1]}')
            remaining_seat = int(ExcelUtils.database[f'N{movie_index+1}'].value)
            print(f"Remaining Seat : {remaining_seat}")
            booked_seat = int(input("Enter no of seats you want to book"))
            available_seat = remaining_seat - booked_seat
            while available_seat<0:
                booked_seat = int(input("Booked More then available seats re enter the seats "))
                available_seat = remaining_seat-booked_seat
            print("Thanks for booking")
            updated_seats = ExcelUtils.database[f'N{movie_index + 1}']
            updated_seats.value = available_seat
            ExcelUtils.workbook.save(ExcelUtils.url)

        except Exception:
            print("Something Went wrong")

    def cancel_ticket(self, movie_index):

        cancelled_seat = int(input("no of seats you want to cancel"))
        remaining_seat = int(ExcelUtils.database[f'N{movie_index + 1}'].value)
        available_seat = remaining_seat + cancelled_seat
        updated_seats = ExcelUtils.database[f'N{movie_index + 1}']
        updated_seats.value = available_seat
        ExcelUtils.workbook.save(ExcelUtils.url)
        print("ticket cancelled Successfully")

    def user_rating(self, movie_index):

        user_review = str(input("Enter user_review\n1. *\n2. **\n3. ***\n4. ****\n5. *****"))
        updated_review = ExcelUtils.database[f'M{movie_index + 1}']
        updated_review.value = user_review
        ExcelUtils.workbook.save(ExcelUtils.url)
        print("your valuable feedback is stored successfully")


