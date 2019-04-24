from django.conf.urls import url
from basic_app import views

#TEMPLATE TAGGING
app_name = 'basic_app'   # important this is the first term in the template tag

urlpatterns= [
    url(r'^relative/$', views.relative,name='relative'),
    url(r'^other/$', views.other,name='other'),
]
