from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.profile, name='index'),
    url(r'^playagain', views.again, name='playagain'),
    # url(r'^answers', views.answers, name='answers'),

]