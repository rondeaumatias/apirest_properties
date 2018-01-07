from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^Persons/', views.PersonList.as_view()),
    url(r'^PersonDetails/(?P<pk>[0-9]+)/$', views.PersonDetails.as_view()),
    url(r'^Properties/', views.PropertyList.as_view()),
    url(r'^PropertyDetails/(?P<pk>[0-9]+)/$', views.PropertyDetails.as_view()),
]
