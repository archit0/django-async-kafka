from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

root_path = 'crawler'
url_with_docs = []

internal_api_root_path = f'{root_path}/internal'
internal_api = [

]

all_urls = url_with_docs + internal_api
schema_view = get_schema_view(
    openapi.Info(
        title="Crawler",
        default_version='v1',
        description="",
        terms_of_service="",
    ),
    public=False,
    patterns=all_urls,
    permission_classes=[permissions.IsAuthenticated],
)

urlpatterns = all_urls + [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='Documentation'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
