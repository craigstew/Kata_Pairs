from sum_args import *

def test_three_ints_in_list():
    assert(sum_args(5, -6, 20) == 19) 

def test_single_int():
    assert(sum_args(5) == 5)   

def test_empty_arg():
    assert(sum_args() == 0) 