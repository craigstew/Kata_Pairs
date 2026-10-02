from are_ordered import *

def test_ordered_list():
    assert(are_ordered([1,2,3,4]) == True)

def test_unordered_list():
    assert(are_ordered([1, 5, 2, 8]) == False)

def test_ordered_list_with_negative_number():
    assert(are_ordered([-1, 2, 3, 4]) == True)

def test_empty_list():
    assert(are_ordered([]) == False)