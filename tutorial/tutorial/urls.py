"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

from apirest import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^inmu/', include('apirest.urls')),
    #url(r'^Persons/', views.PersonList.as_view()),
    #url(r'^PersonDetails/(?P<pk>[0-9]+)/$', views.PersonDetails.as_view()),
    #url(r'^Properties/', views.PropertyList.as_view()),
    #url(r'^PropertyDetails/(?P<pk>[0-9]+)/$', views.PropertyDetails.as_view()),
]
