# filename: test_animal.py
# author: guy whorley
# description: test the Dog class.
# 
# see http://pytest.org/latest/ for information on unit-testing
#   Install pytest:  "pip install -U pytest"  
#   Install pytest-html plugin for html report: "pip install pytest-html"

import pytest
from app_classes import Dog

# def test_raiseExc():
#     with pytest.raises(SystemExit):
#         raiseExc()

def test_dog_initUsesDefaultValues():
    d = Dog()
    assert d.name == "nonce"
    assert d.health == 150

def test_dog_initUsesAssignedName():
    d = Dog("doug")
    assert d.name == "doug"

def test_dog_petAddsFiveHealth():
    d = Dog("doug")
    # default health is 150, pet should += 5
    d.pet()
    assert d.health == 155
