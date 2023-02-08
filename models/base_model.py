#!/usr/bin/python3
"""
    a base class model that saves the date,
        id and time that an instance was created
"""
import uuid
from datetime import datetime


class BaseModel:
    """
        a class BaseModel that defines all
            common attributes/methods for other classes
    """
    def __init__(self):
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        self.__dict__["__class__"] = self.__class__.__name__
        self.__dict__["created_at"] = self.created_at.isoformat()
        self.__dict__["updated_at"] = self.updated_at.isoformat()
        return self.__dict__
