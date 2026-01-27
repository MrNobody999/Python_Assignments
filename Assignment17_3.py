# Write a program which accept one number from user and return its factorial.
# Input : 5
# Output : 120

def Factorial(No):
    Fact = 1
    for i in range(1, No+1):
        Fact = Fact * i
    return Fact

def main():
    No1 = int(input("Enter number : "))

    print(f"Factorial of {No1} is : ",Factorial(No1))


if __name__ == "__main__":
    main()