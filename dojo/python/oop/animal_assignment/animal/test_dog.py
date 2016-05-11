# filename: test_animal.py
# author: guy whorley
# description: test the Dog class.
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
