#!/usr/bin/python3
"""The class of File-Storage."""
import json


class FileStorage:
    """
        Putting instances to JSON and deputting to JSON.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
            Going back to the dictinary.
        """
        fs_objects = {}
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        if cls:
            if type(cls) is str and cls in classes:
                for key, val in self.__objects.items():
                    if cls == key.split('.')[0]:
                        fs_objects[key] = val
            elif cls.__name__ in classes:
                for key, val in self.__objects.items():
                    if cls.__name__ == key.split('.')[0]:
                        fs_objects[key] = val
        else:
            return self.__objects
        return fs_objects

    def new(self, obj):
        """
            Putting the object with key <obj class name> id.
        """
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        value_dict = obj
        FileStorage.__objects[key] = value_dict

    def save(self):
        """
            Putting objects attriebute to JSON.
        """
        objects_dict = {}
        for key, val in FileStorage.__objects.items():
            objects_dict[key] = val.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(objects_dict, fd)

    def reload(self):
        """
            Deputting the JSON file to objects.
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            with open(FileStorage.__file_path, encoding="UTF8") as fd:
                FileStorage.__objects = json.load(fd)
            for key, val in FileStorage.__objects.items():
                class_name = val["__class__"]
                class_name = classes[class_name]
                FileStorage.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deleting object from objects.
        """
        if obj is not None:
            key = obj.__class__.__name__ + "." + str(obj.id)
            if key in self.__objects:
                del self.__objects[key]
        self.save()

    def close(self):
        """
        Calling for reload.
        """
        self.reload()

    def get(self, cls, id):
        """ retrieves one object """
        obj_dict = {}
        obj = None
        if cls:
            obj_dict = FileStorage.__objects.values()
            for item in obj_dict:
                if item.id == id:
                    obj = item
            return obj

    def count(self, cls=None):
        """ counting num of objcts of classes in storage """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        if cls:
            obj_list = []
            obj_dict = FileStorage.__objects.values()
            for item in obj_dict:
                if type(item).__name__ == cls:
                    obj_list.append(item)
            return len(obj_list)
        else:
            obj_list = []
            for class_name in classes:
                if class_name == 'BaseModel':
                    continue
                obj_class = FileStorage.__objects
                for item in obj_class:
                    obj_list.append(item)
            return len(obj_list)

