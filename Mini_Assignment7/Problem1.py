class FormulaError(Exception): pass


def calculator(value1, operator, value2):
    try:
        if operator == "+":
            return print(value1 + value2)
        if operator == "-":
            return print(value1 - value2)
        if operator == "*":
            return print(value1 * value2)
        if operator == "/":
            return print(value1 / value2)
        else:
            raise FormulaError
    except FormulaError:
        print("entered operator is wrong")


while True:
    try:
        user_input = input("enter expression ")
        if user_input == "quit":
            exit()
        user_list = user_input.split(" ")
        if len(user_list) != 3:
            raise FormulaError
        value_one = float(user_list[0])
        value_two = float(user_list[2])
        
        calculator(value_one, user_list[1], value_two)

    except ValueError:
        print("entered value is not floating type")
    except FormulaError:
        print("entered expression in wrong ")

