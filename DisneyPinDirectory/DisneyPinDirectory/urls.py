from django.contrib import admin
from django.urls import path, include, re_path

from pages.urls import page_url_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'', include(page_url_patterns)),
]
