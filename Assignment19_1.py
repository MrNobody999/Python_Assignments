# Write a program which contains one lambda function which accepts one parameter and return power of two.
# Input : 4 Output : 16
# Input : 6 Output : 36

# def LambdaPower(No):
#     return No ** 2

LambdaPower = lambda No : No ** 2

def main():
    No1 = int(input("Enter number : "))
    print(f"Power of two of {No1} is : ", LambdaPower(No1))



if __name__ == "__main__":
    main()