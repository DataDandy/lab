class Account:
    def __init__(self, name: str) -> None:
        """Function to set up the account class. The balance of the account starts at 0
        :param name: Account name
        """
        self.__name = name
        self.__balance = 0

    def deposit(self, amount: float) -> bool:
        """Function to add a designated amount to the account class. When a positive value is given, it will be
        added to the balance and the function will return True. If a number less than or equal to zero is given, the
        function will return False and will not add anything to the balance.
        :param amount: The amount the user will deposit into the account
        :return: Boolean
        """
        amount = float(amount)
        if amount > 0:
            self.__balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """Function to subtract a designated amount from the account class. When a positive value is given it will be
        subtracted from the balance and the function will return True. If a number less than or equal to zero is given,
        the function will return False and will not do anything to the balance. If the value given is greater than the
        balance, nothing will happen and the function will return False.
        :param amount: The amount the user will withdraw from the account
        :return: Boolean
        """
        amount = float(amount)
        if amount <= 0 or amount > self.__balance:
            return False
        else:
            self.__balance -= amount
            return True

    def get_balance(self) -> float:
        """Function to retrieve the current account balance.
        :return: Float
        """
        return self.__balance

    def get_name(self) -> str:
        """Function to retrieve the name associated with the account.
        :return: String
        """
        return self.__name
