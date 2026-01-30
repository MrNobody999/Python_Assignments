# 1: Write a Python program to implement a class named Demo with the following specifications:

    # The class should contain two instance variables: no1 and no2
    # The class should contain one class variable named Value.
    # Define a constructor (__init__) that accepts two parameters and initializes the instance variables.
    # Implement two instance methods:
        # Fun ( ) — displays the values of instance variables no1 and no2
        # Gun ( ) — displays the values of instance variables nol and no2

# Create two objects of the Demo class as follows:
# Obj1 = Demo(11, 21)
# Obj2 = Demo(51, 101)

# Call the instance methods in the given sequence:
# Obj1.Fun()
# Obj2.Fun()
# Obj1.Gun()
# Obj2.Gun()


class Demo : 
    Value = 100

    def __init__(self, num1, num2):
        self.no1 = num1
        self.no2 = num2 

    def Fun(self):
        print(f"Inside Fun method:")
        print(f"Value of no1: {self.no1}")
        print(f"Value of no2: {self.no2}")

    def Gun(self):
        print(f"Inside Gun method:")
        print(f"Value of no1: {self.no1}")
        print(f"Value of no2: {self.no2}")

obj1 = Demo(11,21)

print("Accessing class variable value : ", Demo.Value)

obj1.Gun()

Obj1 = Demo(11, 21)
Obj2 = Demo(51, 101)

Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()