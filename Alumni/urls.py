from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('', include('schools.urls')),
    path('api/offers/', include('offers.urls')),


]

