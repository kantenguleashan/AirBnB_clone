#!/usr/bin/env python3
"""serializes and deserializes objects to
and from json
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    def __init__(self, file_path="file.json"):
        self.file_path = file_path
        self.objects = {}

    def all(self):
        return self.objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.objects[key] = obj

    def save(self):
        with open(self.file_path, "w", encoding="utf-8") as f:
            serialized_objects = {key: value.to_dict() for key, value in self.objects.items()}
            json.dump(serialized_objects, f)

    def reload(self):
        class_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                json_data = json.load(f)
                self.objects = {
                    key: class_dict[value["__class__"]](**value) for key, value in json_data.items()
                }
        except FileNotFoundError:
            pass

