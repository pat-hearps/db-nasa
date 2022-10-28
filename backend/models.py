from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


Base = declarative_base()


class ArticleMeta(Base):
    """Contains identifying information about an article"""
    __tablename__ = "meta"
    id = Column(Integer, primary_key=True)
    section = Column(String, length=80)
    title = Column(String)
    identifier = Column(String)
    published_datetime = Column(DateTime)

    articles = relationship("Article")

class Article(Base):
    """Contains actual content of articles,
    trail: trailing text
    body: main article content"""
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True)
    meta_id = Column(ForeignKey("meta.id"))
    trail = Column(String)
    body = Column(String)
