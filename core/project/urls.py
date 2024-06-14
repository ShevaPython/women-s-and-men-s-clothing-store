from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('account/', include('core.accounts.urls'),name='profile'),
    path('', include('core.shop.urls', namespace='shop')),
    path('blog/', include('core.blog.urls', namespace='blog'))
]
