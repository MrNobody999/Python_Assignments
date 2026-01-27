# Write a program which accept N numbers from user and)store it into List. Return Minimum number from that List.
# Input : Number of elements: 4
# Input Elements : 13 5 45 7
# Output : 5

def MinimumNo(list):
    Mini = list[0]

    for i in list:
        if i < Mini:
            Mini = i

    return Mini


def main():
    list1 = []
    Nos = int(input("Enter list elements: "))

    for i in range(Nos):
        num = int(input(f"Enter Number {i + 1} : "))
        list1.append(num)
    
    Ret = MinimumNo(list1)
    print("Minimum Number is : ", Ret)


if __name__ == "__main__":
    main()