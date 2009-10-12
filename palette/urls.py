# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('palette.views',
    (r'^$', 'index'),
	(r'download.(?P<extension>.+)$', 'convert'),
	# (r'download.(?P<extension>.+)^$', 'convert'),
)
