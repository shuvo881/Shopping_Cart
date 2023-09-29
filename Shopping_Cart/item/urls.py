from django.urls import path

from .views import details, search

urlpatterns = [
    path('<int:pk>', details, name='details'),
    path('search', search, name='search'),

]