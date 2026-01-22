
def Sum(No1):
    Sum = 0
    for i in range(No1+1):
        Sum = Sum + i
    return Sum



def main():
    print("Enter Number: ")
    No1 = int(input())
    Ret = Sum(No1)
    print(f"Sum of {No1} natural number is : ", Ret)


if __name__ == "__main__":
    main()