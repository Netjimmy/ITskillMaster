# -*- coding: utf-8 -*-
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
import unicodedata
#def here(request):
    #return HttpResponse('媽,我在這! ')
	
def welcome(request):
    if 'user_name' in request.GET and request.GET['user_name'] != '':
        return HttpResponse('Welcome!~'+request.GET['user_name'])
    else:
        return render_to_response('welcome.html',locals())
def login(request):

    if request.user.is_authenticated():
        return HttpResponseRedirect('/homepage/')
		
    username = request.POST.get('username','')
    password = request.POST.get('password','')
	
    user = auth.authenticate(username=username, password=password)
	
    if user is not None	and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/homepage/')
    else:
        return render_to_response('login.html', RequestContext(request, locals()))	

def index(request):
    return render_to_response('index.html', RequestContext(request, locals()))

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/accounts/login/')
    else:
        form = UserCreationForm()
    return render_to_response('register.html', RequestContext(request, locals()))

def homepage(request):
    return render_to_response('homepage.html', RequestContext(request, locals()))
	

def skills(request):
    return render_to_response('skills.html', RequestContext(request, locals()))
	
def index(request):
    return render_to_response('index.html', RequestContext(request, locals()))
	
def map(request):
    return render(request,'map.html')
	
def Recommend(request):
    return render(request,'Recommend.html')

# def TaiwanMap_test2(request):
    # return render(request,'TaiwanMap_test2.html',locals())
