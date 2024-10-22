from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.ProductList.as_view(), name='list'),
    path('<slug>', views.Detail.as_view(), name='detail'),
    path('add-to-cart/', views.AddToCart.as_view(), name='addToCart'),
    path('remove-to-cart/', views.RemoveToCart.as_view(), name='removeToCart'),
    path('cart/', views.Cart.as_view(), name='cart'),
    path('finish/', views.Finish.as_view(), name='finish'),
]
