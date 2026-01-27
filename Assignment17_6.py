# Write a program which accept one number and display below pattern.
# Input : 5
# Output :
# * * * * *
# * * * *
# * * *
# * *
# *

def PrintPattern(No):

    for i in range(No, 0, -1):
        for j in range(i,0, -1):
            print("*" , end=" ")
        print()

def main():
    No1 = int(input("Enter number : "))

    PrintPattern(No1)


if __name__ == "__main__":
    main()
