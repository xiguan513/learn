from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
import datetime


# Create your views here.

def hello(request,offset):
    #return HttpResponse("Hello world")
    try:
        offset=int(offset)
    except ValueError:
        raise Http404()
    now=datetime.datetime.now()+datetime.timedelta(hours=offset)
    #assert False查看内部变量
    html="<html><body>In %s hour(s),it whill be %s.</body></html>" % (offset,now)

    return HttpResponse(html)


