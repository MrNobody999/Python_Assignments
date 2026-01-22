
def Divisible(No1):
    if No1 % 3 == 0 and No1 % 5 == 0:
        return True

def main():
    print("Enter Number : ")
    No1 = int(input())
    Ret = False
    Ret = Divisible(No1)
    if Ret == True:
        print("Given number is divisible by 3 and 5.")
    else:
        print("Given number is not divisible by 3 and 5.")
    
if __name__ == "__main__":
    main() 