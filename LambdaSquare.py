# Question : Write a lambda function which accepts one number and returns square of that number.

# def Square(No1):
#     return No1 ** 2

Square = lambda No1 : No1 ** 2

def main():
    No1 = int(input("Enter Number"))
    print(f"Square of {No1} is  ", (Square(No1)))

if __name__ == "__main__":
    main()