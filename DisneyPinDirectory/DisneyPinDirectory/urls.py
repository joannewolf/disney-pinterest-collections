from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from pages.api_urls import page_api_url_patterns
from pages.urls import page_url_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'', include(page_url_patterns)),
    re_path(r'', include(page_api_url_patterns)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
