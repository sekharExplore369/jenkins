from utils import reverse_string

def test_reverse_string_basic():
    assert reverse_string("abc") == "cba"

def test_reverse_string_single_char():
    assert reverse_string("a") == "a"

def test_reverse_string_empty():
    assert reverse_string("") == ""

def test_reverse_string_palindrome():
    assert reverse_string("madam") == "madam"
