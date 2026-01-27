# Write a program which accept one number from user and check whether number is prime or not.
# Input : 5
# Output : It is prime number

def ChkPrime(No):
    for i in range(2, No):
        if No % i == 0:
            return False
    return True

def main():
    No1 = int(input("Enter number : "))

    Ret = ChkPrime(No1)
    if Ret == True:
        print(f"{No1} is a prime number.")
    else:
        print(f"{No1} is not a prime number.")

if __name__ == "__main__":
    main()