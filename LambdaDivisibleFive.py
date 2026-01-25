# Question : Write a lambda function which accept one number and returns True if divisible by 5.
    

DivisibleFive = lambda No1 : True if No1 % 5 == 0 else False

def main():
    No1 = int(input("Enter number : "))
    Ret = DivisibleFive(No1)
    if Ret == True:
        print(f"{No1} is divisible by 5.")
    else:
        print(f"{No1} is not divisible by 5.")

if __name__ == "__main__":
    main()