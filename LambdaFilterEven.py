# Question : Write a lambda function using filter() which accepts a list of numbers and returns a list of evev numders.

CheckEven = lambda No1 : No1 % 2 == 0


def main():
    Data = [1,2,3,4,5,6,7,8,9,10]
    print("Actual Data is : ",Data)

    MData = list(filter(CheckEven,Data))
    print("Data after CheckEven is : ",MData)

if __name__ == "__main__":
    main()