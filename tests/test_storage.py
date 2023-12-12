#!/usr/bin/python3
"""
Unittests for models/engine/file_storage.py
"""
import os
import json
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorageInitialization(unittest.TestCase):
    """Tests for FileStorage initialization."""

    def test_FileStorage_instance(self):
        """Test if FileStorage is an instance of FileStorage"""
        self.assertIsInstance(FileStorage(), FileStorage)

    def test_FileStorage_with_argument(self):
        """Test if FileStorage raises TypeError with an argument"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_file_path_type(self):
        """Test if __file_path attribute is of type str"""
        self.assertEqual(str, type(FileStorage()._FileStorage__file_path))

    def test_objects_type(self):
        """Test if __objects attribute is of type dict"""
        self.assertEqual(dict, type(FileStorage()._FileStorage__objects))

    def test_storage_instance(self):
        """Test if models.storage is an instance of FileStorage"""
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorageMethods(unittest.TestCase):
    """Tests for FileStorage methods."""

    @classmethod
    def setUp(self):
        """Set up for testing FileStorage methods."""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        """Tear down after testing FileStorage methods."""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage()._FileStorage__objects = {}

    def test_all_method(self):
        """Test the all method of FileStorage"""
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_method_with_argument(self):
        """Test if all method raises TypeError with an argument"""
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new_method(self):
        """Test the new method of FileStorage"""
        bm = BaseModel()
        models.storage.new(bm)
        bm_key = "{}.{}".format(bm.__class__.__name__, bm.id)
        self.assertIn(bm_key, models.storage.all().keys())
        self.assertIn(bm.to_dict(), models.storage.all().values())

    def test_new_method_with_argument(self):
        """Test if new method raises TypeError with an argument"""
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save_method(self):
        """Test the save method of FileStorage"""
        bm = BaseModel()
        models.storage.new(bm)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            bm_key = "{}.{}".format(bm.__class__.__name__, bm.id)
            self.assertIn(bm_key, save_text)
            self.assertIn(str(bm.to_dict()), save_text)

    def test_save_method_with_argument(self):
        """Test if save method raises TypeError with an argument"""
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload_method(self):
        """Test the reload method of FileStorage"""
        bm = BaseModel()
        models.storage.new(bm)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage()._FileStorage__objects
        bm_key = "{}.{}".format(bm.__class__.__name__, bm.id)
        self.assertIn(bm_key, objs)
        self.assertIn(str(bm.to_dict()), str(objs[bm_key]))

    def test_reload_method_with_argument(self):
        """Test if reload method raises TypeError with an argument"""
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
