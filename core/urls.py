from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
] + i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('career/', include('apps.career.urls')), 
    path('main/', include('apps.main.urls')), 
    path('projects/', include('apps.projects.urls')), 
    path('news/', include('apps.news.urls')), 
    path('service/', include('apps.service.urls')), 
)
