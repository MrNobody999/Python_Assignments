# Write a program nich display 5 times Marvellous on screen.
# Marvellous 
# Marvellous 
# Marvellous 
# Marvellous 
# Marvellous


def printMarvellous(No1):
    for i in range(No1):
        print("Marvellous")

def main():
    No1 = int(input("Enter number : "))
    printMarvellous(No1)

if __name__ == "__main__":
    main()