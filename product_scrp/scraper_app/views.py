from django.shortcuts import render
from django.http import HttpResponse
from scraper_app.models import Product, Competitor
from readprd import readxls


from django.shortcuts import render, redirect
from . models import Product, Competitor
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django import forms
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.db import models
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from prices import get_price

# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file

class UploadFileForm(forms.Form):
    file  = forms.FileField()


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            readxls(request.FILES['file'].read())
            return render(request, 'upload.html')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})



def index(request):
	return render(request, 'base.html')

class viewProduct(ListView):
	model = Product
	template_name = 'product_list.html'
	
class viewCompetitor(ListView):
	model = Competitor
	template_name = 'competitor_list.html'
	
class addProduct(CreateView):
	model = Product
	fields = ['brand', 'code', 'color', 'url', 'price', 'currency']
	template_name = 'add_product.html'
	success_url = reverse_lazy('index_URL')
	
class addCompetitor(CreateView):
	model = Competitor
	fields = '__all__'
	template_name = 'add_product.html'
	success_url = reverse_lazy('index_URL')


def UpdatePrices(request):
	if request.method == 'POST':
		for comp in Competitor.objects.all():
			pr = get_price(comp.site)
			comp.price = pr
			comp.save()
		for prd in Product.objects.all():
			pr = get_price(prd.url)
			prd.price = pr
			prd.save()
			
		print('Prices scraped')
		return render(request, 'update.html')
	return render(request, 'update.html')
	
def ComparePrices(request):
	rows = list()

	for Prod in Product.objects.all():
		rowdict = dict()
		rowdict['Product'] = str(Prod)
		rowdict['product_price'] = Prod.price

		for compr in Competitor.objects.filter(prod_key=Prod):
			color = 'rgba(0, 0, 0, 0)'
			if compr.price == -2.00:
				prc = 'Error'
			elif compr.price == -1.00:
				prc = 'Mining not attempted'
			else:
				prc = compr.price
				color = 'rgba(200, 0, 0, 0.3)' if compr.price < Prod.price else 'rgba(0, 200, 0, 0.3)'
				
			rowdict[''.join(compr.vendor.split()).lower() + '_price'] = prc
			rowdict[''.join(compr.vendor.split()).lower() + '_color'] = color

		rows.append(rowdict)
	

	return render(request, 'compare.html', context={'Rows': rows})
