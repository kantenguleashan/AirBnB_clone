import unittest
from models.base_model import BaseModel
import uuid
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bm = BaseModel()

    @classmethod
    def tearDownClass(cls):
        del cls.bm

    def test_id(self):
        self.assertTrue(uuid.UUID(self.bm.id))
        self.assertIsInstance(self.bm.id, str)

    def test_created_at(self):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.assertEqual(now, self.bm.created_at.strftime("%Y-%m-%d %H:%M:%S"))
        self.assertIsInstance(self.bm.created_at, datetime)

    def test_updated_at(self):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.assertEqual(now, self.bm.updated_at.strftime("%Y-%m-%d %H:%M:%S"))
        self.assertIsInstance(self.bm.updated_at, datetime)

    def test_str_format(self):
        expected = f"[BaseModel] ({self.bm.id}) {self.bm.__dict__}"
        self.assertEqual(str(self.bm), expected)

    def test_str_update(self):
        self.bm.name = "myname"
        expected = f"[BaseModel] ({self.bm.id}) {self.bm.__dict__}"
        self.assertEqual(str(self.bm), expected)

    def test_str_save(self):
        self.bm.save()
        expected = f"[BaseModel] ({self.bm.id}) {self.bm.__dict__}"
        self.assertEqual(str(self.bm), expected)

    def test_to_dict_format(self):
        my_dict = self.bm.to_dict()
        self.assertIn("id", my_dict)
        self.assertIn("created_at", my_dict)
        self.assertIn("updated_at", my_dict)
        self.assertIn("__class__", my_dict)

    def test_to_dict_attributes(self):
        my_dict = self.bm.to_dict()
        self.assertEqual(my_dict["id"], self.bm.id)
        self.assertEqual(my_dict["created_at"], self.bm.created_at.isoformat())
        self.assertEqual(my_dict["updated_at"], self.bm.updated_at.isoformat())
        self.assertEqual(my_dict["__class__"], "BaseModel")

    def test_to_dict_update(self):
        self.bm.name = "test_name"
        my_dict = self.bm.to_dict()
        self.assertEqual(my_dict["name"], "test_name")

    def test_save_update_to_dict(self):
        self.bm.save()
        my_dict = self.bm.to_dict()
        self.assertEqual(my_dict["updated_at"], self.bm.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()

