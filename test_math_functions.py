from math_functions import *

def testAdd():
    output = add_numbers(2,4)
    assert output == 6

def testSub():
    output = subtract_numbers(2,4)
    assert output == -2

def testMult():
    output = multiply_numbers(2,4)
    assert output == 8

def testMultFail():
    output = multiply_numbers(4,4)
    assert output == 16

def testDiv():
    output = divide_numbers(10,2)
    assert output == 5

def test1():
    output = square_numbers(2, 4)
    assert output == 20

def test2():
    output = twoab_numbers(2, 4)
    assert output == 12
