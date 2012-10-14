from django.conf.urls.defaults import *
from icetea.resource import Resource
                       
from handlers import TestHandler

eh = Resource(TestHandler)

urlpatterns = patterns('',
    url(r'^test/$', eh),
)        
