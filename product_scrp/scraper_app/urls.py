from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index_URL'),
	url(r'^products/$', views.addProduct.as_view(), name='add_product_URL'),
	url(r'^competitor/$', views.addCompetitor.as_view(), name='add_competitor_URL'),
	url(r'^list-product/$', views.viewProduct.as_view(), name='product_list_URL'),
	url(r'^list-competitor/$', views.viewCompetitor.as_view(), name='competitor_list_URL'),
	url(r'^update/$', views.UpdatePrices, name='update_URL'),
	url(r'^compare/$', views.ComparePrices, name='compare_URL'),
]