from django.db import models
import uuid
from ckeditor.fields import RichTextField
# Create your models here.


class Base_model(models.Model):
    uid = models.UUIDField(
        default=uuid.uuid4, editable=False, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Series(Base_model):
    name = models.CharField(max_length=100)
    bio = models.TextField(default="")

    def __str__(self):
        return str(self.name)


class Tag(Base_model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Blog(Base_model):
    title = models.CharField(max_length=100)
    bio = models.CharField(max_length=500, blank=True, null=True)
    main_image = models.ImageField(upload_to="blog_images")
    introduction = RichTextField()
    image1 = models.ImageField(
        upload_to="blog_images", blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image2 = models.ImageField(
        upload_to="blog_images", blank=True, null=True)
    conclusion = RichTextField(blank=True, null=True)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return str(self.title)


class Project(Base_model):
    name = models.CharField(max_length=100)
    live_link = models.URLField(max_length=500, blank=True, null=True)
    github_link = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Project_category(Base_model):
    name = models.CharField(max_length=100)
    project = models.ManyToManyField(Project, blank=True)

    def __str__(self):
        return str(self.name)
