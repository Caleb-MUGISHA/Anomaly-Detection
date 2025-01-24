from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.settings import Config

Base = declarative_base()

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    amount = Column(Float)
    currency = Column(String(3))
    timestamp = Column(DateTime)
    merchant = Column(String(100))
    location = Column(String(50))
    is_fraud = Column(Integer)

def get_engine():
    return create_engine(
        f"postgresql://{Config.DB_USER}:{Config.DB_PASSWORD}@{Config.DB_HOST}:{Config.DB_PORT}/{Config.DB_NAME}"
    )

def create_tables(engine):
    Base.metadata.create_all(engine)
