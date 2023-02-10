#!/usr/bin/python3
"""
    unnittest for base_model.py
"""
import datetime
import unittest
import sys

# add two directories back to the sys.path list
sys.path.append("..")
sys.path.append("..")

from models.Basemodel import BaseModel


class TestDatetimeISOFormat(unittest.TestCase):
    def to_dict(self):
        dt = datetime.now
        expected_output = self.__dict__["created_at"]
        self.assertEqual(dt.isoformat(), expected_output)

if __name__ == '__main__':
    unittest.main()

