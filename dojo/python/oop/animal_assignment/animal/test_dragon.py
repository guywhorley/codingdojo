# filename: test_animal.py
# author: guy whorley
# description: test the Dragon class.
#
# see http://pytest.org/latest/ for information on unit-testing
#   1) Install pytest:  "pip install -U pytest"  
#   2) Install pytest-html plugin for html report: "pip install pytest-html"
#   3) Testing your class/modules/packages:
#       a. create a file with your unit test cases: "test_<someName>.py"
#       b. ensure you have imported your code into the test_case.py
#       c. create 'test cases' by defining a method with name starting with "test_<someMethodName>
#       d. at the command line in project root, run "py.test --html=report.html"[enter]. This lauches
#          pytest runner which searches for any files with name beginning with "test_" then look in that file
#          for any methods with names beginning with "test_..." and then runs them.
#       e. Once test run is complete, open up the 'report.html' in a browser to view results.


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
