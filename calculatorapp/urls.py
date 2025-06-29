from django.urls import path
from . import views
urlpatterns = [
    path('standard/', views.standard_calculator, name='standard'),
    path('',views.home, name="home")
]
