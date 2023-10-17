#!/usr/bin/python3
"""testing the console methods"""
import unittest
import os
import sys
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBCommand(unittest.TestCase):
    """tests the console"""
    def test_prompt(self):
        """test the string passed as the prompt"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    """testing the empty line function"""
    def test_empty_line(self):
        """tests whether the empty line + enter return nothing"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())


"""a class to test exit functions from the console"""


class TestExitFunctions(unittest.TestCase):
    """tests the functionality of the EOF and quit"""
    def test_quit(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))


"""a class to test do_create"""


class TestCreate(unittest.TestCase):
    """tests the create function"""
    def test_create_missing_class(self):
        right = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(right, output.getvalue().strip())

    """testing a class that does not exist"""
    def test_no_such_class(self):
        right = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create MyModel"))
            self.assertEqual(right, output.getvalue().strip())


"""class to test the show function"""


class TestShow(unittest.TestCase):
    """test the show function"""
    def test_show_missing_class(self):
        right = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(right, output.getvalue().strip())
        """with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".show()"))
            self.assertEqual(right, output.getvalue().strip())"""

    """test invalid classes"""
    def test_no_such_class(self):
        right = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show MyModel"))
            self.assertEqual(right, output.getvalue().strip())
        """with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.show()"))
            self.assertEqual(right, output.getvalue().strip())"""

    """testing a class with a missing id"""
    def test_mssing_id(self):
        right = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel"))
            self.assertEqual(right, output.getvalue().strip())

    """testing an instance that doesn't exist but has a class name"""
    def test_missing_class_name(self):
        right = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel 121212"))
            self.assertEqual(right, output.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
