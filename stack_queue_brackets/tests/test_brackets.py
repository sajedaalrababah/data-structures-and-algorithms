import pytest 
from  stack_queue_Brackets import validate_brackets

def test_validate_brackets():
    assert validate_brackets("(){}[]") == True
    assert validate_brackets("()[[Extra Characters]]") == True
    assert validate_brackets("(){}[[]]") == True
    assert validate_brackets("{}{Code}[Fellows](())") == True
    assert validate_brackets("[({}]") == False
    assert validate_brackets("(](") == False
    assert validate_brackets("{(})") == False
    assert validate_brackets("{") == False
    assert validate_brackets(")") == False
    assert validate_brackets("[}") == False
    assert validate_brackets("(]") == False
    assert validate_brackets("}{") == False
    assert validate_brackets(")(") == False
    assert validate_brackets("][") == False
    
def test_validate_brackets_empty_string():
    assert validate_brackets("") == True


def test_validate_brackets_no_brackets():
    assert validate_brackets("This is a test string") == True

def test_validate_brackets_no_brackets_with_numbers():
    assert validate_brackets("This is a test string 123") == True

def test_validate_brackets_no_brackets_with_symbols():
    assert validate_brackets("This is a test string !@#$%^&*()") == True

