from sqlalchemy import Column, ForeignKey, Table, desc, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Integer, String, Boolean, Float, Date
from sqlalchemy.orm import relationship
from database import db_session, engine

Base = declarative_base()


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    def __repr__(self):
        return f"<Category {self.name}>"

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True, autoincrement=True)
    category_id = Column(Integer, ForeignKey(
        'category.id'), nullable=False)
    make = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    year = Column(Integer, nullable=False)
    fuel_type = Column(String(20), nullable=False)
    horsepower = Column(Integer, nullable=False)
    kilometers = Column(Float, nullable=False)
    transmission = Column(String(20), nullable=False)
    image_url = Column(String(250))
    location = Column(String(50), nullable=False)
    available_for_rent = Column(Boolean, nullable=False)
    available_for_purchase = Column(Boolean, nullable=False)
    rental_price_per_day = Column(Float)
    purchase_price = Column(Float)
    is_available = Column(Boolean, nullable=False)

    category = relationship('Category', backref='vehicles')

    def __repr__(self):
        return f"<Vehicle {self.make} {self.model} ({self.year})>"

class Client(Base):
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    phone = Column(String(20), nullable=False)

    def __repr__(self):
        return f"<Client {self.first_name} {self.last_name}>"


class Purchase(Base):
    __tablename__ = 'purchase'
    id = Column(Integer, primary_key=True, autoincrement=True)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), nullable=False)
    client_id = Column(Integer, ForeignKey('client.id'), nullable=False)
    purchase_date = Column(Date, nullable=False)
    total_price = Column(Float, nullable=False)

    vehicle = relationship('Vehicle', backref='purchases')
    client = relationship('Client', backref='purchases')

    def __repr__(self):
        return f"<Purchase {self.purchase_date} - Car ID: {self.vehicle_id}>"


class Rental(Base):
    __tablename__ = 'rental'
    id = Column(Integer, primary_key=True, autoincrement=True)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), nullable=False)
    client_id = Column(Integer, ForeignKey('client.id'), nullable=False)
    rental_start_date = Column(Date, nullable=False)
    rental_end_date = Column(Date, nullable=False)
    total_price = Column(Float, nullable=False)

    vehicle = relationship('Vehicle', backref='rentals')
    client = relationship('Client', backref='rentals')

    def __repr__(self):
        return f"<Rental {self.rental_start_date} to {self.rental_end_date} - Car ID: {self.vehicle_id}>"

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)

# Base.metadata.create_all(engine)
