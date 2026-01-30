# Write a Python program to implement a class named BankAccount with the following requirements:

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



class BankAccount : 
    ROI = 10.5

    def __init__(self, name, initial_amount):
        self.Name = name
        self.Amount = initial_amount
        print(f"Account created for {self.Name} with initial balance of {self.Amount:.2f}.")

    def Display(self):
        print(f"\n--- Account Details ---")
        print(f"Account Holder: {self.Name}")
        print(f"Current Balance: {self.Amount:.2f}")
        print(f"-----------------------")


    def Deposit(self):
        deposit_amount = float(input(f"Enter deposit amount for {self.Name}: "))
        if deposit_amount > 0:
            self.Amount += deposit_amount
            print(f"Deposited {deposit_amount:.2f}.")
        else:
            print("Deposit amount must be positive.")

        self.Display()

    def Withdraw(self):
        withdrawal_amount = float(input(f"Enter withdrawal amount for {self.Name}: "))
        if withdrawal_amount > 0:
            if self.Amount >= withdrawal_amount:
                self.Amount -= withdrawal_amount
                print(f"Withdrew {withdrawal_amount:.2f}.")
            else:
                print(f"Insufficient funds. Cannot withdraw {withdrawal_amount:.2f}.")
        else:
                print("Withdrawal amount must be positive.")
        self.Display()

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest


account1 = BankAccount("Bhavik", 1000)
account2 = BankAccount("Prashant", 500)

print("Account 1 (Bhavik)")
account1.Display()
account1.Deposit()
account1.Withdraw()
account1.Withdraw()

interest1 = account1.CalculateInterest()
print(f"Calculated interest for Bhavik: ${interest1:.2f}")

print("Account 2 (Prashant) ")
account2.Display()


