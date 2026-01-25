# Question : Write a lambda function which accept one number and returns True if number is even otherwise False.

# def CheckEven(No1):
#     if No1 % 2 == 0 :
#         return True
    

CheckEven = lambda No1 : True if No1 % 2 == 0 else False

def main():
    No1 = int(input("Enter number : "))
    Ret = CheckEven(No1)
    if Ret == True:
        print(f"{No1} is Even.")
    else:
        print(f"{No1} is Odd.")

if __name__ == "__main__":
    main()