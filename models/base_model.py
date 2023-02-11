#!/usr/bin/python3
"""
    a base class model that saves the date,
        id and time that an instance was created
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
        a class BaseModel that defines all
            common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        The class constructor
        Initializes instance attributes
        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """

        if len(kwargs) != 0:
            for key in kwargs:
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(
                            kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns official string representation of the class"""

        return "[{}] ({}) {}".\
            format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a copy of a dictionary containing all keys-values of __dict__"""

        class_dict = self.__dict__.copy()
        class_dict["__class__"] = type(self).__name__
        class_dict["created_at"] = class_dict["created_at"].isoformat()
        class_dict["updated_at"] = class_dict["updated_at"].isoformat()
        return class_dict
