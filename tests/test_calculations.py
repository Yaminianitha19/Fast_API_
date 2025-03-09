
import pytest
from app.calculations import add, multiply, subtract, divide, BankAccount, InsufficientFunds


@pytest.fixture
def zero_bank_account():
    print("creating empty bank account")
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)

@pytest.mark.parametrize("num1, num2, expected", [(3, 5, 8), (-2, 3, 1), (12,4,16)]) 
def test_add(num1, num2, expected):
    
    
    assert add(num1, num2) == expected
 
def test_subtract():
    assert subtract(8, 5) == 4

def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(-6, 2) == -3
    
    
def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
    

def test_bank_set_initial_amount(bank_account):
    
    assert bank_account.balance == 50

def test_bank_default_amount(zero_bank_account):
    bank_account = BankAccount(50)
    assert zero_bank_account.balance == 0 
    
def test_withdraw(bank_account):
    
    bank_account.withdraw(20)
    assert bank_account.balance == 30

def test_deposit(bank_account):

    bank_account.deposit(30)
    assert bank_account.balance == 80

def test_collect_interest(bank_account):
    
    bank_account.collect_interest()
    assert round(bank_account.balance,6) == 56




@pytest.mark.parametrize("deposited, withdrew, expected", [(200, 100, 100), (50, 10, 40), (1200,200,1000)]) 
def test_bank_transaction(zero_bank_account, deposited,withdrew,expected):
    
    zero_bank_account.deposit (deposited)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance == expected 


def test_insufficient_funds(bank_account):
    
    with pytest.raises(InsufficientFunds):
         bank_account.withdraw(200)


