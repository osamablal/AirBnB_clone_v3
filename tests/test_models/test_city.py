#!/usr/bin/python3
"""Testing of the city."""
import unittest
import os
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """
    Testing for the class city.
    """
    @classmethod
    def setUpClass(cls):
        """
        Preparing for the test.
        """
        cls.city = City()
        cls.city.name = "LA"
        cls.city.state_id = "CA"

    @classmethod
    def teardown(cls):
        """
        Tearing down finally after the test.
        """
        del cls.city

    def tearDown(self):
        """
        The Tear down.
        """
        try:
            os.remove("file.json")
        except ImportError:
            pass

    def test_checking_for_docstring_city(self):
        """
        A check for doc-string.
        """
        self.assertIsNotNone(City.__doc__)

    def test_attributes_city(self):
        """
        Testing attrebute of city.
        """
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_is_subclass_city(self):
        """
        Testing for city be sub-class base-model.
        """
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_attribute_types_city(self):
        """
        Testing city type attrebute.
        """
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == 'db', 'Not file engine')
    def test_save_city(self):
        """
        Testing for Saving.
        """
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict_city(self):
        """
        Testing for the dictionary.
        """
        self.assertEqual('to_dict' in dir(self.city), True)


if __name__ == "__main__":
    unittest.main()
