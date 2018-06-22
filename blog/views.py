from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from blog.models import Blog
from blog.forms import BlogForm
from django.utils import timezone
# Create your views here.
def all_post(request):
  all_post = Blog.objects.all().order_by('-published_at')
  title = "Latest articles"
  context ={
    "all_post": all_post,
    "title": title
  }
  return render(request, "blog/all_post.html", context)

def post_detail(request, id):
  post = get_object_or_404(Blog, id=id)
  return render(request, "blog/post_detail.html", {"post": post})



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
            return redirect("blog")
    else:
        form = BlogForm()
        return render(request, "blog/create_form.html", {"form": form, "title": title})
def edit_post(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    if not request.user.is_authenticated:
        raise Http404
    title = "Update"
    post = get_object_or_404(Blog, id=id)
    if request.method=="POST":
        form = BlogForm(request.POST or None, request.FILES or None, instance = post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.updated_at = timezone.now()
            post.save()
            return redirect("blog")
    else:
        form = BlogForm(instance = post)
        return render(request, "blog/create_form.html", {"form": form, "title": title})

def delete_post(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    if not request.user.is_authenticated:
        raise Http404
    if request.user.is_superuser:
        post = get_object_or_404(Blog, id=id)
    else:
        post = get_object_or_404(Blog, id=id, user=request.user)
    if request.method=="POST":
        post.delete()
        return redirect('blog')
    else:
        return render(request, "blog/blog_delete.html", {"post": post})