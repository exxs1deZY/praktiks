from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Sword(Base):
    __tablename__ = 'swords'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    damage = Column(Integer)
    rarity = Column(String(50))
