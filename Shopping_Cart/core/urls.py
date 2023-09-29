from django.urls import path

from .views import index, checkout

urlpatterns = [
    path('', index, name='index'),
    path('checkout/', checkout, name='checkout'),

]