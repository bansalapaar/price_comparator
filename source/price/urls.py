"""
If the url provided is emtpy then view.index is accessed otherwise if the url is search/ then view of mainSearch is accessed
"""
from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('search/',views.mainSearch,name='mainSearch')
]
