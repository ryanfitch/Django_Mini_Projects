from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^profile/$', views.profile, name='profile'),
    url(r'^$', views.profile, name='index'),
    url(r'^answers', views.answers, name='answers'),

]
