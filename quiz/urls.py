from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    
    url(r'^(?P<exam_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<exam_id>[0-9]+)/score/$', views.score, name='score'),
]
