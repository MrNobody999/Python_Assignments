# Write a program which contains one lambda function which accepts two parameters and return its multiplication.

# Input: 4 3 Output : 12
# Input: 6 3 Output: 18


Mult = lambda No1, No2 : No1 * No2

def main():
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))
    print(f"Multiplication of {No1} and {No2} is : ", Mult(No1, No2))



if __name__ == "__main__":
    main()