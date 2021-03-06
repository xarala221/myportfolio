from django.conf.urls import url, include

from blog.views import *

urlpatterns = [
  url(r"^$", all_post, name="list"),
  url(r"^create/$", new_post, name="create"),
  url(r"^(?P<slug>[^\.]+).html/edit$", edit_post, name="update"),
  url(r"^(?P<slug>[^\.]+).html/delete$",  delete_post, name="delete"),
  url(r"^(?P<slug>[^\.]+).html/$", post_detail, name="blog-detail"),
]