#!/usr/bin/python3
"""Testing of the base model."""
import unittest
import os
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Testing for the class base model.
    """
    @classmethod
    def setUpClass(cls):
        """
        Preparing for the test.
        """
        cls.base = BaseModel()
        cls.base.name = "Kev"
        cls.base.num = 20

    @classmethod
    def teardown(cls):
        """
        Tearing down finally after the test.
        """
        del cls.base

    def tearDown(self):
        """
        The Tear down.
        """
        try:
            os.remove("file.json")
        except ImportError:
            pass

    def test_checking_for_docstring_basemodel(self):
        """
        A check for doc-string.
        """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_method_basemodel(self):
        """
        A check for Base-model methods.
        """
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init_basemodel(self):
        """
        Testing for the base-model type.
        """
        self.assertTrue(isinstance(self.base, BaseModel))

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == 'db', 'Not file engine')
    def test_save_basemodel(self):
        """
        Testing for Saving.
        """
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_to_dict_basemodel(self):
        """
        Testing for the dictionary.
        """
        base_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
