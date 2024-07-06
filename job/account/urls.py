from django .urls import path
from .views import loginview,registerview
from account import views

urlpatterns=[
    path("log",loginview,name='log'),
    path("reg",registerview.as_view(),name="reg")
]