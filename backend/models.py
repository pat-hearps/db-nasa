from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, Float, String, BigInteger, Integer


Base = declarative_base()


class EpicImage(Base):
    __tablename__ = "epic_images"
    id = Column(Integer, primary_key=True)
    identifier = Column(BigInteger)
    taken_datetime = Column(DateTime)
    version = Column(String(length=6))
    image_name = Column(String(length=30))
    centroid_lat = Column(Float)
    centroid_long = Column(Float)
