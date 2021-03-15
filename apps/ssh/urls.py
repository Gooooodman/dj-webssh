'''
@project : gops
@author  : lupuxiao
@contact : jiucows@gmail.com
@file    : urls.py
@time    : 2021-03-14 17:40:31
'''

from django.conf.urls import url

from .views import *

urlpatterns = [
    # url(r'do/$', do_task),
    url(r'host/$',host),
]