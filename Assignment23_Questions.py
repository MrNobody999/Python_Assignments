# 1: Write a Python program to implement a class named BookStore with the following specifications:

    # The class should contain two instance variables : 
        # Name (Book Name)
        # Author (Book Author)

    # The class should contain one class variable:
        # NoOfBooks (initialize it to 0)

    # Define a constructor (__init__) that accepts Name and Author and initializes instance variables.

    # Inside the constructor, increment the class variable NoOfBooks by 1 whenever a new object is created.

    # Implement an instance method:
        # Display ( ) — should display book details in the format:
            # <BookName> by <Author>. No of books: <NoOfBooks>

# Example usage:

# Obj1 = BookStore("Linux System Programming", "Robert Love")
# Objl.Display()  # Linux System Programming by Robert Love. No of books: 1

# Obj2 = BookStore("C Programming", "Dennis Ritchie")
# Obj2.Display() # C Programming by Dennis Ritchie. No of books: 2


# 2: Write a Python program to implement a class named BankAccount with the following requirements:

    # The class should contain two instance variable
        # Name (Account holder name)
        # Amount (Account balance)

    # The class should contain one class variable:
        # ROI (Rate of Interest), initialized to 10.5
    
    # Define a constructor (__init__) that accepts Name and initial Amount.

    # Implement the following instance methods:
        # Display () —displays account holder name and current balance.
        # Deposit () — accepts an amount from the user and adds it to balance.
        # Withdraw( ) — accepts an amount from the user and subtracts it from balance.
            # (Ensure withdrawal is allowed only if sufficient balance exists)
        # CalculateInterest ( ) — calculates and returns interest using formula:
            # Interest = (Amount * ROI) / 100

    # Create multiple objects and demonstrate all methods.


# 3: Write a Python program to implement a class named Numbers with the following specifications:

    # The class should contain one instance variable:
        # Value

    # Define a constructor (__init__) that accepts a number from the user and initializes Value.

    # Implement the following instance methods:
    # ChkPrime ( ) - returns True if the number is prime, otherwise returns False.
    # ChkPerfect ( ) - returns True if the number is perfect, otherwise returns False.
    # Factors () — displays all factors of the number.
    # SumFactors ( ) —retums the sum of all factors.
        # (You may use this method as a helper in ChkPerfect () if required)

    # Create multiple objects and call all methods.

