#!/usr/bin/python3
"""
Unittests for city.py
"""
import unittest
from datetime import datetime
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases for City class"""

    def test_instantiation(self):
        """Test City instantiation"""
        city = City(
                state_id="CB",
                name="Casa Blanca",
                created_at=datetime.now()
                )
        self.assertIsInstance(city, BaseModel)
        self.assertIsInstance(city, City)

    def test_attributes(self):
        """Test City attributes"""
        city = City()
        self.assertTrue(hasattr(city, 'id'))
        self.assertTrue(hasattr(city, 'created_at'))
        self.assertTrue(hasattr(city, 'updated_at'))
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))

    def test_attribute_types(self):
        """Test City attribute types"""
        city = City()
        self.assertIsInstance(city.id, str)
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)

    def test_city_initialization(self):
        """Test City initialization"""
        city = City(state_id="CB", name="Casa Blanca")
        self.assertEqual(city.state_id, "CB")
        self.assertEqual(city.name, "Casa Blanca")

    def test_str_representation(self):
        """Test City __str__ representation"""
        city = City()
        city.id = "113356"
        city.created_at = city.updated_at = datetime.today()
        city_str = str(city)
        self.assertIn("[City] (1133456)", city_str)
        self.assertIn("'id': '1133456'", city_str)
        self.assertIn("'created_at':", city_str)
        self.assertIn("'updated_at':", city_str)

    def test_to_dict_method(self):
        """Test City to_dict method"""
        city = City(state_id="CB", name="Casa Blanca")
        city_dict = city.to_dict()
        expected_keys = ['id', 'created_at', 'updated_at', 'state_id', 'name']

        for key in expected_keys:
            self.assertIn(key, city_dict)

        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.assertEqual(
                city.created_at.strftime(date_format),
                city_dict['created_at']
                )
        self.assertEqual(
                city.updated_at.strftime(date_format),
                city_dict['updated_at']
                )

    def test_save_method(self):
        """Test City save method"""
        city = City()
        city.save()
        self.assertNotEqual(city.created_at, city.updated_at)


if __name__ == "__main__":
    unittest.main()
