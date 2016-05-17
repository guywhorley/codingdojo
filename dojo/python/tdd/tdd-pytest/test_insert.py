from insert_value import insert_value_at
import pytest

class InsertValueTest:

    def setUp(self):
        self.source = [0,1,2,3,4]
        self.oracle = [0,1,100,2,3,4]
        self.result = insert_value_at(2, self.source, 100)
        self.invalidIndex = insert_value_at(-8,self.source,100)

    def test_InsertAtIndexTwo(self):
        self.assertEqual(self.oracle, self.result)

    def test_ReturnFalseForInvalidIndex(self):
        self.assertEqual(False, self.invalidIndex)
