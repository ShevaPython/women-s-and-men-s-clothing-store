from django.urls import path
from .views import profile

app_name = 'accounts'  # Указываем имя пространства имён

urlpatterns = [
    path('profile/', profile,name='profile'),
]