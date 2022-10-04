from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def myview(request):
    resp = HttpResponse()
    resp.set_cookie('dj4e_cookie', '436e8382', max_age=1000)
    view_count = int(request.COOKIES.get('view_count',0)) + 1
    resp.set_cookie('view_count', view_count)
    resp.write('<p>Hello 436e8382</p><p>view count=%s</p>' %view_count)
    return resp
