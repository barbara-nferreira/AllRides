from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Integer, String, Boolean, Float, Date
from sqlalchemy.orm import relationship
from database import session, engine

Base = declarative_base()


class VehicleCategory(Base):
    __tablename__ = 'vehicle_category'
    category_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    def __repr__(self):
        return f"<VehicleCategory {self.name}>"


class CarType(Base):
    __tablename__ = 'car_type'
    car_type_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    category_id = Column(Integer, ForeignKey(
        'vehicle_category.category_id'), nullable=False)

    category = relationship('VehicleCategory', backref='car_types')

    def __repr__(self):
        return f"<CarType {self.name}>"


class Car(Base):
    __tablename__ = 'car'
    car_id = Column(Integer, primary_key=True, autoincrement=True)
    type_id = Column(Integer, ForeignKey(
        'car_type.car_type_id'), nullable=False)
    make = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    year = Column(Integer, nullable=False)
    fuel_type = Column(String(20), nullable=False)
    horsepower = Column(Integer, nullable=False)
    kilometers = Column(Float, nullable=False)
    transmission = Column(String(20), nullable=False)
    image_url = Column(String(250))
    available_for_rent = Column(Boolean, nullable=False)
    available_for_purchase = Column(Boolean, nullable=False)
    rental_price_per_day = Column(Float)
    purchase_price = Column(Float)
    is_available = Column(Boolean, nullable=False)

    car_type = relationship('CarType', backref='cars')

    def __repr__(self):
        return f"<Car {self.make} {self.model} ({self.year})>"


class MotorcycleType(Base):
    __tablename__ = 'motorcycle_type'
    type_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    category_id = Column(Integer, ForeignKey(
        'vehicle_category.category_id'), nullable=False)

    category = relationship('VehicleCategory', backref='motorcycle_types')

    def __repr__(self):
        return f"<MotorcycleType {self.name}>"


class Motorcycle(Base):
    __tablename__ = 'motorcycle'
    motorcycle_id = Column(Integer, primary_key=True, autoincrement=True)
    type_id = Column(Integer, ForeignKey(
        'motorcycle_type.type_id'), nullable=False)
    make = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    year = Column(Integer, nullable=False)
    fuel_type = Column(String(20), nullable=False)
    horsepower = Column(Integer, nullable=False)
    kilometers = Column(Float, nullable=False)
    transmission = Column(String(20), nullable=False)
    image_url = Column(String(250))
    available_for_rent = Column(Boolean, nullable=False)
    available_for_purchase = Column(Boolean, nullable=False)
    rental_price_per_day = Column(Float)
    purchase_price = Column(Float)
    is_available = Column(Boolean, nullable=False)

    motorcycle_type = relationship('MotorcycleType', backref='motorcycles')

    def __repr__(self):
        return f"<Motorcycle {self.make} {self.model} ({self.year})>"


class TruckType(Base):
    __tablename__ = 'truck_type'
    type_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    category_id = Column(Integer, ForeignKey(
        'vehicle_category.category_id'), nullable=False)

    category = relationship('VehicleCategory', backref='truck_types')

    def __repr__(self):
        return f"<TruckType {self.name}>"


class Truck(Base):
    __tablename__ = 'truck'
    truck_id = Column(Integer, primary_key=True, autoincrement=True)
    type_id = Column(Integer, ForeignKey('truck_type.type_id'), nullable=False)
    make = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    year = Column(Integer, nullable=False)
    fuel_type = Column(String(20), nullable=False)
    horsepower = Column(Integer, nullable=False)
    kilometers = Column(Float, nullable=False)
    payload_capacity = Column(Float, nullable=False)
    image_url = Column(String(250))
    available_for_rent = Column(Boolean, nullable=False)
    available_for_purchase = Column(Boolean, nullable=False)
    rental_price_per_day = Column(Float)
    purchase_price = Column(Float)
    is_available = Column(Boolean, nullable=False)

    truck_type = relationship('TruckType', backref='trucks')

    def __repr__(self):
        return f"<Truck {self.make} {self.model} ({self.year})>"


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
    car_id = Column(Integer, ForeignKey('car.car_id'), nullable=False)
    client_id = Column(Integer, ForeignKey('client.client_id'), nullable=False)
    purchase_date = Column(Date, nullable=False)
    total_price = Column(Float, nullable=False)

    car = relationship('Car', backref='purchases')
    client = relationship('Client', backref='purchases')

    def __repr__(self):
        return f"<Purchase {self.purchase_date} - Car ID: {self.car_id}>"


class Rental(Base):
    __tablename__ = 'rental'
    rental_id = Column(Integer, primary_key=True, autoincrement=True)
    car_id = Column(Integer, ForeignKey('car.car_id'), nullable=False)
    client_id = Column(Integer, ForeignKey('client.client_id'), nullable=False)
    rental_start_date = Column(Date, nullable=False)
    rental_end_date = Column(Date, nullable=False)
    total_price = Column(Float, nullable=False)

    car = relationship('Car', backref='rentals')
    client = relationship('Client', backref='rentals')

    def __repr__(self):
        return f"<Rental {self.rental_start_date} to {self.rental_end_date} - Car ID: {self.car_id}>"


# Base.metadata.create_all(engine)
