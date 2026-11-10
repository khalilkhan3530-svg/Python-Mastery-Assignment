import pytest
from part09_oop import BankAccount


# Create a fresh bank account with Rs 1000 for each test
@pytest.fixture
def account():
    return BankAccount("Ali", 1000)


# Test deposit
def test_deposit(account):
    account.deposit(500)
    assert account.balance == 1500


# Test withdrawal
def test_withdraw(account):
    account.withdraw(200)
    assert account.balance == 800


# Test transaction history
def test_history(account):
    account.deposit(500)
    account.withdraw(200)

    assert account.history == [
        "Deposited: Rs 500",
        "Withdrawn: Rs 200"
    ]


# Test negative amount error
def test_negative_amount(account):
    with pytest.raises(ValueError):
        account.deposit(-100)

    with pytest.raises(ValueError):
        account.withdraw(-100)


# Test insufficient balance error
def test_insufficient_balance(account):
    with pytest.raises(ValueError):
        account.withdraw(2000)
