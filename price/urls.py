from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('search/',views.mainSearch,name='mainSearch')
]