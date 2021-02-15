from django.conf.urls import url
from . import views
#from django.contrib.auth.views import login
from django.urls import path, include
from iipinmotion.views import (login_view_before,login_view,registation_view)

app_name = 'iipinmotion'

urlpatterns = [url(r'^$', views.IndexView.as_view(), name='IndexView'),
               url(r'^(?P<pk>[0-9]+)/$',
                   views.DetailedView.as_view(), name='detail'),
 				url(r'^login/', login_view_before, name='login'),
 				url(r'^registrationForm/', registation_view, name='login'),
                ]

#urlpatterns += [
#    path('iipinmotion/', include('django.contrib.auth.urls')),
#]
