from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("app/", include("app.urls")),
    path("admin/", admin.site.urls),
]

if "debug_toolbar" in settings.INSTALLED_APPS:
    import debug_toolbar

    urlpatterns.append(path("__debug__/", include(debug_toolbar.urls)))
