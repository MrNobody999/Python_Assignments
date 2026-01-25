# Question : Write a lambda function which accept one number and returns True if number is odd otherwise False.

# def CheckOdd(No1):
#     if No1 % 2 == 1 :
#         return True
    

CheckOdd = lambda No1 : True if No1 % 2 == 1 else False

def main():
    No1 = int(input("Enter number : "))
    Ret = CheckOdd(No1)
    if Ret == True:
        print(f"{No1} is Odd.")
    else:
        print(f"{No1} is Even.")

if __name__ == "__main__":
    main()