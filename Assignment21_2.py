# Design a Python application that creates two threads.
# Thread 1 should calculate and display the maximum element from an list.
# Thread 2 should calculate and display the minimum element from the same list.
# The list should be accepted from the user.

import threading

def Maximum(Numbers):
    Maxi = Numbers[0] 
    for i in Numbers:
        if i > Maxi:
            Maxi = i
    print("Maximum number is : ",Maxi)    

def Minimum(Numbers):
    Mini = Numbers[0]
    for i in Numbers:
        if i < Mini:
            Mini = i
    print("Minimum numbers is :",Mini)



def main():

    list1 = []
    No = int(input("Enter list elements : "))
    print("Enter list elements : ")
    for _ in range(No):
        list1.append(input())

    Thread1 = threading.Thread(target= Maximum, args = (list1, ))
    Thread2 = threading.Thread(target= Minimum, args = (list1, ))

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

    print("Main thread completed")

if __name__ == "__main__":
    main()