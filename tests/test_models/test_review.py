#!/usr/bin/python3
"""
Unittests for review.py
"""
import unittest
from datetime import datetime
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test cases for Review class"""

    def test_instantiation(self):
        """Test Review instantiation"""
        review = Review()
        self.assertIsInstance(review, BaseModel)
        self.assertIsInstance(review, Review)

    def test_attributes(self):
        """Test Review attributes"""
        review = Review()
        self.assertTrue(hasattr(review, 'id'))
        self.assertTrue(hasattr(review, 'created_at'))
        self.assertTrue(hasattr(review, 'updated_at'))
        self.assertTrue(hasattr(review, 'place'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'comment'))

    def test_attribute_types(self):
        """Test Review attribute types"""
        review = Review()
        self.assertIsInstance(review.id, str)
        self.assertIsInstance(review.created_at, datetime)
        self.assertIsInstance(review.updated_at, datetime)
        self.assertIsInstance(review.place, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.comment, str)

    def test_review_initialization(self):
        """Test Review initialization"""
        review = Review(place="123", user_id="456", comment="Great experience")
        self.assertEqual(review.place, "123")
        self.assertEqual(review.user_id, "456")
        self.assertEqual(review.comment, "Great experience")

    def test_str_representation(self):
        """Test Review __str__ representation"""
        review = Review()
        review.id = "1133456"
        review.created_at = review.updated_at = datetime.today()
        review_str = str(review)
        self.assertIn("[Review] (1133456)", review_str)
        self.assertIn("'id': '1133456'", review_str)
        self.assertIn("'created_at':", review_str)
        self.assertIn("'updated_at':", review_str)

    def test_to_dict_method(self):
        """Test Review to_dict method"""
        review = Review()
        review_dict = review.to_dict()
        self.assertEqual(dict, type(review_dict))
        self.assertIn('id', review_dict)
        self.assertIn('created_at', review_dict)
        self.assertIn('updated_at', review_dict)
        self.assertIn('place', review_dict)
        self.assertIn('user_id', review_dict)
        self.assertIn('comment', review_dict)
        self.assertIn('__class__', review_dict)

    def test_save_method(self):
        """Test Review save method"""
        review = Review()
        review.save()
        self.assertNotEqual(review.created_at, review.updated_at)


if __name__ == "__main__":
    unittest.main()
