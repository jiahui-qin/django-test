from django.conf.urls import url  
from . import views
from django.contrib.auth import views as auth_views
from .views import dashboard

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='blog/login.html')),
    #url(r'^login/$', auth_views.login, name='login'),
    #url(r'^logout/$', auth_views.logout, name='logout'),
    #url(r'^logout-then-login/$', auth_views.logout_then_login, name='logout_then_login'),
    #url(r'^$', views.dashboard, name='dashboard'),

]