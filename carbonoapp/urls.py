from django.urls import path, include
from .views import hello_home
from .views import hello_calc


urlpatterns = [
    path('', hello_home),
    path('calc/', hello_calc),
]