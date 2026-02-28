import os
import csv

os.makedirs('data/raw', exist_ok=True)

# Crear sales_data.csv de ejemplo con más datos
with open('data/raw/sales_data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(
        f,
        fieldnames=['id', 'product', 'quantity', 'price', 'region']
    )
    writer.writeheader()

    writer.writerow({'id': '1', 'product': 'A', 'quantity': '3', 'price': '15', 'region': 'north'})
    writer.writerow({'id': '2', 'product': 'B', 'quantity': '5', 'price': '20', 'region': 'south'})
    writer.writerow({'id': '3', 'product': 'C', 'quantity': '1', 'price': '50', 'region': 'east'})
    writer.writerow({'id': '4', 'product': 'A', 'quantity': '7', 'price': '15', 'region': 'west'})
    writer.writerow({'id': '5', 'product': 'B', 'quantity': '2', 'price': '20', 'region': 'north'})

# Crear product_catalog.csv con más productos
with open('data/raw/product_catalog.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(
        f,
        fieldnames=['product', 'category']
    )
    writer.writeheader()

    writer.writerow({'product': 'A', 'category': 'electronics'})
    writer.writerow({'product': 'B', 'category': 'home'})
    writer.writerow({'product': 'C', 'category': 'sports'})

print("Sample data created successfully")