# Design a Python application that creates two threads named Prime and NonPrime.
# Both threads should accept a list of integer:
# The Prime thread should display all prime numbers from the list.
# The NonPrime thread should display all non-prime numbers from the list.

import threading

def is_Prime(No1):
    for i in range(2, int(No1 ** 0.5)+1):
        if No1 % i == 0:
            return False
    return True
    

def PrimeNos(Numbers):
    list1 = []
    for i in Numbers:
        if is_Prime(i):
             list1.append(i)
    print("Prime numbers are : ",list1)    

def NonPrimeNos(Numbers):
    list1 = []
    for i in Numbers:
        if not is_Prime(i):
            list1.append(i)
    print("Non numbers are :",list1)



def main():

    list1 = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

    Thread1 = threading.Thread(target= PrimeNos, args = (list1, ), name = "Prime")
    Thread2 = threading.Thread(target= NonPrimeNos, args = (list1, ), name = "NonPrime")

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

    print("Main thread completed")

if __name__ == "__main__":
    main()