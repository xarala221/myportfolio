from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Blog
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