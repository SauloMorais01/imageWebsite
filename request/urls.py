from django.urls import path
from . import views

app_name = 'request'

urlpatterns = [
    path('', views.Pay.as_view(), name='pay'),
    path('close-order/', views.CloseOrder.as_view(), name='closeOrder'),
    path('detail/', views.Detail.as_view(), name='detail'),
]
