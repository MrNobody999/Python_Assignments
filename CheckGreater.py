
def ChkGreater(No1, No2):
    if (No1 > No2):
        print(No1)
    else:
        print(No2)
    

def main():
    No1 = int(input())
    No2 = int(input())
    #No2 = input(int(print("Enter second number : ")))
    ChkGreater(No1, No2)

if __name__ == "__main__":
    main() 