from django.db import models
from tinymce import HTMLField
# Create your models here.
class Blog(models.Model):
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  title = models.CharField(max_length=2040)
  image = models.ImageField(null=True, blank=True)
  video = models.CharField(max_length=2040, null=True, blank=True)
  content =  HTMLField('Content')
  published_at = models.DateTimeField(auto_now=False, auto_now_add=False)
  updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

  def __str__(self):
    return self.title