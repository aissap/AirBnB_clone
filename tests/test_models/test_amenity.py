#!/usr/bin/python3
"""
Unittests for amenity.py
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class"""

    def test_instantiation(self):
        """Test Amenity instantiation"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertIsInstance(amenity, Amenity)

    def test_attributes(self):
        """Test Amenity attributes"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))
        self.assertTrue(hasattr(amenity, 'amenity'))

    def test_attribute_types(self):
        """Test Amenity attribute types"""
        amenity = Amenity()
        self.assertIsInstance(amenity.id, str)
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)
        self.assertIsInstance(amenity.amenity, str)

    def test_amenity_initialization(self):
        """Test Amenity initialization"""
        amenity = Amenity(amenity="WiFi")
        self.assertEqual(amenity.amenity, "WiFi")

    def test_str_representation(self):
        """Test Amenity __str__ representation"""
        amenity = Amenity()
        amenity.id = "123456"
        amenity.created_at = amenity.updated_at = datetime.today()
        amenity_str = str(amenity)
        self.assertIn("[Amenity] (123456)", amenity_str)
        self.assertIn("'id': '123456'", amenity_str)
        self.assertIn("'created_at':", amenity_str)
        self.assertIn("'updated_at':", amenity_str)

    def test_to_dict_method(self):
        """Test Amenity to_dict method"""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertEqual(dict, type(amenity_dict))
        self.assertIn('id', amenity_dict)
        self.assertIn('created_at', amenity_dict)
        self.assertIn('updated_at', amenity_dict)
        self.assertIn('__class__', amenity_dict)

    def test_save_method(self):
        """Test Amenity save method"""
        amenity = Amenity()
        amenity.save()
        self.assertNotEqual(amenity.created_at, amenity.updated_at)


if __name__ == "__main__":
    unittest.main()
