from sum_digits import *

def test_empty_input():

     assert(sum_digits("") == 0)

def test_single_digit():
    
    assert(sum_digits(1) == 1)

def test_longer_input_with_decimal():

    assert(sum_digits(13.62) == 12)

def test_starting_with_minus_sign():

    assert(sum_digits(-245.12) == 14)