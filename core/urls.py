from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
] + i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('api/v1/career/', include('apps.career.urls')), 
    path('api/v1/main/', include('apps.main.urls')), 
    path('api/v1/projects/', include('apps.projects.urls')), 
    path('api/v1/news/', include('apps.news.urls')), 
    path('api/v1/service/', include('apps.service.urls')), 
)
