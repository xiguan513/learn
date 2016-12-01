from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import  reverse
# Create your views here.

"""
HttpResponse用来向页面返回内容
定义函数，第一个参数必须是request，与网页发来的请求有关，request变量包含get或post内容
"""

#http://127.0.0.1:8000
def index(request):
    return HttpResponse('欢迎光临，自强学堂！')

#http://127.0.0.1:8000/add/?a=4&b=10
def add(request):
    a=request.GET['a']
    b=request.GET['b']
    c=int(a)+int(b)
    return HttpResponse(str(c))

#http://127.0.0.1:8000/add2/3/123/
def add2(request,a,b):
    c=int(a)+int(b)
    return HttpResponse(str(c))

#http://127.0.0.1:8000/add/3/12/自动跳转到http://127.0.0.1:8000/new_add/3/12/
#通过urls中指定的访问url跳转
#url(r'^add/(\d+)/(\d+)/$',learn_views.old_add2_redirect),
#url(r'^new_add/(\d+)/(\d+)/$',learn_views.add2,name='add2'),
#
def old_add2_redirect(request,a,b):
    return HttpResponseRedirect(
        reverse('add2',args=(a,b))
    )

#通过访问http://127.0.0.1:8000/cal/显示cat.html的内容
def cal(request):
    return render(request,'cal.html')

#通过字典{'string'：string }给home.html页面传递变量
#在HTML中使用{{ }}（变量），功能类的，比如循环，条件判断是用 {%  %}（标签）
def home(request):
    tutolist=["HTMl","CSS","JS"]
    info_dict={"site":"自强学堂","count":"各种IT技术"}
    List=map(str,range(100))
    string='我在自强学堂学习django，用它来建设网站'
    return render(request,'home.html',{'string':string,'tutolist':tutolist,'info_dict':info_dict,"List":List})


def current_url_view_good(request):
    return HttpResponse("Welcome to the page at %s " % request.path )

def ua_display_good(request):
    try:
        ua=request.META
    except KeyError:
        ua='unknow'
    return HttpResponse("You browser is %s" % ua)
