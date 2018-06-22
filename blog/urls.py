from django.conf.urls import url, include

from blog.views import *

urlpatterns = [
  url(r"^$", all_post, name="blog"),
  url(r"^detail/(?P<id>[0-9]+)/$", post_detail, name="detail"),
  url(r"^create/$", new_post, name="create"),
  url(r"^detail/(?P<id>[0-9]+)/edit/$", edit_post, name="update"),
  url(r"^detail/(?P<id>[0-9]+)/delete/$", delete_post, name="delete"),
  url(r'^tinymce/', include('tinymce.urls')),
]