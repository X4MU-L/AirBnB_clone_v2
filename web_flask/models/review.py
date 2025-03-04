#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, ForeignKey, Column


class Review(BaseModel, Base):
    """
    Review class to store review information

        attributes:

            place_id (string): foreign key from places id
            user_id (string): foreign key from states id
            text (string): the review text
    """

    __tablename__ = "reviews"
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    text = Column(String(1024), nullable=False)
