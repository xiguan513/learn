#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from django.http import HttpResponse
import datetime
from django.http import Http404

def hello(request):
    return HttpResponse("Hello world!")

def current_datetime(request):
    now=datetime.datetime.now()
    html="<html><body>It IS time %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request,offset):
    try:
        offset=int(offset)
    except ValueError:
        raise Http404()

    dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
    #assert False
    html="<html><body>In %s hour(s),it will be %s.</body></html>" % (offset,dt)
    return HttpResponse(html)


