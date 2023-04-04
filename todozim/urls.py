from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='list'),
    path('createList/', views.createList, name='createList'),
    path('detail/<int:id_list>/', views.detail, name='detail'),
    path('add_task/<int:id_list>/', views.add_task, name='add_task'),
    path('task/update_done_task/<int:id_task>/<int:status_task>', views.update_done_task, name='update_done_task'),
]