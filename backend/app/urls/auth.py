from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from app import views

app_name = 'backend'

urlpatterns = [
    path('auth-check', views.AuthCheck.as_view(), name='auth_check'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('expire-session/<str:session_key>/', views.expire_session_view, name='expire_session'),
]

urlpatterns = format_suffix_patterns(urlpatterns)