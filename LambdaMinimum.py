# Question : Write a lambda function which accepts two numbers and returns minimum number.
# def Minimum(No1, No2):
#     if No1 < No2:
#         return No1
#     else:
#         return No2
    
Minimum = lambda No1, No2 : No1 if No1 <= No2 else No2 

def main():
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))
        
    print("Minimum number is : ", (Minimum(No1, No2)))

if __name__ == "__main__":
    main()