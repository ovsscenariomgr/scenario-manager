from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('scenarios', views.ScenarioList.as_view(), name='scenario_list'),
    path('scenarios/<int:pk>', views.ScenarioDetail.as_view(), name='scenario_detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)