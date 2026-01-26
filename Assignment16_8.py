# Write a program which accept number from user and print that number of "*"" on screen. 
# Input : 5 
# Output :  *   *   *   *   *


def PrintStar(No1):
    for i in range(No1):
        print("*", end=" ")
    print()

def main():
    No1 = int(input("Enter number : "))
    PrintStar(No1)

if __name__ == "__main__":
    main()