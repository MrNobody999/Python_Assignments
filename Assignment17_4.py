# Write a program which accept one number form user and return addition of its factors.
# Input : 12
# Output : 16    (1+2+3+4+6)

def FactorsAddition(No):
    Sum = 0
    for i in range(1,(No//2)+1):
        if No % i == 0:
            Sum += i
    return Sum

def main():
    No1 = int(input("Enter number : "))

    print(f"Addition of factors of {No1} is : ",FactorsAddition(No1))


if __name__ == "__main__":
    main()