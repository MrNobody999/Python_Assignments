# Question : Write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers.

from functools import reduce


CountEven = lambda No1 : No1 % 2 == 0 


def main():
    Data = [1,2,3,4,5,6,7,8,9,10,12]
    print("Actual Data is : ",Data)

    FData = len(list(filter(CountEven,Data)))
    print("Data after filter is : ",FData)


if __name__ == "__main__":
    main()