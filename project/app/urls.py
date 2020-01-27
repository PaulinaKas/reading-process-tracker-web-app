from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views

from app import views

urlpatterns = [
    url(r'^lists/(\d+)/$', views.viewList, name='viewList'),
    url(r'^lists/(\d+)/add_book$', views.addBook, name='addBook'),
    url(r'^lists/new$', views.newList, name='newList'),

]
