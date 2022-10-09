from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, Float, String, BigInteger, Integer


Base = declarative_base()


class EpicMeta(Base):
    __tablename__ = "epic_metadata"
    id = Column(Integer, primary_key=True)
    identifier = Column(BigInteger)
    taken_datetime = Column(DateTime)
    version = Column(String(length=6))
    image_name = Column(String(length=30))
    centroid_lat = Column(Float)
    centroid_long = Column(Float)
