# Write a program which accept number from user and return number of digits in that number.
# Input : 5187934
# Output : 7

def DigitCount(No):
    iCnt = 0
    while No > 0:
        iCnt += 1
        No = No // 10
    return iCnt

def main():
    No1 = int(input("Enter number : "))

    print(f"Number of digits in {No1} is : ",DigitCount(No1))


if __name__ == "__main__":
    main()