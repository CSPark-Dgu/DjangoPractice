"""
URL configuration for Practice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('instagram/', include('instagram.urls'))
"""
import os
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from dotenv import load_dotenv
from django.views.generic import TemplateView, RedirectView

load_dotenv()
admin_url = os.getenv("ADMIN_URL")

urlpatterns = [
    # path("", TemplateView.as_view(template_name="root.html"), name="root"),
    path(
        "",
        RedirectView.as_view(
            # url="/instagram/"),
            pattern_name="instagram:post_list"
        ),
        name="root",
    ),
    path(admin_url, admin.site.urls),  # URL Reverse
    path("instagram/", include("instagram.urls")),
    path("accounts/", include("accounts.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar

    urlpatterns += [
        re_path(r"^__debug__", include(debug_toolbar.urls)),
    ]
# settings.MEDIA_ROOT
# settings.MEDIA_URL
