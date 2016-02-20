from django.conf.url import url, patterns, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

]
