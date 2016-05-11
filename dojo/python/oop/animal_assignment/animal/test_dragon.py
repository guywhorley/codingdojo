# filename: test_animal.py
# author: guy whorley
# description: test the Dragon class.
# 
# see http://pytest.org/latest/ for information on unit-testing
#   Install pytest:  "pip install -U pytest"  
#   Install pytest-html plugin for html report: "pip install pytest-html"

import pytest
from app_classes import Dragon

# def test_raiseExc():
#     with pytest.raises(SystemExit):
#         raiseExc()

def test_dragon_initUsesDefaultValues():
    dg = Dragon()
    assert dg.name == "nonce"
    assert dg.health == 170

def test_dragon_initUsersAssignedName():
    dg = Dragon("Eragon")
    assert dg.name == "Eragon"

def test_dragon_flyReducesHealthByTen():
    dg = Dragon()
    dg.fly()
    assert dg.health == 160

def test_dragon_displayHealthIsCorrect():
    dg = Dragon()
    assert "This is a dragon! name:nonce, health:170" == dg.displayHealth()
