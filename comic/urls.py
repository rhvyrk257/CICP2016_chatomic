from django.conf.urls import url
from . import views

urlpatterns = [
#    url(r'^annotate/$', views.annotate, name='annotate'),
    url(r'^$', views.index, name='index'),
]
