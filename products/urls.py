from django.urls import path
from . import views

urlpatterns = [
    path('catalog/', views.catalog, name='catalog'),
    path('contact/', views.contact, name='contact'),
    path('sort_price/', views.sort_by_price, name='sort_price'),
    path('<int:pk>', views.ProductDetailView.as_view(), name='shop-details')
]