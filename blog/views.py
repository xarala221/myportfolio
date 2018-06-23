from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic import ListView, DetailView
from blog.models import Blog
from blog.forms import BlogForm
from django.utils import timezone
# Create your views here.
def all_post(request):
  all_post = Blog.objects.all().order_by('-published_at')
  paginator = Paginator(all_post, 10)
  page = request.GET.get('page')
  posts = paginator.get_page(page)

  title = "Welcome to my  blog"
  context ={
    "posts": posts,
    "title": title
  }
  return render(request, "blog/all_post.html", context)

"""
class BlogDetail(DetailView):
    model = Blog
    template_name='blog/post_detail.html'
"""
def post_detail(request, slug):
  post = get_object_or_404(Blog, slug=slug)
  context = {
      "post": post
  }
  return render(request, "blog/post_detail.html", context)



def new_post(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    if not request.user.is_authenticated:
        raise Http404
    title = "Create"
    if request.method=="POST":
        form = BlogForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_at = timezone.now()
            post.save()
            return redirect(post.get_absolute_url())
    else:
        form = BlogForm()
        return render(request, "blog/create_form.html", {"form": form, "title": title})

def edit_post(request, slug):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    if not request.user.is_authenticated:
        raise Http404
    title = "Update"
    post = get_object_or_404(Blog, slug=slug)
    if request.method=="POST":
        form = BlogForm(request.POST or None, request.FILES or None, instance = post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.updated_at = timezone.now()
            post.save()
            return redirect(post.get_absolute_url())
    else:
        form = BlogForm(instance = post)
        return render(request, "blog/create_form.html", {"form": form, "title": title})

def delete_post(request, slug):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    if not request.user.is_authenticated:
        raise Http404
    if request.user.is_superuser:
        post = get_object_or_404(Blog, slug=slug)
    else:
        post = get_object_or_404(Blog, slug=slug, user=request.user)
    if request.method=="POST":
        post.delete()
        return redirect('list')
    else:
        return render(request, "blog/blog_delete.html", {"post": post})
