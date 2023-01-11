from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("blog", views.blog, name="blog"),
    path("show_blog/<str:pk>", views.show_blog, name="show_blog"),
    path("projects", views.projects_page, name="projects"),
    path("all_tags", views.tag_page, name="all_tags"),
    path("all_tags/<str:pk>", views.category_blogs, name="Category_blogs"),
    path("series", views.series, name="series"),
    path("show_series/<str:pk>", views.show_series, name="show_series")
]
