#!/usr/bin/python3
"""Testing for the amenity."""
import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    Testing for the class amenity.
    """

    @classmethod
    def setUpClass(cls):
        """
        Preparing for the test.
        """
        cls.amenity = Amenity()
        cls.amenity.name = "WiFi"

    @classmethod
    def teardown(cls):
        """
        Tearing down finally after the test.
        """
        del cls.amenity

    def tearDown(self):
        """
        The Tear down.
        """
        try:
            os.remove("file.json")
        except ImportError:
            pass

    def test_checking_for_docstring_amenity(self):
        """
        A check for doc-string.
        """
        self.assertIsNotNone(Amenity.__doc__)

    def test_attributes_amenity(self):
        """
        A check for amenity for attebutes.
        """
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    def test_is_subclass_amenity(self):
        """
        Testing for amenity be sub-class base-model.
        """
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_attribute_types_amenity(self):
        """
        Testing attrebute of amenity.
        """
        self.assertEqual(type(self.amenity.name), str)

    def test_save_amenity(self):
        """
        Testing for Saving.
        """
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_to_dict_amenity(self):
        """
        Testing for the dictionary.
        """
        self.assertEqual('to_dict' in dir(self.amenity), True)


if __name__ == "__main__":
    unittest.main()
