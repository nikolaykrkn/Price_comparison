from django.db import models


class Product(models.Model):
	brand = models.CharField('Brand Name', max_length=200, blank=True)
	#gtin = models.CharField('GTIN code', max_length=200, blank=True)
	code = models.CharField(max_length=200, blank=True)
	color = models.CharField(max_length=200, blank=True)
	#size = models.CharField(max_length=5, blank=True)
	url = models.CharField(max_length=200, blank=True)
	price = models.DecimalField('Price', decimal_places=2, max_digits=12, default=-1.0, blank=True)
	currency = models.CharField('Currency', max_length=5, default='GBP', blank=True)

	def __str__(self):
		return self.url.split('/')[-1].replace('-', ' ')



class Competitor(models.Model):
	brand = models.CharField('Brand Name', max_length=200, blank=True)
	color = models.CharField(max_length=200, blank=True)
	#size = models.CharField(max_length=200, blank=True)
	vendor = models.CharField(max_length=200, blank=True)
	site = models.CharField(max_length=200)
	price = models.DecimalField ('Product Price', decimal_places=2, max_digits=10, default=-1)
	update_dt = models.DateTimeField('date updated', auto_now_add=True)
	prod_key = models.ForeignKey(Product, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.prod_key.url.split('/')[-1].replace('-', ' ') + " - " + self.vendor