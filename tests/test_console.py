#!/usr/bin/python3
"""
Unittests for console.py
"""
import unittest
from unittest.mock import patch
import io
import sys
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test cases for the console.py file"""

    @classmethod
    def setUpClass(cls):
        """Set up for the test"""
        cls.console_output = io.StringIO()
        sys.stdout = cls.console_output

    @classmethod
    def tearDownClass(cls):
        """Clean up after the test"""
        sys.stdout = sys.__stdout__

    def setUp(self):
        """Reset the console output for each test"""
        self.console_output.seek(0)
        self.console_output.truncate()

    @patch('sys.stdin', io.StringIO('create BaseModel\n'))
    def test_create(self):
        """Test create command"""
        HBNBCommand().cmdloop()
        self.assertIn("BaseModel", self.console_output.getvalue())

    @patch('sys.stdin', io.StringIO('show BaseModel\n'))
    def test_show_missing_instance_id(self):
        """Test show command with missing instance id"""
        HBNBCommand().cmdloop()
        self.assertIn("** instance id missing **", self.console_output.getvalue())

    @patch('sys.stdin', io.StringIO('show BaseModel 123\n'))
    def test_show_instance_not_found(self):
        """Test show command with instance not found"""
        HBNBCommand().cmdloop()
        self.assertIn("** no instance found **", self.console_output.getvalue())

    @patch('sys.stdin', io.StringIO('destroy BaseModel\n'))
    def test_destroy_missing_instance_id(self):
        """Test destroy command with missing instance id"""
        HBNBCommand().cmdloop()
        self.assertIn("** instance id missing **", self.console_output.getvalue())

    @patch('sys.stdin', io.StringIO('destroy BaseModel 123\n'))
    def test_destroy_instance_not_found(self):
        """Test destroy command with instance not found"""
        HBNBCommand().cmdloop()
        self.assertIn("** no instance found **", self.console_output.getvalue())

    @patch('sys.stdin', io.StringIO('all\n'))
    def test_all(self):
        """Test all command"""
        HBNBCommand().cmdloop()
        self.assertIn("BaseModel", self.console_output.getvalue())

    @patch('sys.stdin', io.StringIO('count\n'))
    def test_count(self):
        """Test count command"""
        HBNBCommand().cmdloop()
        self.assertIn("0", self.console_output.getvalue())

    @patch('sys.stdin', io.StringIO('update BaseModel\n'))
    def test_update_missing_instance_id(self):
        """Test update command with missing instance id"""
        HBNBCommand().cmdloop()
        self.assertIn("** instance id missing **", self.console_output.getvalue())

    @patch('sys.stdin', io.StringIO('update BaseModel 123\n'))
    def test_update_missing_attribute_name(self):
        """Test update command with missing attribute name"""
        HBNBCommand().cmdloop()
        self.assertIn("** attribute name missing **", self.console_output.getvalue())

    @patch('sys.stdin', io.StringIO('update BaseModel 123 name\n'))
    def test_update_missing_attribute_value(self):
        """Test update command with missing attribute value"""
        HBNBCommand().cmdloop()
        self.assertIn("** value missing **", self.console_output.getvalue())

    @patch('sys.stdin', io.StringIO('update BaseModel 123 name "John"\n'))
    def test_update(self):
        """Test update command"""
        HBNBCommand().cmdloop()
        self.assertIn("John", self.console_output.getvalue())


if __name__ == "__main__":
    unittest.main()
