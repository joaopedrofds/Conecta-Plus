from django.urls import path
from ConectaPlusapp.views import teste 

urlpatterns = [
    path('', teste, name = 'teste'),
]
