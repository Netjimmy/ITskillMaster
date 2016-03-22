# -*- coding: utf-8 -*-
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from restaurants.models import Restaurant, Food
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

def menu(request,id):
    if id:
        restaurants = Restaurant.objects.get(id=id)
        return render_to_response('menu.html',locals())
    else:
        return HttpResponseRedirect("/restaurants_list/")
		
def meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>{0}</td><td>{1}</td></tr>'.format(k,v))
    return HttpResponse('<table>{0}</table>'.format('\n'.join(html)))

@login_required	
def list_restaurants(request):
    restaurants = Restaurant.objects.all()
    return render_to_response('restaurants_list.html',RequestContext(locals()))
	
def comment(request,id):
    if id:
	    r = Restaurant.objects.get(id=id)
    else:
        return HttpResponseRedirect("/restaurants_list/")
    errors = []
    if request.POST:
        visitor = request.POST['visitor']
        content = request.POST['content']
        email = request.POST['email']
        date_time = datetime.now()
        if any(not request.POST[k] for k in request.POST):
            errors.append('*有空白欄位,請不要留空')
        if '@'not in email:
            errors.append('* email格式不正確,請重新輸入')		
        if not errors:
            Comment.objects.create(visitor=visitor, email=email, content=content, date_time=date_time, restaurant=r)
            visitor, email, content=('', '', '')
    f = CommentForm()
    return render_to_response('comments.html',RequestContext(request, locals()))

def set_c(request):
    response = HttpResponse('Set your lucky_number as 8')
    response.set_cookie('lucky_number',8)
    return response

def get_c(request):
    if 'lucky_number' in request.COOKIES:
        return HttpResponse('Your lucky_number is {0}'.format(request.COOKIES['lucky_number']))
    else:
        return HttpResponse('No cookies.')
