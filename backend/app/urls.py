from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'backend'

urlpatterns = [
    re_path('scenarios', views.ScenarioList.as_view(), name='scenario_list'),
    re_path('scenarios/<int:pk>', views.ScenarioDetail.as_view(), name='scenario_detail'),
    re_path('vocals/<int:pk>', views.ScenarioVocals.as_view(), name='scenario_vocals'),
    re_path('media/<int:pk>', views.ScenarioMedia.as_view(), name='scenario_media'),
    re_path('images/<int:pk>', views.ScenarioImages.as_view(), name='scenario_images'),
    re_path('export/<int:pk>', views.ScenarioExport.as_view(), name='scenario_export')
]

urlpatterns = format_suffix_patterns(urlpatterns)