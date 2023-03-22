import sqlalchemy
from os import getenv

class DBStorage:
    """New storage using database."""

    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine("mysql+mysqldb://hbnb_dev:hbnb_dev_pwd@localhost:3306/hbnb_dev_db, pool_pre_ping=True")
        self.user = getenv(HBNB_MYSQL_USER)
        self.password = getenv(HBNB_MYSQL_PWD)
        self.host = getenv(HBNB_MYSQL_HOST)
        self.db = getenv(HBNB_MYSQL_DB)
        
        Session = sessionmaker(bind=engine)
        session = Session()


    if getenv(HBNB_ENV) == 'test':
        DBStorage.drop_all()


    def all(self, cls=None):
        results = {}
        if cls is None:
            for key, value in results.items():
                results += session.query(User).all()
                results += session.query(State).all()
                results += sessions.query(City).all()
                results += sessions.query(Amenity).all()
                results += sessions.query(Place).all()
                results += sessions.query(Review).all()
        else:
            results = session.query(cls).all()
        return results
    
    def new(self, obj):
        session.add(obj)

    def save(self, obj):
        session.commit(obj)

    def delete(self, obj=None):
        if obj not none:
            session.delete(obj)

    def reload(self):
        from models.base_model import BaseModel
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False), scoped_session=False)
        session = Session()
        Base.metadata.create_all(engine)



