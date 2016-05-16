# filename: test_animal.py
# author: guy whorley
# description: test the animal class.
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
from app_classes import Animal

# def test_raiseExc():
#     with pytest.raises(SystemExit):
#         raiseExc()

def test_animal_initUsesDefaultValues():
    a = Animal()
    assert a.name == "nonce"
    assert a.health == 100

def test_animal_initUsesAssignedName():
    a = Animal("bob")
    assert a.name == 'bob'

def test_animal_dropHealthDecrementsOk():
    a = Animal("bob")
    a.__dropHealth__("run",1)
    assert a.health == 99

def test_animal_dropHealthDoesNotGoBelowZero():
    a = Animal("bob")
    a.__dropHealth__("run",99)
    a.__dropHealth__("run",2)
    assert a.health != -1
    assert a.health == 1

def test_animal_walkReducesHealthByOne():
    a = Animal("bob")
    a.walk()
    assert a.health == 99

def test_animal_runReducesHealthByFive():
    a = Animal("bob")
    a.run()
    assert a.health == 95

def test_animal_displayHealthShowsCorrectInfo():
    a = Animal("bob")
    a.run()
    a.walk()
    assert a.displayHealth() == "name:bob, health:94"
