from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'blog'
urlpatterns = [
    url(r'^accounts/login/$', views.login_user, name = 'login_user'),
    url(r'^search/$', views.search, name='search'),
    url(r'^sortindexmz/$', views.sortindexmz, name='sortindexmz'),
    url(r'^sortindexrt/$', views.sortindexrt, name='sortindexrt'),
    url(r'^index/$', views.index, name='index'),

]