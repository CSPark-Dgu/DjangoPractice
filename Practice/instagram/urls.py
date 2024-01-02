from django.urls import path, re_path, register_converter

from . import views
from .converters import DayConverter, MonthConverter, YearConverter

register_converter(YearConverter, 'year')
register_converter(MonthConverter, type_name="month")
register_converter(DayConverter, type_name="day")
app_name = "instagram"


urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("<int:pk>/", views.post_detail, name="post_detail"),
    # re_path(r"^new/$", views.post_detail),
    path("archive/", views.post_archive, name="post_archive"),
    path("archive/<year:year>/", views.post_archive_year, name="post_year_archive"),
    path("archive/<year:year>/<month:month>/", views.post_archive_month, name="post_archive_month" ),
    path("archive/<year:year>/<month:month>/<day:day>/", views.post_archive_day, name="post_archive_day"),
]
