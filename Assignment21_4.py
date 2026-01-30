# Design a Python application that creates two threads.
# Thread 1 should compute the sum of elements from a list.
# Thread 2 should compute the product of elements from the same list.
# Return the results to the main thread and display them.


import threading

def ElementsSum(Numbers):
    Sum = 0 
    for i in Numbers:
        Sum += i
    print("Sum of list elements is : ",Sum)    

def ElementsProduct(Numbers):
    product = 1 
    for i in Numbers:
        product *= i
    print("Product of list elements is :",product)


def main():

    list1 = [4, 34, 36, 76, 68, 24]

    Thread1 = threading.Thread(target= ElementsSum, args = (list1, ))
    Thread2 = threading.Thread(target= ElementsProduct, args = (list1, ))

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

    print("Main thread completed")

if __name__ == "__main__":
    main()