from alternate_case import *

def test_basic_hello():
    assert(alternate_case('hello') == 'HeLlO')

def test_twoword_hello():
    assert(alternate_case('hello world') == 'HeLlO wOrLd')