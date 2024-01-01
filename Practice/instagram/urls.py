from django.urls import path, re_path

from . import views


app_name = "instagram"

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("<int:pk>/", views.post_detail, name="post_detail"),
    # re_path(r"^new/$", views.post_detail),
]
