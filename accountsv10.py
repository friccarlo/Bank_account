# Fric Carlo Joseph Benedict
# 201720702

# Importing random and datetime to use it in code below
import random
import datetime

# Creating Class for Basic Account
class BasicAccount:
    """ The BasicAccount class is a Python class that represents a basic bank account, with attributes for
    account name, balance, account number, card number, and card expiration date. """
    # Initializing the count which will be used to count the account numbers
    count = 0
    def __init__(self, ac_name, opening_balance: float):
        """
        The above function is the constructor for a BasicAccount class in Python, which initializes the
        account name, opening balance, account number, card number, and card expiration date.
        
        :param ac_name: The ac_name parameter is used to store the name of the account holder
        :param opening_balance: The `opening_balance` parameter is a float that represents the initial
        balance of the account. It is used to set the `balance` attribute of the account object
        :type opening_balance: float
        """
        self.ac_name = ac_name
        self.balance = opening_balance
        self.ac_num = BasicAccount.count
        self.ac_num += 1
        BasicAccount.count = self.ac_num
        self.card_num = ''
        self.card_exp = ()

    def __str__(self):
        """
        The function returns a string representation of an object, including the name and opening balance.
        :return: The method `__str__(self)` is returning a formatted string that includes the name and
        opening balance of an account.
        """
        return 'Name:{}\nOpening Balance: £{:.2f}'.format(self.ac_name, self.balance)


    def deposit(self, amount: float):
        """
        The `deposit` function adds a positive amount to the balance of an account.

        :param amount: The amount parameter is a float that represents the amount of money to be deposited
        into the account
        :type amount: float
        """
        if amount <= 0:
            print("Error! Negative balance in the account")
        else:
            self.balance += amount

    def withdraw(self, amount: float):
        """
        The function withdraws a specified amount from an account balance and updates the balance
        accordingly, while also printing relevant messages.

        :param amount: The amount parameter is the amount of money that the user wants to withdraw from
        their account
        :type amount: float
        Converting the numbers into pence and then back to float
        """
        amount = int(amount*100)
        self.balance = int(self.balance*100)
        if amount <= 0 or amount > self.balance:
            amount = float(amount/100)
            self.balance = (self.balance/100)
            print(f"Can not withdraw £{amount}")
        else:
            amount = (amount/100)
            self.balance = (self.balance/100)
            self.balance-=amount
            print(f"{self.ac_name} has withdrawn £{amount}. New balance is £{self.balance:.2f}")

    def get_available_balance(self):
        """
        The function `get_available_balance` returns the current balance.
        :return: The available balance of the account.
        """
        return self.balance

    def get_balance(self):
        """
        The function `get_balance` returns the balance of an object.
        :return: The balance of the object.
        """
        return self.balance

    def print_balance(self):
        """
        The function `print_balance` prints the current balance with a currency symbol.
        """
        print(f"Your balance is: £{self.balance:.2f}")

    def get_name(self):
        """
        The function `get_name` returns the value of the attribute `ac_name`.
        :return: The method is returning the value of the attribute `ac_name`.
        """
        return self.ac_name

    def get_ac_num(self):
        """
        The function `get_ac_num` returns the account number as a string.
        :return: The method is returning the account number as a string.
        """
        return str(self.ac_num)

    def issue_new_card(self):
        """
        The function `issue_new_card` generates a random card number and sets the card expiration date to
        three years from the current month.
        """
        self.card_num = random.randint(10**15, 10**16-1)
        today_date = datetime.datetime.now().date()
        month= today_date.month
        year = int(today_date.strftime("%y"))
        Today_tuple = (month, year)
        self.card_exp = (month, Today_tuple[1]+ 3)

    def close_account(self):
        """
        The function "close_account" checks if the balance is greater than zero, withdraws the balance if it
        is, and returns True if the account is successfully closed.
        :return: a boolean value. If the balance is greater than 0, it will withdraw the balance and return
        True. If the balance is 0, it will return True. If the balance is negative, it will return False.
        """
        if self.balance>0:
            self.withdraw(self.balance)
            return True
        elif self.balance == 0:
            return True
        else:
            return False

# Creating Class for Premium Account and inheriting Basic Account
class PremiumAccount(BasicAccount):
    """The `PremiumAccount` class is a subclass of `BasicAccount` that adds an initial overdraft limit to
    the account.
    """
    def __init__(self, ac_name, opening_balance: float, initial_overdraft: float = 0):
        """
        The above function is a constructor for a class that initializes the account name, opening balance,
        overdraft limit, and overdraft status.
        
        :param ac_name: The `ac_name` parameter is a string that represents the name of the account. It is
        used to identify the account
        :param opening_balance: The `opening_balance` parameter is a float that represents the initial
        balance of the account. It is the amount of money that is available in the account when it is first
        created
        :type opening_balance: float
        :param initial_overdraft: The initial_overdraft parameter is an optional parameter that represents
        the initial overdraft limit for the account. If no value is provided for this parameter, it defaults
        to 0
        : type overdraft: boolean
        It is initially set to False. If initial overdraft is greater than 0 then overdraft becomes True or 
        else stays false
        """
        super().__init__(ac_name, opening_balance)
        self.overdraft_limit = initial_overdraft
        self.overdraft = False
        self.overdraft = initial_overdraft != 0


    def set_overdraft_limit(self, new_limit: float):
        """
        The function sets a new overdraft limit and returns the updated limit.
        
        :param new_limit: The new_limit parameter is a float that represents the new value for the overdraft
        limit
        :type new_limit: float
        :return: The method is returning the value of the `overdraft_limit` attribute after it has been
        updated with the new limit.
        """
        self.overdraft_limit = new_limit
        return self.overdraft_limit

    def __str__(self):
        """
        The function returns a string representation of an account holder's name, account balance, and
        overdraft limit.
        :return: The `__str__` method is returning a formatted string that includes the account holder's
        name, account opening balance, and overdraft limit.
        """
        return f'Account Holder Name: {self.ac_name}\nAccount Opening Balance: £{self.balance}\nOverdraft Limit:{self.overdraft_limit}'

    def get_available_balance(self):
        """
        The function returns the available balance by adding the current balance and the overdraft limit.
        :return: the sum of the current balance and the overdraft limit.
        """
        return self.balance + self.overdraft_limit

    def withdraw(self, amount: float):
        """
        The function `withdraw` allows a user to withdraw a specified amount from their account, updating
        the balance accordingly.
        
        :param amount: The `amount` parameter represents the amount of money that the user wants to withdraw
        from their account. It is of type `float`, which means it can be a decimal number
        :type amount: float
        Converting the numbers into pence and then back to float
        """
        amount = int(amount*100)
        self.balance = int(self.balance*100)
        self.overdraft_limit = int(self.overdraft_limit*100)

        if amount<=0 or amount>(self.balance + self.overdraft_limit):
            amount = (amount/100)
            self.balance = (self.balance/100)
            self.overdraft_limit = (self.overdraft_limit/100)
            print(f"Can not withdraw £{amount}")
        else:
            self.balance-=amount
            amount = (amount/100)
            self.balance = (self.balance/100)
            self.overdraft_limit = (self.overdraft_limit/100)
            print(f"{self.ac_name} has withdrawn £{amount}. New balance is £{self.balance:.2f}")

    def print_balance(self):
        """
        The function `print_balance` prints the actual balance and the overdraft limit and remaining overdraft money.
        """

        print(f"Your Actual balance: {self.balance:.2f}")
        if self.balance <= 0:
            print('Overdraft limit is: £', self.overdraft_limit)
            print('Overdraft remaining is: £', self.balance + self.overdraft_limit)
        else:
            print('Overdraft limit is: £', self.overdraft_limit)
            print('Overdraft remaining is: £', self.overdraft_limit)

    def close_account(self):
        """
        The `close_account` function checks if the balance is negative, and if so, it prints a message and
        returns False; if the balance is zero, it sets the balance and overdraft limit to zero and returns
        True; otherwise, it withdraws the entire balance, sets the balance and overdraft limit to zero, and
        returns True.
        :return: The close_account method returns a boolean value. It returns True if the account is
        successfully closed, and False if the account cannot be closed due to the customer being overdrawn.
        """
        if self.balance < 0:
            print(f"Can not close account due to customer being overdrawn by £{abs(self.balance)}")
            return False
        elif self.balance == 0:
            self.overdraft_limit = 0.0
            return True
        else:
            self.withdraw(self.balance)
            self.overdraft_limit = 0.0
            return True

A= PremiumAccount('A', 10, 2)
A.withdraw(12)
A.close_account()