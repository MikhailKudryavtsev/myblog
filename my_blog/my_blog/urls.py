from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('blog.urls')),
    path('auth/', include('authorization.urls')),
    path('admin/', admin.site.urls),
]
