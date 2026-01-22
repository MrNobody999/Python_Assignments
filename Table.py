
def Table(No1):
    # for i  in range(No1, No1 * 10 + 1, No1):
    #     print(i)

    i = 10
    while(i > 0):
        print(No1)
        No1 += 5
        i = i - 1



def main():
    print("Enter Number: ")
    No1 = int(input())
    Table(No1)


if __name__ == "__main__":
    main()