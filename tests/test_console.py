#!/usr/bin/python3

from datetime import datetime
import unittest
from unittest.mock import patch
import io
import os
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_help(self, mock_stdout):
        with patch('builtins.input', side_effect=['help', 'quit']):
            self.console.cmdloop()
        output = mock_stdout.getvalue()
        self.assertIn("Documented commands (type help <topic>):", output)
        self.assertIn("EOF  help  quit", output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_quit(self, mock_stdout):
        with patch('builtins.input', return_value='quit'):
            self.assertTrue(self.console.onecmd('quit'))
        output = mock_stdout.getvalue()
        self.assertEqual(output, '')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_create(self, mock_stdout):
        with patch('builtins.input', return_value='create BaseModel'):
            self.console.onecmd('create BaseModel')
        output = mock_stdout.getvalue()
        self.assertRegex(output, r"\w{8}-\w{4}-\w{4}-\w{4}-\w{12}")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show(self, mock_stdout):
        with patch('builtins.input', return_value='show BaseModel'):
            self.console.onecmd('show BaseModel')
        output = mock_stdout.getvalue()
        self.assertIn("** instance id missing **", output)


if __name__ == '__main__':
    unittest.main()
