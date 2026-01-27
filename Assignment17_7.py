# Write a program which accept one number and display below pattern.
# Input : 5
# Output : 
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

def PrintPattern(No):

    for i in range(No):
        for j in range(1,No+1):
            print(j , end=" ")
        print()

def main():
    No1 = int(input("Enter number : "))

    PrintPattern(No1)


if __name__ == "__main__":
    main()
