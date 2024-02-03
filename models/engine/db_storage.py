#!/usr/bin/python3
"""Creating the DB-Storage class."""
from os import getenv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session

database = getenv("HBNB_MYSQL_DB")
user = getenv("HBNB_MYSQL_USER")
host = getenv("HBNB_MYSQL_HOST")
password = getenv("HBNB_MYSQL_PWD")
hbnb_env = getenv("HBNB_ENV")


class DBStorage:
    """
    DB-Storage Class.
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Start init instences.
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format
                                      (user, password, host, database),
                                      pool_pre_ping=True)

        if hbnb_env == 'test':
            from models.base_model import Base
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Giving back vareity of instence attributes. 
        """
        dbobjects = {}
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
                for obj in self.__session.query(classes[cls]).all():
                    key = str(obj.__class__.__name__) + "." + str(obj.id)
                    val = obj
                    dbobjects[key] = val
            elif cls.__name__ in classes:
                for obj in self.__session.query(cls).all():
                    key = str(obj.__class__.__name__) + "." + str(obj.id)
                    val = obj
                    dbobjects[key] = val
        else:
            for key, v in classes.items():
                for obj in self.__session.query(v).all():
                    key = str(v.__name__) + "." + str(obj.id)
                    val = obj
                    dbobjects[key] = val
        return dbobjects

    def new(self, obj):
        """
        Putting object to actual database sesion. 
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """
        Making commit of changes of database sesion.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deleting from curent database sesion.
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Creating tables in database and curent database sesion.
        """
        from models.base_model import Base
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        session = scoped_session(session_factory)
        self.__session = session()

    def close(self):
        """
        quitting sesion.
        """
        self.__session.close()

    def get(self, cls, id):
        """ retrieves one object """
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
            obj_dict = {}
            if cls:
                obj_class = self.__session.query(classes.get(cls)).all()
                for item in obj_class:
                    obj_dict[item.id] = item
            return obj_dict[id]
        except:
            return None

    def count(self, cls=None):
        """Counts number of objects in storage

        Args:
            cls: optional string representing the class name
        Returns:
            the number of objects in storage matching the given class name.

            If no name is passed, returns the count of all objects in storage.
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
        obj_dict = {}
        if cls:
            obj_class = self.__session.query(classes.get(cls)).all()
            for item in obj_class:
                obj_dict[item.id] = item
            return len(obj_dict)
        else:
            for cls_name in classes:
                if cls_name == 'BaseModel':
                    continue
                obj_class = self.__session.query(classes.get(cls_name)).all()
                for item in obj_class:
                    obj_dict[item.id] = item
            return len(obj_dict)

