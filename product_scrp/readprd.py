import xlrd
from scraper_app.models import Product, Competitor


def readxls(contents):
	wb = xlrd.open_workbook(file_contents=contents)
	sh = wb.sheet_by_index(0)
	rows_num = sh.nrows
	cols_num = sh.ncols
	for row in range(rows_num):
		if row != 0:

			row_dict = dict(zip(sh.row_values(0), sh.row_values(row)))

			if 'The Sports Edit URL' in sh.row_values(0):

				if not Product.objects.filter(url = row_dict['The Sports Edit URL'], color = row_dict['Colour']):
					
					p = Product(
									brand=row_dict['Brand'],
									#gtin=row_dict['GTIN'],
									code=row_dict['Code'],
									color=row_dict['Colour'],
									#size=row_dict['The Sports Edit URL'],
									url=row_dict['The Sports Edit URL'],
								)
					p.save()
					print ("Product saved to database")
				else:
					print("Already exists")

			if 'Competitor URL' in sh.row_values(0):

				if not Competitor.objects.filter(site = row_dict['Competitor URL'], color=row_dict['Colour']
												) and Product.objects.filter(url=row_dict['Source URL']):

					c = Competitor(
									brand=row_dict['Brand'],
									color=row_dict['Colour'],
									vendor=row_dict['Vendor'],
									site=row_dict['Competitor URL'],
									prod_key=Product.objects.filter(url=row_dict['Source URL'])[0]
								)
					c.save()

				else:
					print('cannot add competitor')
					


if __name__ == "__main__":
	readxls('Price Scraping GTIN codes.xls')

'''from scraper_app.models import Product

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
			p.save()'''

