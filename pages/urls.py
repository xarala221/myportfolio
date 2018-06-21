from django.conf.urls import url
from pages.views import *
urlpatterns = [
  url(r'^$', HomeView.as_view(), name="home"),
  url(r"^contact/$", get_contact, name="contact"),
]