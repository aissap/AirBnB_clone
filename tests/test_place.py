#!/usr/bin/python3
"""
Unittests for place.py
"""
import unittest
from datetime import datetime
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test cases for Place class"""

    def test_instantiation(self):
        """Test Place instantiation"""
        place = Place()
        self.assertIsInstance(place, BaseModel)
        self.assertIsInstance(place, Place)

    def test_attributes(self):
        """Test Place attributes"""
        place = Place()
        self.assertTrue(hasattr(place, 'id'))
        self.assertTrue(hasattr(place, 'created_at'))
        self.assertTrue(hasattr(place, 'updated_at'))
        self.assertTrue(hasattr(place, 'city'))
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertTrue(hasattr(place, 'name'))
        self.assertTrue(hasattr(place, 'description'))
        self.assertTrue(hasattr(place, 'number_of_rooms'))
        self.assertTrue(hasattr(place, 'number_of_bathrooms'))
        self.assertTrue(hasattr(place, 'maximum_guests'))
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertTrue(hasattr(place, 'lat'))
        self.assertTrue(hasattr(place, 'lon'))
        self.assertTrue(hasattr(place, 'amenity_ids'))

    def test_attribute_types(self):
        """Test Place attribute types"""
        place = Place()
        self.assertIsInstance(place.id, str)
        self.assertIsInstance(place.created_at, datetime)
        self.assertIsInstance(place.updated_at, datetime)
        self.assertIsInstance(place.city, str)
        self.assertIsInstance(place.user_id, str)
        self.assertIsInstance(place.name, str)
        self.assertIsInstance(place.description, str)
        self.assertIsInstance(place.number_of_rooms, int)
        self.assertIsInstance(place.number_of_bathrooms, int)
        self.assertIsInstance(place.maximum_guests, int)
        self.assertIsInstance(place.price_by_night, int)
        self.assertIsInstance(place.lat, float)
        self.assertIsInstance(place.lon, float)
        self.assertIsInstance(place.amenity_ids, list)

    def test_place_initialization(self):
        """Test Place initialization"""
        place = Place(city="Casa Blanca", user_id="123", name="Cozy Apartment")
        self.assertEqual(place.city, "Casa Blanca")
        self.assertEqual(place.user_id, "123")
        self.assertEqual(place.name, "Cozy Apartment")

    def test_str_representation(self):
        """Test Place __str__ representation"""
        place = Place()
        place.id = "1133456"
        place.created_at = place.updated_at = datetime.today()
        place_str = str(place)
        self.assertIn("[Place] (113456)", place_str)
        self.assertIn("'id': '1133456'", place_str)
        self.assertIn("'created_at':", place_str)
        self.assertIn("'updated_at':", place_str)

    def test_to_dict_method(self):
        """Test Place to_dict method"""
        place = Place()
        place_dict = place.to_dict()
        self.assertEqual(dict, type(place_dict))
        self.assertIn('id', place_dict)
        self.assertIn('created_at', place_dict)
        self.assertIn('updated_at', place_dict)
        self.assertIn('city', place_dict)
        self.assertIn('user_id', place_dict)
        self.assertIn('name', place_dict)
        self.assertIn('description', place_dict)
        self.assertIn('number_of_rooms', place_dict)
        self.assertIn('number_of_bathrooms', place_dict)
        self.assertIn('maximum_guests', place_dict)
        self.assertIn('price_by_night', place_dict)
        self.assertIn('lat', place_dict)
        self.assertIn('lon', place_dict)
        self.assertIn('amenity_ids', place_dict)
        self.assertIn('__class__', place_dict)

    def test_save_method(self):
        """Test Place save method"""
        place = Place()
        place.save()
        self.assertNotEqual(place.created_at, place.updated_at)


if __name__ == "__main__":
    unittest.main()
