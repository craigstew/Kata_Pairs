from max_and_min import *

def test_find_max_normal_ints():
    assert (nc_max([3, 7, 2, 9, 4]) == 9) 

def test_find_min_normal_ints():
    assert (nc_min([3, 7, 2, 9, 4]) == 2) 

def test_empty_list():
    assert (nc_min([]) == 0)