from django.shortcuts import render, redirect
from .models import Blog, Project_category, Project, Tag, Series
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, 'index.html')


def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, "blog.html", context)


def show_blog(request, pk):
    blog = Blog.objects.filter(uid=pk).first()
    context = {'blog': blog}
    return render(request, 'show_blog.html', context)


def projects_page(request):
    all_category = Project_category.objects.all()
    context = {'all_category': all_category}
    return render(request, 'projects.html', context)


def tag_page(request):
    all_tags = Tag.objects.all()
    context = {'all_tags': all_tags}
    return render(request, 'tags.html', context)


def category_blogs(request, pk):
    tag = Tag.objects.filter(name=pk).first()
    blogs = Blog.objects.filter(tag=tag)
    count = Blog.objects.filter(tag=tag).count()
    context = {'blogs': blogs, 'name': pk, 'count': count}
    return render(request, 'Category_blog.html', context)


def series(request):
    all_series = Series.objects.all()
    context = {'all_series': all_series}
    return render(request, 'series.html', context)


def show_series(request, pk):
    try:
        print(pk)
        series = Series.objects.get(name=pk)
        blogs = Blog.objects.filter(series=series)
        context = {"blogs": blogs, "series": series}
        return render(request, 'show_series.html', context)
    except Exception as e:
        messages.warning(request, "Series Not Found")
        print(e)
        return redirect("series")
