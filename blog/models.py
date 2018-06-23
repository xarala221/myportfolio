from django.db import models
from django.db.models import permalink
from django.db.models.signals import pre_save
from django.urls import reverse
from django.utils.text import slugify
from tinymce import HTMLField


# Create your models here.
class Blog(models.Model):
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  title = models.CharField(max_length=2040)
  slug = models.SlugField(unique=True)
  image = models.ImageField(null=True, blank=True)
  video = models.CharField(max_length=2040, null=True, blank=True)
  content =  HTMLField('Content')
  published_at = models.DateTimeField(auto_now=False, auto_now_add=False)
  updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

  @permalink
  def get_absolute_url(self):
      return ('blog-detail', None, {'slug': self.slug})

  def __str__(self):
    return self.title


#slug automatic
"""
def create_slug(post, new_slug=None):
    slug = slugify(post.title)
    if new_slug is not None:
        slug = new_slug
    qs = Blog.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(post, new_slug=new_slug)
    return slug


'''
unique_slug_generator from Django Code Review #2 on joincfe.com/youtube/
'''
from .utils import unique_slug_generator

def pre_save_post_receiver(sender, post, *args, **kwargs):
    if not post.slug:
        # post.slug = create_slug(post)
        post.slug = unique_slug_generator(post)
"""