from django.conf.urls import url

from blog.views import *

urlpatterns = [
  url(r"^$", all_post, name="blog"),
  url(r"^detail(?P<id>[0-9]+)/$", post_detail, name="detail"),
]