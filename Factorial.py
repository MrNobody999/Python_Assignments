
def Factorial(No1):
    Ans = 1
    for i in range(1, No1+1):
        Ans = Ans * i
    return Ans



def main():
    print("Enter Number: ")
    No1 = int(input())
    Ret = Factorial(No1)
    print(f"Factorial of {No1} is : ", Ret)


if __name__ == "__main__":
    main()