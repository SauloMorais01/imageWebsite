from django.urls import path
from . import views

app_name = 'perfil'

urlpatterns = [
    path('', views.Login.as_view(), name='login'),
    path('sign-in/', views.SignIn.as_view(), name='signIn'),
    path('update/', views.Update.as_view(), name='update'),
    path('logout/', views.Logout.as_view(), name='logout'),
]
