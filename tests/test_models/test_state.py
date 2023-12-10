#!/usr/bin/python3
"""
Unittests for state.py
"""
import unittest
from datetime import datetime
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test cases for State class"""

    def test_instantiation(self):
        """Test State instantiation"""
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertIsInstance(state, State)

    def test_attributes(self):
        """Test State attributes"""
        state = State()
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))
        self.assertTrue(hasattr(state, 'name'))

    def test_attribute_types(self):
        """Test State attribute types"""
        state = State()
        self.assertIsInstance(state.id, str)
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)
        self.assertIsInstance(state.name, str)

    def test_state_initialization(self):
        """Test State initialization"""
        state = State(name="California")
        self.assertEqual(state.name, "California")

    def test_str_representation(self):
        """Test State __str__ representation"""
        state = State()
        state.id = "123456"
        state.created_at = state.updated_at = datetime.today()
        state_str = str(state)
        self.assertIn("[State] (123456)", state_str)
        self.assertIn("'id': '123456'", state_str)
        self.assertIn("'created_at':", state_str)
        self.assertIn("'updated_at':", state_str)

    def test_to_dict_method(self):
        """Test State to_dict method"""
        state = State()
        state_dict = state.to_dict()
        self.assertEqual(dict, type(state_dict))
        self.assertIn('id', state_dict)
        self.assertIn('created_at', state_dict)
        self.assertIn('updated_at', state_dict)
        self.assertIn('name', state_dict)
        self.assertIn('__class__', state_dict)

    def test_save_method(self):
        """Test State save method"""
        state = State()
        state.save()
        self.assertNotEqual(state.created_at, state.updated_at)


if __name__ == "__main__":
    unittest.main()
