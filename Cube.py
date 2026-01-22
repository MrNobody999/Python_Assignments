
def Cube(No1):
    # return No1 ** 3
    return No1 * No1 * No1    

def main():
    print("Enter Number : ")
    No1 = int(input())
    Ret = Cube(No1)
    print("Cube of number is: ", Ret)

if __name__ == "__main__":
    main() 