from is_leap_year import *

def test_true_case():
    assert(is_leap_year(2024) == True)

def test_false_case():
    assert(is_leap_year(1900) == False)

def test_case_year_two_thousand():
    assert(is_leap_year(2000) == True)