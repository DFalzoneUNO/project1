from typing import Literal


class Account:
    def __init__(self, name, balance=0):
        self._account_name = name
        self.set_balance(balance)

    def _alter_balance(self, amount, alteration_type: Literal["withdraw"] | Literal["deposit"]) -> bool:
        if amount <= 0:
            return False
        else:
            match alteration_type:
                case "withdraw":
                    self._account_balance -= amount
                case "deposit":
                    self._account_balance += amount
            return True

    def deposit(self, amount) -> bool:
        return self._alter_balance(amount, "deposit")
    
    def withdraw(self, amount) -> bool:
        return self._alter_balance(amount, "withdraw")

    def get_balance(self) -> int | float:
        return self._account_balance

    def set_balance(self, value):
        if type(value) not in [int, float]:
            raise ValueError("Balance must be a number!")
        self._account_balance = 0.0 if value < 0 else float(value)

    def get_name(self) -> str:
        return self._account_name

    def set_name(self, value):
        if type(value) is str:
            self._account_name = value

    def __str__(self):
        return f"Account name = {self._account_name}, Account balance = {self._account_balance:.2f}"


class SavingAccount(Account):
    """This class adds two new features to the Account class: an account balance minimum and an interest rate.
    Because there are no overdraft fees, and because the interest rate is the same for all accounts, this class
    is only suitable for savings accounts at the People's Egalitarian Credit Union.
    """
    _MINIMUM = 100
    _RATE = 0.02

    def __init__(self, name):
        super().__init__(name, SavingAccount._MINIMUM)
        self._deposit_count = 0

    def apply_interest(self):
        if self._deposit_count % 5 == 0:
            self._account_balance *= 1 + SavingAccount._RATE

    def deposit(self, amount) -> bool:
        did_succeed = super().deposit(amount)
        if did_succeed:
            self._deposit_count += 1
            self.apply_interest()
        return did_succeed

    def withdraw(self, amount) -> bool:
        if self._account_balance - amount < SavingAccount._MINIMUM:
            return False
        else:
            return super().withdraw(amount)

    def set_balance(self, value):
        if value < SavingAccount._MINIMUM:
            super().set_balance(SavingAccount._MINIMUM)
        else:
            super().set_balance(value)

    def __str__(self):
        return f"SAVING ACCOUNT: {super().__str__()}"
