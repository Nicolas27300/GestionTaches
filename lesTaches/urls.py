from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path(r'home/<param>', views.home, name='home'),
    path(r'listing', views.task_listing, name='listing')
]