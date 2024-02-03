#!/usr/bin/python3
"""Testing of the user."""
import unittest
import os
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    Testing for the user class.
    """
    @classmethod
    def setUpClass(cls):
        """
        Preparing for the test.
        """
        cls.user = User()
        cls.user.first_name = "Kevin"
        cls.user.last_name = "Yook"
        cls.user.email = "yook00627@gmamil.com"
        cls.user.password = "secret"

    @classmethod
    def teardown(cls):
        """
        Tearing down finally after the test.
        """
        del cls.user

    def tearDown(self):
        """
        The Tear down.
        """
        try:
            os.remove("file.json")
        except ImportError:
            pass

    def test_checking_for_docstring_user(self):
        """
        A check for doc-string.
        """
        self.assertIsNotNone(User.__doc__)

    def test_attributes_user(self):
        """
        Testing attrebute of user.
        """
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)

    def test_is_subclass_user(self):
        """
        Testing for user be sub-class base-model.
        """
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def test_attribute_types_user(self):
        """
        Testing user type attrebute.
        """
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.first_name), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == 'db', 'Not file engine')
    def test_save_user(self):
        """
        Testing for Saving.
        """
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_to_dict_user(self):
        """
        Testing for the dictionary.
        """
        self.assertEqual('to_dict' in dir(self.user), True)


if __name__ == "__main__":
    unittest.main()
