from django.urls import path
from views import home_view

url_patterns = [
    path('/home', home_view)
]