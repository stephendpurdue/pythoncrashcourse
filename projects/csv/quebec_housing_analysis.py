import csv
from matplotlib import pyplot as plt

filename = 'quebec_housing_sales_v2.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    
    city = []
    bedrooms = []
    bathrooms = []

    # Extracts all information in one pass (more efficient)
    for row in reader:
        city.append(row[1])
        bedrooms.append(row[4])
        bathrooms.append(row[5])

    print(bedrooms)
    print(bathrooms)