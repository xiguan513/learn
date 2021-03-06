"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from learn import views as learn_views

urlpatterns = [
    url(r'^$',learn_views.index),
    url(r'^add/$',learn_views.add,name='add'),
    url(r'^add2/(\d+)/(\d+)/$',learn_views.add2,name='add2'),
    url(r'^add/(\d+)/(\d+)/$',learn_views.old_add2_redirect),
    url(r'^new_add/(\d+)/(\d+)/$',learn_views.add2,name='add2'),
    url(r'cal/',learn_views.cal,name='cal'),
    url(r'^home/$',learn_views.home,name='home'),
    url(r'^current/(\w+)/$',learn_views.current_url_view_good,name='current_url_view_good'),
    url(r'^ua/$',learn_views.ua_display_good,name='ua'),
    url(r'^admin/', admin.site.urls),
]
