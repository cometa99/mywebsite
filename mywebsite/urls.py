"""mywebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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

from django.conf.urls import include, url
from django.contrib import admin
from loteria import views

urlpatterns = [
        url(r'^polls/', include('polls.urls')),
        url(r'^admin/', include(admin.site.urls)),
        url(r'^personal/', include('personal.urls')),
        url(r'^$', 'personal.views.home', name='home'),
        url(r'^blog/', include('blog.urls')),
        url(r'^contact/', 'personal.views.contact', name='contact'),
        url(r'^$/', 'blog.views.index', name='index'),
        url(r'^$/', 'polls.views.index', name='index'),
        url(r'^loteria/', include('loteria.urls')),
        url(r'^$/', 'loteria.views.index', name='index'),
        url(r'^$/', 'liveblog.views.index', name='index'),
        url(r'^liveblog/', include('liveblog.urls')),
        url(r'^tlc/', include('tlc.urls')),


]
