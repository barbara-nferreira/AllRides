from sqlalchemy import Column, ForeignKey, Table, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Integer, String, Boolean, Float, Date
from sqlalchemy.orm import relationship
from database import session, engine

Base = declarative_base()


class Category(Base):
    __tablename__ = 'category'
    category_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    def __repr__(self):
        return f"<Category {self.name}>"

class Vehicle(Base):
    __tablename__ = 'vehicle'
    vehicle_id = Column(Integer, primary_key=True, autoincrement=True)
    category_id = Column(Integer, ForeignKey(
        'category.category_id'), nullable=False)
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
    client_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    phone = Column(String(20), nullable=False)

    def __repr__(self):
        return f"<Client {self.first_name} {self.last_name}>"


class Purchase(Base):
    __tablename__ = 'purchase'
    purchase_id = Column(Integer, primary_key=True, autoincrement=True)
    vehicle_id = Column(Integer, ForeignKey('vehicle.vehicle_id'), nullable=False)
    client_id = Column(Integer, ForeignKey('client.client_id'), nullable=False)
    purchase_date = Column(Date, nullable=False)
    total_price = Column(Float, nullable=False)

    vehicle = relationship('Vehicle', backref='purchases')
    client = relationship('Client', backref='purchases')

    def __repr__(self):
        return f"<Purchase {self.purchase_date} - Car ID: {self.vehicle_id}>"


class Rental(Base):
    __tablename__ = 'rental'
    rental_id = Column(Integer, primary_key=True, autoincrement=True)
    vehicle_id = Column(Integer, ForeignKey('vehicle.vehicle_id'), nullable=False)
    client_id = Column(Integer, ForeignKey('client.client_id'), nullable=False)
    rental_start_date = Column(Date, nullable=False)
    rental_end_date = Column(Date, nullable=False)
    total_price = Column(Float, nullable=False)

    vehicle = relationship('Vehicle', backref='rentals')
    client = relationship('Client', backref='rentals')

    def __repr__(self):
        return f"<Rental {self.rental_start_date} to {self.rental_end_date} - Car ID: {self.vehicle_id}>"


# Base.metadata.create_all(engine)
