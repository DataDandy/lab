import pytest
from account import *


class Test:
    def setup_method(self):
        self.a1 = Account('Jane')

    def teardown_method(self):
        del self.a1

    def test_init(self):
        assert self.a1.get_name() == 'Jane'
        assert self.a1.get_balance() == 0

    def test_deposit(self):
        assert self.a1.deposit(-1.5) is False
        assert self.a1.get_balance() == 0

        assert self.a1.deposit(0) is False
        assert self.a1.get_balance() == 0

        assert self.a1.deposit(5.5) is True
        assert self.a1.get_balance() == pytest.approx(5.5, abs=.01)



    def test_withdraw(self):
        #negative, zero, positive invalid, positive validPass
        self.a1.deposit(10.00)

        assert self.a1.withdraw(-1.5) is False
        assert self.a1.get_balance() == pytest.approx(10.00, abs=.01)

        assert self.a1.withdraw(0) is False
        assert self.a1.get_balance() == pytest.approx(10.00, abs=.01)

        assert self.a1.withdraw(15) is False
        assert self.a1.get_balance() == pytest.approx(10.00, abs=.01)

        assert self.a1.withdraw(5.5) is True
        assert self.a1.get_balance() == pytest.approx(4.50, abs=.01)


