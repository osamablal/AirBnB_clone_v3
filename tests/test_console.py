#!/usr/bin/python3
"""testing the primary console."""
import unittest
from unittest.mock import patch
from io import StringIO
import os
import console
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test of the console."""

    @classmethod
    def setUpClass(cls):
        """Setting up for test."""
        cls.consol = HBNBCommand()

    @classmethod
    def teardown(cls):
        """Finally after test."""
        del cls.consol

    def tearDown(self):
        """Deleting temperory files."""
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            try:
                os.remove("file.json")
            except ImportError:
                pass

    def test_docstrings_in_console(self):
        """A check for doc-strings."""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)
        self.assertIsNotNone(HBNBCommand.help_count.__doc__)

    def test_emptyline(self):
        """the testing of empty-line."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("\n")
            self.assertEqual('', f.getvalue())


if __name__ == "__main__":
    unittest.main()
