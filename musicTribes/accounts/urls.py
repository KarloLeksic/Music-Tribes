from urllib.parse import urlparse
from django.urls import URLPattern, path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('sign-up', views.SignUpView.as_view(), name='signup'),   
    path('<int:user_id>/', views.profile, name='profile'),
]