from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^answers', views.answers, name='answers'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^$', views.index, name='index'),

]
