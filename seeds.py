from models import *
from datetime import date
from database import *

# Add vehicle categories to the database
categories = ['Car', 'Motorcycle', 'Truck']
for category in categories:
    category = Category(name=category)
    session.add(category)

# Add vehicles
Vehicles = [

    
    {'category_id': 1, 'make': 'Ford', 'model': 'Explorer', 'year': 2019, 'fuel_type': 'Gasoline', 'horsepower': 250, 'kilometers': 30000, 'transmission': 'Automatic', 'image_url': 'public/assets/img/seeds/car1.jpg', 'location': 'Rome', 'available_for_rent': True, 'available_for_purchase': False, 'rental_price_per_day': 60.0, 'purchase_price': None, 'is_available': True},
    {'category_id': 1, 'make': 'Toyota', 'model': 'Tacoma', 'year': 2021, 'fuel_type': 'Diesel', 'horsepower': 278, 'kilometers': 15000, 'transmission': 'Automatic', 'image_url': 'public/assets/img/seeds/car3.jpg', 'location': 'Rome', 'available_for_rent': True, 'available_for_purchase': False, 'rental_price_per_day': 55.0, 'purchase_price': None, 'is_available': True},
    {'category_id': 1, 'make': 'Honda', 'model': 'Accord', 'year': 2020, 'fuel_type': 'Gasoline', 'horsepower': 190, 'kilometers': 20000, 'transmission': 'Automatic', 'image_url': 'public/assets/img/seeds/car4.jpg', 'location': 'Rome', 'available_for_rent': False, 'available_for_purchase': True, 'rental_price_per_day': None, 'purchase_price': 28000.0, 'is_available': False},
    {'category_id': 1, 'make': 'Nissan', 'model': 'Rogue', 'year': 2018, 'fuel_type': 'Gasoline', 'horsepower': 170, 'kilometers': 35000, 'transmission': 'Manual', 'image_url': 'public/assets/img/seeds/car5.png', 'location': 'Milano', 'available_for_rent': False, 'available_for_purchase': True, 'rental_price_per_day': None, 'purchase_price': 23000.0, 'is_available': False},
    {'category_id': 2, 'make': 'Harley-Davidson', 'model': 'Sportster Iron 883', 'year': 2022, 'fuel_type': 'Gasoline', 'horsepower': 50, 'kilometers': 2000, 'transmission': 'Manual', 'image_url': 'public/assets/img/seeds/moto1.jpg', 'location': 'Rome', 'available_for_rent': True, 'available_for_purchase': False, 'rental_price_per_day': 25.0, 'purchase_price': None, 'is_available': True},
    {'category_id': 2, 'make': 'Vespa', 'model': 'GTS 300', 'year': 2021, 'fuel_type': 'Gasoline', 'horsepower': 22, 'kilometers': 1000, 'transmission': 'Automatic', 'image_url': 'public/assets/img/seeds/moto2.jpg', 'location': 'Milano', 'available_for_rent': True, 'available_for_purchase': False, 'rental_price_per_day': 20.0, 'purchase_price': None, 'is_available': True},
    {'category_id': 2, 'make': 'Indian', 'model': 'Chieftain', 'year': 2020, 'fuel_type': 'Gasoline', 'horsepower': 74, 'kilometers': 3000, 'transmission': 'Manual', 'image_url': 'public/assets/img/seeds/moto4.jpg', 'location': 'Napoles', 'available_for_rent': False, 'available_for_purchase': True, 'rental_price_per_day': None, 'purchase_price': 18000.0, 'is_available': True},
    {'category_id': 2, 'make': 'Honda', 'model': 'PCX', 'year': 2022, 'fuel_type': 'Gasoline', 'horsepower': 14, 'kilometers': 500, 'transmission': 'Automatic', 'image_url': 'public/assets/img/seeds/moto5.jpg', 'location': 'Rome', 'available_for_rent': False, 'available_for_purchase': True, 'rental_price_per_day': None, 'purchase_price': 4000.0, 'is_available': True},
    {'category_id': 2, 'make': 'KTM', 'model': 'Adventure 390', 'year': 2021, 'fuel_type': 'Gasoline', 'horsepower': 43, 'kilometers': 1500, 'transmission': 'Manual', 'image_url': 'public/assets/img/seeds/moto6.jpg', 'location': 'Milano', 'available_for_rent': False, 'available_for_purchase': True, 'rental_price_per_day': None, 'purchase_price': 9000.0, 'is_available': True},
    {'category_id': 3, 'make': 'Isuzu', 'model': 'NQR', 'year': 2020, 'fuel_type': 'Diesel', 'horsepower': 200, 'kilometers': 40000, 'transmission': 'Automatic', 'image_url': 'public/assets/img/seeds/truck1.jpg', 'location': 'Napoles', 'available_for_rent': True, 'available_for_purchase': False, 'rental_price_per_day': 90.0, 'purchase_price': None, 'is_available': True},
    {'category_id': 3, 'make': 'Freightliner', 'model': 'Cascadia', 'year': 2019, 'fuel_type': 'Diesel', 'horsepower': 450, 'kilometers': 100000, 'transmission': 'Automatic', 'image_url': 'public/assets/img/seeds/truck2.jpg', 'location': 'Rome', 'available_for_rent': True, 'available_for_purchase': False, 'rental_price_per_day': 120.0, 'purchase_price': None, 'is_available': True},
    {'category_id': 3, 'make': 'Kenworth', 'model': 'T680', 'year': 2022, 'fuel_type': 'Diesel', 'horsepower': 500, 'kilometers': 20000, 'transmission': 'Automatic', 'image_url': 'public/assets/img/seeds/truck3.jpg', 'location': 'Rome', 'available_for_rent': True, 'available_for_purchase': False, 'rental_price_per_day': 100.0, 'purchase_price': None, 'is_available': True},
    {'category_id': 3, 'make': 'Hino', 'model': '155', 'year': 2021, 'fuel_type': 'Diesel', 'horsepower': 210, 'kilometers': 5000, 'transmission': 'Automatic', 'image_url': 'public/assets/img/seeds/truck4.jpg', 'location': 'Rome', 'available_for_rent': False, 'available_for_purchase': True, 'rental_price_per_day': None, 'purchase_price': 40000.0, 'is_available': False},
    {'category_id': 3, 'make': 'Peterbilt', 'model': '579', 'year': 2023, 'fuel_type': 'Diesel', 'horsepower': 500, 'kilometers': 1000, 'transmission': 'Automatic', 'image_url': 'public/assets/img/seeds/truck5.jpg', 'location': 'Napoles', 'available_for_rent': False, 'available_for_purchase': True, 'rental_price_per_day': None, 'purchase_price': 80000.0, 'is_available': True},
    {'category_id': 3, 'make': 'Volvo', 'model': 'VNR 640', 'year': 2020, 'fuel_type': 'Diesel', 'horsepower': 425, 'kilometers': 30000, 'transmission': 'Automatic', 'image_url': 'public/assets/img/seeds/truck6.jpeg', 'location': 'Rome', 'available_for_rent': False, 'available_for_purchase': True, 'rental_price_per_day': None, 'purchase_price': 60000.0, 'is_available': True},
    {'category_id': 2, 'make': 'BMW', 'model': 'R 1250 GS', 'year': 2023, 'fuel_type': 'Gasoline', 'horsepower': 136, 'kilometers': 500, 'transmission': 'Manual', 'image_url': 'public/assets/img/seeds/moto3.jpg', 'location': 'Rome', 'available_for_rent': True, 'available_for_purchase': False, 'rental_price_per_day': 35.0, 'purchase_price': None, 'is_available': True},
    {'category_id': 1, 'make': 'Jeep', 'model': 'Wrangler', 'year': 2022, 'fuel_type': 'Gasoline', 'horsepower': 285, 'kilometers': 5000, 'transmission': 'Automatic', 'image_url': 'public/assets/img/seeds/car2.jpg', 'location': 'Rome', 'available_for_rent': True, 'available_for_purchase': False, 'rental_price_per_day': 70.0, 'purchase_price': None, 'is_available': True},
    {'category_id': 1, 'make': 'Ford', 'model': 'Ranger', 'year': 2021, 'fuel_type': 'Diesel', 'horsepower': 270, 'kilometers': 10000, 'transmission': 'Manual', 'image_url': 'public/assets/img/seeds/car6.jpg', 'location': 'Rome', 'available_for_rent': False, 'available_for_purchase': True, 'rental_price_per_day': None, 'purchase_price': 32000.0, 'is_available': True},
]

for vehicle in Vehicles:
    vehicle = Vehicle(**vehicle)
    session.add(vehicle)

# Add clients
clients = [
    {'first_name': 'Jane', 'last_name': 'Smith', 'email': 'jane.smith@example.com', 'phone': '9876543210'},
    {'first_name': 'Michael', 'last_name': 'Johnson', 'email': 'michael.johnson@example.com', 'phone': '5555555555'},
    {'first_name': 'Emily', 'last_name': 'Williams', 'email': 'emily.williams@example.com', 'phone': '1112223333'},
    {'first_name': 'Maria', 'last_name': 'Williams', 'email': 'maria.williams@example.com', 'phone': '1112224444'},
    {'first_name': 'Michael', 'last_name': 'Scott', 'email': 'michael.scott@example.com', 'phone': '1112226666'},
    {'first_name': 'Toby', 'last_name': 'Smith', 'email': 'toby.smith@example.com', 'phone': '1112223388'},
    
]

for client in clients:
    client = Client(**client)
    session.add(client)

# Add purchases
purchases = [
    {'vehicle_id': 3, 'client_id': 3, 'purchase_date': date(2023, 3, 20), 'total_price': 28000.0},
    {'vehicle_id': 4, 'client_id': 4, 'purchase_date': date(2023, 4, 10), 'total_price': 23000.0},
    {'vehicle_id': 13, 'client_id': 2, 'purchase_date': date(2023, 7, 1), 'total_price': 40000.0},   
]

for purchase in purchases:
    purchase = Purchase(**purchase)
    session.add(purchase)

# Add rentals
rentals = [
    {'vehicle_id': 17, 'client_id': 1, 'rental_start_date': date(2023, 2, 1), 'rental_end_date': date(2023, 2, 7), 'total_price': 420.0},
    {'vehicle_id': 16, 'client_id': 4, 'rental_start_date': date(2023, 3, 10), 'rental_end_date': date(2023, 3, 18), 'total_price': 280.0},
    {'vehicle_id': 10, 'client_id': 5, 'rental_start_date': date(2023, 4, 5), 'rental_end_date': date(2023, 4, 10), 'total_price': 450.0},
    {'vehicle_id': 12, 'client_id': 6, 'rental_start_date': date(2023, 7, 3), 'rental_end_date': date(2023, 7, 9), 'total_price': 600.0},
]

for rental in rentals:
    rental = Rental(**rental)
    session.add(rental)

# Commit changes to the database
session.commit()
