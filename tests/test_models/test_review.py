#!/usr/bin/python3
"""Testing of the review."""
import unittest
import os
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """
    Testing for the review place.
    """
    @classmethod
    def setUpClass(cls):
        """
        Preparing for the test.
        """
        cls.rev = Review()
        cls.rev.place_id = "4321-dcba"
        cls.rev.user_id = "123-bca"
        cls.rev.text = "The srongest in the Galaxy"

    @classmethod
    def teardown(cls):
        """
        Tearing down finally after the test.
        """
        del cls.rev

    def tearDown(self):
        """
        The Tear down.
        """
        try:
            os.remove("file.json")
        except ImportError:
            pass

    def test_checking_for_docstring_review(self):
        """
        A check for doc-string.
        """
        self.assertIsNotNone(Review.__doc__)

    def test_attributes_review(self):
        """
        Testing attrebute of review.
        """
        self.assertTrue('id' in self.rev.__dict__)
        self.assertTrue('created_at' in self.rev.__dict__)
        self.assertTrue('updated_at' in self.rev.__dict__)
        self.assertTrue('place_id' in self.rev.__dict__)
        self.assertTrue('text' in self.rev.__dict__)
        self.assertTrue('user_id' in self.rev.__dict__)

    def test_is_subclass_review(self):
        """
        Testing for review be sub-class base-model.
        """
        self.assertTrue(issubclass(self.rev.__class__, BaseModel), True)

    def test_attribute_types_review(self):
        """
        Testing review type attrebute.
        """
        self.assertEqual(type(self.rev.text), str)
        self.assertEqual(type(self.rev.place_id), str)
        self.assertEqual(type(self.rev.user_id), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == 'db', 'Not file engine')
    def test_save_review(self):
        """
        Testing for Saving.
        """
        self.rev.save()
        self.assertNotEqual(self.rev.created_at, self.rev.updated_at)

    def test_to_dict_review(self):
        """
        Testing for the dictionary.
        """
        self.assertEqual('to_dict' in dir(self.rev), True)


if __name__ == "__main__":
    unittest.main()
