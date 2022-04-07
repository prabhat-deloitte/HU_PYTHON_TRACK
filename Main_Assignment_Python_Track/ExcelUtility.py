import openpyxl


class ExcelUtils:
    def __init__(self):
        workbook = openpyxl.load_workbook("C:\\Users\\praparihar\\Desktop\\New Microsoft Excel Worksheet.xlsx")
        ExcelUtils.sheet = workbook.worksheets[0]
        ExcelUtils.Total_row = ExcelUtils.sheet.max_row
        ExcelUtils.Total_Column = ExcelUtils.sheet.max_column
        ExcelUtils.user_sheet = workbook.worksheets[1]
        ExcelUtils.Total_user_row = ExcelUtils.user_sheet.max_row
        ExcelUtils.Total_user_Column = ExcelUtils.user_sheet.max_column
        ExcelUtils.database = workbook.worksheets[2]
        ExcelUtils.Total_main_database_row = ExcelUtils.database.max_row
        ExcelUtils.Total_main_database_Column = ExcelUtils.database.max_column





