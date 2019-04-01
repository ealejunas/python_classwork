class Calculator:
    what = "im a class of calculator"  # class variable

    def calc_addition(self, n1, n2):
        return n1 + n2

    def calc_subtract(self, n1, n2):
        return n1 - n2

    def calc_mult(self, n1, n2):
        return n1 * n2

    def calc_div(self, n1, n2):
        return n1 / n2

    def menu(self):
        input1 = int(input("Welcome to my calculator! Enter your first number."))
        operator = input("Enter your operator.")
        input2 = int(input("Enter your second number."))
        result = 0

        if operator == "+":
            result = calc_addition(input1, input2)
        elif operator == "-":
            result = calc_subtract(input1, input2)
        elif operator == "/":
            result = calc_div(input1, input2)
        else:
            result = calc_mult(input1, input2)
        return result

    print("The result is " + str(Calculator()))


print(Calculator.what)

#initiated an object of calculator
my_cal_instance = Calculator()
print(my_cal_instance.add())



#
# # print possible choice of function
#
# print("Select your operation:")
# print("1. Add ")
# print("2. Subtract ")
# print("3. Multiply ")
# print("4. Divide ")
#
# # Take input from the user, this will be stored in variable 'choice'
#
# choice = input("Enter choice(1/2/3/4):")
#
# # actual inputs
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
#
#
# if choice == '1':
#     print(num1, "+", num2, "=", calc_addition(num1, num2))
# elif choice == '2':
#     print(num1, "-", num2, "=", calc_subtract(num1, num2))
# elif choice == '3':
#     print(num1, "*", num2, "=", calc_mult(num1, num2))
# elif choice == '4':
#     print(num1, "/", num2, "=", calc_div(num1, num2))
# else:
#     print("Invalid input")
