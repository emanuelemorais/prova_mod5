from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine
from backend.models.base import Base
from backend.models.game import Game

engine = create_engine('sqlite+pysqlite:///banco.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)
