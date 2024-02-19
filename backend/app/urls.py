from django.urls import path
from . import views

urlpatterns = [
    path('scenarios', views.scenario_list, name='scenario_list'),
    path('scenarios/<int:pk>', views.scenario_detail, name='scenario_detail')
]