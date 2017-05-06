from django.conf.urls import url

from polls import views

urlpatterns = [
    url(r'^', 'loteria.views.index', name='index'),


]
