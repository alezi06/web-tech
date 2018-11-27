from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.test, name='test'),
    url(r'^(?P<num>\d+)/$', views.test, name='test'),
]