variable_first = int(input("Enter first number: "))
variable_second = int(input("Enter first second: "))
operator_option = input("Enter operator: ")

if operator_option == "+":
    print(variable_first + variable_second)
elif operator_option == "-":
    print(variable_first - variable_second)
elif operator_option == "*":
    print(variable_first * variable_second)
elif operator_option == "/":
    if variable_second == 0:
        print("Error: Division by zero is not allowed!")
        exit()
    print(variable_first / variable_second)
else:
    print("Error")