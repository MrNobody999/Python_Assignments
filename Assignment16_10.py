# Write a program which accept name from user and display length of its name.
# Input : Marvellous 
# Output : 10


def CountChars(Name):
    iCnt = 0
    for i in Name:
        iCnt += 1
    return iCnt

def main():
    Name = input("Enter String : ")
    print(CountChars(Name))

if __name__ == "__main__":
    main()