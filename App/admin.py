from django.contrib import admin
from .models import Blog, Tag, Series, Project, Project_category
# Register your models here.

admin.site.register(Blog)

admin.site.register(Tag)

admin.site.register(Series)

admin.site.register(Project)

admin.site.register(Project_category)
