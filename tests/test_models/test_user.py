#!/usr/bin/python3
"""
Unittests for city.py
"""
import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    def test_user_initialization(self):
        """Test User initialization"""
        user_data = {
            'first_name': 'Jordan',
            'last_name': 'Joe',
            'email': 'jordan.doe@example.com',
            'password': 'password'
        }
        user = User(**user_data)

        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')
        self.assertEqual(user.email, 'john.doe@example.com')
        self.assertEqual(user.password, 'secure_password')
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)
