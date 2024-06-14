from django.urls import path
from .views import hello_world

app_name = 'blog'

urlpatterns = [
    path('', hello_world,name='post_blog'),
]