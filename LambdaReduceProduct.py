# Question : Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements.

from functools import reduce


Product = lambda No1, No2 : No1 * No2 


def main():
    Data = [1,2,3,4,5]
    print("Actual Data is : ",Data)

    RData = reduce(Product, Data)
    print("Data after reduce is : ",RData)

if __name__ == "__main__":
    main()