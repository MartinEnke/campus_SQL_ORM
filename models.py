from sqlalchemy import Column, Integer, String
from setup import Base



class Restaurant(Base):

    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    city = Column(String)
    famous_dish = Column(String)

    def __repr__(self):
        return f"Restaurant(id = {self.id}, name = {self.name})"


class Hotel(Base):

    __tablename__ = "hotels"

    hotel_id = Column(Integer, primary_key=True)
    hotel_name = Column(String, nullable=False)
    hotel_city = Column(String)

