"""HouseHelper URL Configuration

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
from House.views import factor_choice, house_detail, house_result, query_result, login, register, factor_empty
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', factor_choice),
    url(r'^result/$', house_result),
    url(r'^post/(?P<pk>\d+)/$', house_detail, name='h_detail'),
    url(r'^qresult/$', query_result),
    url(r'^login/', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout'),
    url(r'^register/$', register, name='register'),
    url(r'^factor_empty', factor_empty),
]
