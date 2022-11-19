class Account:
    """
    A class representing details for an account
    """

    def __init__(self, name: str) -> None:
        """
        Constructor to create initial state of an account object
        :param name: Name of the person tied to the account
        """
        self.__account_name = name
        self.__account_balance: float = 0

    def deposit(self, amount: float) -> bool:
        """
        Method to add an amount to an account's balance
        :param amount: Amount to be added to the account
        :return: True if the deposit was successful, False if it was unsuccessful
        """
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount: float) -> bool:
        """
        Method to remove an amount from an account's balance
        :param amount: Amount to be removed from the account
        :return: True if the withdrawal was successful, False if it was unsuccessful, or the amount was too great
        """
        if amount <= 0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        """
        Method to retrieve the balance on an account
        :return: The balance of an account
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Method to retrieve the balance on a name
        :return: The name of an account
        """
        return self.__account_name
