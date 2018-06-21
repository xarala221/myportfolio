from django.db import models

# Create your models here.
class Contact(models.Model):
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=200)
  message = models.TextField()
  timestamp = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.email
