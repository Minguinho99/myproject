from django.conf.urls import url
from . import views


usrlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
