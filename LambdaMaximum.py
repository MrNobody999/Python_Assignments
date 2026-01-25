#Question : Write a lambda function which accepts two numbers and returns maximum number.
# def Maximum(No1, No2):
#     if No1 > No2:
#         return No1
#     else:
#         return No2
    
Maximum = lambda No1, No2 : No1 if No1 >= No2 else No2 

def main():
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))
        
    print("Maximum number is : ", (Maximum(No1, No2)))

if __name__ == "__main__":
    main()