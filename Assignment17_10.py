# Write a program which accept number from user and return addition of digits in that number.
# Input : 5187934
# Output : 37

def DigitSum(No):
    iSum = 0
    while No > 0:
        iDigit = No % 10
        iSum = iSum + iDigit
        No = No // 10
    return iSum

def main():
    No1 = int(input("Enter number : "))

    print(f"Sum of digits of {No1} is : ",DigitSum(No1))


if __name__ == "__main__":
    main()