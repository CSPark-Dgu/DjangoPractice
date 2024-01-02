from django.urls import path, register_converter
from . import views
from .converters import DayConverter, MonthConverter, YearConverter

register_converter(YearConverter, "year")
register_converter(MonthConverter, type_name="month")
register_converter(DayConverter, type_name="day")

app_name = "instagram"

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("<int:pk>/", views.post_detail, name="post_detail"),
    path("archive/", views.post_archive, name="post_archive"),
    path("archive/<year:year>/", views.post_archive_year, name="post_archive_year"),
    path(
        "archive/<year:year>/<month:month>/",
        views.post_archive_month,
        name="post_archive_month",
    ),
    path(
        "archive/<year:year>/<month:month>/<day:day>/",
        views.post_archive_day,
        name="post_archive_day",
    ),
    # Make month and day parameters optional by adding '?'
    path(
        "archive/<year:year>/<month:month>/?",
        views.post_archive_month,
        name="post_archive_month_optional_day",
    ),
    path(
        "archive/<year:year>/<month:month>/<day:day>/?",
        views.post_archive_day,
        name="post_archive_day_optional",
    ),
]
