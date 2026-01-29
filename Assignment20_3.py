# Design a Python application that creates two threads named EvenList and OddList.
# Both threads should accept a list of integers as input.
# The EvenList thread should:
   # Extract all even elements from the list.
   # Calculate and display their sum,
# The OddList thread should:
   # Extract all odd elements from the list.
   # Calculate and display their sum,
# Threads should run concurrently

import threading

def EvenList(Numbers):
    list1 = []
    Sum = 0
    for i in Numbers:
        if i % 2 == 0:
            list1.append(i)
            Sum += i

    print("Even elements are : ",list1)    
    print(f"Sum of even numbers is : ", Sum)

def OddList(Numbers):
    list1 = []
    Sum = 0
    for i in Numbers:
        if i % 2 == 1:
            list1.append(i)
            Sum += i    
    print("Odd elements are :",list1)    
    print(f"Sum of odd numbers is : ", Sum)



def main():

    list1 = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

    Even_thread = threading.Thread(target= EvenList, args = (list1, ))
    Odd_thread = threading.Thread(target= OddList, args = (list1, ))

    Even_thread.start()
    Odd_thread.start()

    Even_thread.join()
    Odd_thread.join()

    print("Main thread completed")

if __name__ == "__main__":
    main()