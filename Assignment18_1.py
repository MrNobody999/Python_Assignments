# Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.
# Input : Number of elements : 6
# Input Elements : 13 5 45 7 4 56
# Output : 130

def Addition(list):
    Sum = 0
    for i in list:
        Sum += i

    return Sum


def main():
    list1 = []
    Nos = int(input("Enter how many numbers do you want to addition : "))

    for i in range(Nos):
        num = float(input(f"Enter Number {i + 1} : "))
        list1.append(num)
    
    Ret = Addition(list1)
    print("Addition is : ", Ret)


if __name__ == "__main__":
    main()