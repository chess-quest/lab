import pytest
from Account import *


class Test:
    def setup_method(self):
        self.account_1 = Account('Sandwich')
        self.account_2 = Account('Hotdog')
        self.account_3 = Account('Pizza')
        self.account_1.deposit(100)
        self.account_2.deposit(100)

    def teardown_method(self):
        del self.account_1
        del self.account_2
        del self.account_3

    def test_init(self):
        assert self.account_1.get_name() == 'Sandwich'
        assert self.account_1.get_balance() == 100
        assert self.account_2.get_name() == 'Hotdog'
        assert self.account_2.get_balance() == 100
        assert self.account_3.get_name() == 'Pizza'
        assert self.account_3.get_balance() == 0

    def test_deposit(self):
        assert self.account_2.deposit(100) is True
        assert self.account_2.deposit(0) is False
        assert self.account_2.deposit(-5) is False
        assert self.account_2.get_balance() == 200

    def test_withdrawal(self):
        assert self.account_1.withdraw(50) is True
        assert self.account_1.get_balance() == 50
        assert self.account_1.withdraw(0) is False
        assert self.account_1.withdraw(100) is False
        assert self.account_1.withdraw(-50) is False
