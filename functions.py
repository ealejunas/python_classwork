# def print_something(text):
#     print(text)
#
# print_something("I want chicken")
# print_something("Now I want falafel")

# this is a method that adds two numbers
# def adding_two_numbers(n1=4, n2=11):
#         return n1 + n2
#
#
# def add_any_numbers(*numbers):
#     for num in numbers:
#         print(num)
#
# result = add_any_numbers(1, 2, 3, 4, 5, 6, 7, 8, 1, 3)
# result1 = adding_two_numbers()
# print(result)
# print("----")
# print(result1)


# creating a calculator

# define 4 functions

def calc_addition(n1, n2):
    return n1 + n2


def calc_subtract(n1, n2):
    return n1 - n2


def calc_mult(n1, n2):
    return n1 * n2


def calc_div(n1, n2):
    return n1 / n2


# print possible choice of function

print("Select your operation:")
print("1. Add ")
print("2. Subtract ")
print("3. Multiply ")
print("4. Divide ")

# Take input from the user, this will be stored in variable 'choice'

choice = input("Enter choice(1/2/3/4):")

# actual inputs
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


if choice == '1':
    print(num1, "+", num2, "=", calc_addition(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", calc_subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", calc_mult(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", calc_div(num1, num2))
else:
    print("Invalid input")

