from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('colors/', include('colors.urls')),
    path('admin/', admin.site.urls),
]
