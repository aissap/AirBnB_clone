#!/usr/bin/python3
"""
Unittests for user.py
"""
import unittest
from datetime import datetime
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for User class"""

    def test_user_initialization(self):
        """Test User initialization"""
        user = User(
                first_name="John",
                last_name="Doe",
                email="john@example.com",
                password="pass123"
                )
        self.assertIsInstance(user, BaseModel)
        self.assertIsInstance(user, User)
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')
        self.assertEqual(user.email, 'john@example.com')
        self.assertEqual(user.password, 'pass123')

    def test_str_representation(self):
        """Test User __str__ representation"""
        user = User()
        user.id = "113356"
        user.created_at = user.updated_at = datetime.today()
        user_str = str(user)
        self.assertIn("[User] (113356)", user_str)
        self.assertIn("'id': '113356'", user_str)
        self.assertIn("'created_at':", user_str)
        self.assertIn("'updated_at':", user_str)

    def test_to_dict_method(self):
        """Test User to_dict method"""
        user = User(
                first_name="John",
                last_name="Doe",
                email="john@example.com",
                password="pass123"
                )
        user_dict = user.to_dict()
        expected_keys = [
                'id', 'created_at', 'updated_at',
                'first_name', 'last_name', 'email', 'password'
                ]

        for key in expected_keys:
            self.assertIn(key, user_dict)

            date_format = "%Y-%m-%dT%H:%M:%S.%f"
            self.assertEqual(
                    user.created_at.strftime(date_format),
                    user_dict['created_at']
                    )
            self.assertEqual(
                    user.updated_at.strftime(date_format),
                    user_dict['updated_at']
                    )

    def test_save_method(self):
        """Test User save method"""
        user = User()
        user.save()
        self.assertNotEqual(user.created_at, user.updated_at)


if __name__ == "__main__":
    unittest.main()
