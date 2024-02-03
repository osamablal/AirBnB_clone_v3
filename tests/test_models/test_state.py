#!/usr/bin/python3
"""Testing of the state."""
import unittest
import os
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """
    Testing for the state place.
    """
    @classmethod
    def setUpClass(cls):
        """
        Preparing for the test.
        """
        cls.state = State()
        cls.state.name = "CA"

    @classmethod
    def teardown(cls):
        """
        Tearing down finally after the test.
        """
        del cls.state

    def tearDown(self):
        """
        The Tear down.
        """
        try:
            os.remove("file.json")
        except ImportError:
            pass

    def test_checking_for_docstring_state(self):
        """
        A check for doc-string.
        """
        self.assertIsNotNone(State.__doc__)

    def test_attributes_state(self):
        """
        Testing attrebute of state.
        """
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        self.assertTrue('name' in self.state.__dict__)

    def test_is_subclass_state(self):
        """
        Testing for state be sub-class base-model.
        """
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_attribute_types_state(self):
        """
        Testing state type attrebute.
        """
        self.assertEqual(type(self.state.name), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == 'db', 'Not file engine')
    def test_save_state(self):
        """
        Testing for Saving.
        """
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict_state(self):
        """
        Testing for the dictionary.
        """
        self.assertEqual('to_dict' in dir(self.state), True)


if __name__ == "__main__":
    unittest.main()
