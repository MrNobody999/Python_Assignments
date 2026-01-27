# Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction,
# Mult()) for multiplication and Div() for division. All functions accepts two
# parameters as number and perform the operation. Write on python program which call all the functions from Arithmetic module by accepting the parameters from user.

import Arithmetic

def main():
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    print(f"Addition of {No1} and {No2} is : ", Arithmetic.Add(No1, No2))
    print(f"Subtraction of {No1} and {No2} is : ", Arithmetic.Sub(No1, No2))
    print(f"Multiplication of {No1} and {No2} is : ", Arithmetic.Mult(No1, No2))
    print(f"Division of {No1} and {No2} is : ", Arithmetic.Div(No1, No2))


if __name__ == "__main__":
    main()
