# from django.conf.urls import url
# # from django.contrib import admin
# from django.conf.urls import include
# from . import views
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#
#
# from . import views
#
#
# urlpatterns = [
#     url(r'^$', views.index, name='index'),
#
# ]



from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index')]
