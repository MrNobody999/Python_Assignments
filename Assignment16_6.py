# Write a program which accept number from user and check whether that number is positive or negative or zero.
# Input : 11
# Output : Positive Number
# Input: -8
# Output : Negative Number
# Input : 0
# Output : Zero


def ChkNum(No1):
    if No1 > 0:
        print("Positive Number")
    elif No1 < 0:
        print("Negative Number")
    elif No1 == 0:
        print("Zero")

def main():
    No1 = int(input("Enter number : "))
    ChkNum(No1)

if __name__ == "__main__":
    main()