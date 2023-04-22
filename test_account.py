import pytest
from account import *


class Account_Test:
    def setup_method(self):
        self.a1 = Account('Jane')

    def teardown_method(self):
        del self.a1

    def test_init(self):
        assert self.a1.get_name() == 'Jane'

    def test_deposit(self, amount):
        assert self.a1.deposit(-1.5) is False
        assert self.a1.get_balance() == 0

        assert self.a1.deposit(0) is False
        assert self.a1.get_balance() == 0

        assert self.a1.deposit(5.5) is True
        assert self.a1.get_balance() == pytest.approx(5.5, abs=.01)


'''
def test_withdraw(self):
    # negative, zero, positive invalid, positive validPass
     assert self.a1.withdraw(-1.5) is False
     assert self.a1.get_balance() == 0

     assert self.a1.withdraw(0) is False
     assert self.a1.get_balance() == 0

     assert self.a1.withdraw(-1.5) is False
     assert self.a1.get_balance() == 0

     assert self.a1.withdraw(5.5) is True
     assert self.a1.get_balance() ==
'''

