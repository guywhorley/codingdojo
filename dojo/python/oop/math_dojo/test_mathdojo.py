# filename: math_dojo.py
# author: guy whorley

import pytest
from mathdojo import MathDojo

num_empty = []
num_zero = [ 0,0,0,0 ]
num_posInts = [ 1, 2 ]
num_negInts = [ -1, -2 ]
num_comboInts = [ -1, 3 ]
num_positiveFloats = [ 1.25, 4.25 ]
num_negativeFloats = [ -1.25, -4.25 ]

def test_subtract_mixedLists():
    md=MathDojo().subtract(1,2,[1,2],[-1,2])
    assert(md.result == -7)

def test_add_subtract_mixedLists():
    md=MathDojo().subtract(1,2,[1,2],[-1,2]).add([1,2,3],3,4,[5,6,7])
    assert(md.result == 24)

def  test_add_emptyLists():
    md = MathDojo().add()
    assert (md.result == 0)

def  test_add_mixedLists():
    md = MathDojo().add([1,2,3],3,4,[5,6,7])
    assert (md.result == 31)

# test multiple add and subtracts
def test_chained_part1():
    md = MathDojo().add(2).add(2,5).subtract(3,2)
    assert (md.result == 4)

# test subtraction
def test_subtract_EmptyArgs():
    md = MathDojo().subtract(*num_zero)
    assert (md.result == 0)

def test_subtract_TwoInts():
    md = MathDojo().subtract(*num_posInts)
    assert (md.result == -3)

def test_subtract_TwoPositiveFloats():
    md = MathDojo().subtract(*num_positiveFloats)
    assert (md.result == -5.5)

def test_subtract_TwoNegativeFloats():
    md = MathDojo().subtract(*num_negativeFloats)
    assert (md.result == 5.5)

def test_subtract_TwoNegativeNumbers():
    md = MathDojo().subtract(*num_negInts)
    assert (md.result == 3)

def test_subtract_Zeros():
    md = MathDojo().subtract(*num_zero)
    assert (md.result == 0)

# test addition
def test_add_TwoInts():
    md = MathDojo().add(*num_posInts)
    assert ( md.result == 3)

def test_add_EmptyArgs():
    md = MathDojo().add(*num_empty)
    assert ( md.result == 0)

def test_add_TwoPositiveFloats():
    md = MathDojo().add(*num_positiveFloats)
    assert (md.result == 5.50)

def test_add_TwoNegativeFloats():
    md = MathDojo().add(*num_negativeFloats)
    assert (md.result == -5.50)

def test_add_TwoNegativeNumbers():
    md = MathDojo().add(*num_negInts)
    assert (md.result == -3)

def test_add_OnePositiveOneNegativeInt():
    md = MathDojo().add(*num_comboInts)
    assert (md.result == 2)

def test_add_Zeros():
    md = MathDojo().add(*num_zero)
    assert (md.result == 0)
