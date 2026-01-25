# Question : Write a lambda function which accepts one number and returns cube of that number.

Cube = lambda No1 : No1 ** 3

def main():
    No1 = int(input("Enter Number"))
    print(f"Cube of {No1} is : ", (Cube(No1)))

if __name__ == "__main__":
    main()