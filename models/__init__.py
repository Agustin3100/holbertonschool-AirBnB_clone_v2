#!/usr/bin/python3
"""Choose if dbstorage or filestorage will be used."""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.engine.db_storage import DBStorage
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.city import City
from models.state import State
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
