# Question : Write a lambda function using reduce() which accepts a list of numbers and returns the maximum element.

from functools import reduce

Maximum = lambda No1, No2 : No1 if No1 >= No2 else No2 


def main():
    Data = [11,21,33,45,54,6,77,88,99,10]
    print("Actual Data is : ",Data)

    RData = reduce(Maximum,Data)
    print("Data after reduce is : ",RData)

if __name__ == "__main__":
    main()