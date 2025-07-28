from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.add, name='add_task'),
    path('mark_as_done/<int:pk>', views.mark_as_done, name='mark_as_done'),
]