#!/usr/bin/python3
from os import getenv, environ
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, query, scoped_session
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.base_model import BaseModel
from models.amenity import Amenity


class DBStorage:
    """class for database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage."""
        user = environ["HBNB_MYSQL_USER"]
        password = environ["HBNB_MYSQL_PWD"]
        host = environ["HBNB_MYSQL_HOST"]
        database = environ["HBNB_MYSQL_DB"]

        self.__engine = create_engine(
                "mysql+mysqldb://{}:{}@{}/{}".format(
                    user, password, host, database),
                echo=False, pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Return requested type of object if not specified retun all."""
        all_dict = {}
        if cls is None:
            obj = self.__session.query(State).all()
            obj.extend(self.__session.query(User).all())
            obj.extend(self.__session.query(Review).all())
            obj.extend(self.__session.query(Place).all())
            obj.extend(self.__session.query(City).all())
            obj.extend(self.__session.query(Amenity).all())
        else:
            obj = (self.__session.query(cls).all())
        for item in obj:
            all_dict[f"{item.__class__.__name__}.{item.id}"] = item
        return all_dict

    def new(self, obj):
        """Add object to database session."""
        self.__session.add(obj)

    def save(self):
        """Save changes to database."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete objects from the database."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Push objects to database."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
