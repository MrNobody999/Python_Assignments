# Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all prime numbers. Map function will multiply each number by 2. Reduce will
# return Maximum number from that numbers. (You can also use normal functions instead of
# lambda functions).

# Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
# List after filter = [2, 11, 17, 23, 31]
# List after map = [4, 22, 34, 46, 62]
# Output of reduce = 62

from functools import reduce

def ChkPrime(No):
    for i in range(2,No):
        if No % i == 0 :
            return False
    return True


MultiplyTwo = lambda No : No * 2

Maximum = lambda No1, No2 : No1 if No1 > No2 else No2

def main():

    list1 = [2, 70 , 11, 10, 17, 23, 31, 77]

    FData = list(filter(ChkPrime, list1))
    print("Filtered data : ", FData)

    MData = list(map(MultiplyTwo, FData))
    print("Data after Map : ", MData)

    RData = int(reduce(Maximum, MData))
    print("Data after Reduce : ", RData)

if __name__ == "__main__":
    main()