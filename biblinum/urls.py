from django.contrib import admin
from django.urls import include, path

from domain.ninja_api import urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("domain/", include("domain.urls")),
    path("ninja/", include(urls))

]
