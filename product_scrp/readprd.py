from scraper_app.models import Product

import csv

with open('products.csv', 'r') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';')
	for row in spamreader:
		if not ''.join(row) == '':
			p = Product(brand=row[0],
						#gtin=row[1],
						code=row[1],
						color=row[2],
						#size=row[4],
						url=row[3],
						)
			p.save()

