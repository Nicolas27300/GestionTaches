from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    path('', views.list, name='list'),
    path('detail/<int:cid>', views.detail, name='detail'),
    path('edit/<int:cid>', views.edit, name='edit'),
    path('editdetail/<int:cid>', views.editdetail, name='editdetail'),
    path('delete/<int:cid>', views.remove, name='delete')
]