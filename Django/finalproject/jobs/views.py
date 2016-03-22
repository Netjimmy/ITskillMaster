# -*- coding: utf-8 -*-
import json
import csv
# from __future__ import unicode_literals
from django.utils import timezone
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render_to_response, render
from jobs.models import Job
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core import serializers
import os

def JobList(request):
    jobs = Job.objects.filter(cluster = 2)
    return render_to_response('JobList.html',locals())
	
def jobRecommend(request):
    # jobs = Job.objects.filter(skill__contains='python')
    jobs = Job.objects.filter(cluster=13)[0:20]
    return render_to_response('jobRecommend.html',locals())
	
# def jobRecommend(request):
    # a = []
    # skill = request.POST.getlist('id',[])
    #a = matchskill(skill)
    # return a
    # skill_all = [".net", "ajax", "android", "app", "asp.net", "c", "c#", "c#.net", "c++", "css", "html", "ios", "java", "javascript", "jquery", "jsp", "linux", "mysql", "objective-c", "php", "python", "sql", "unix", "visualbasic", "xml"]
    # count = 0
    # for i in skill_all:
        # if i in skill:
            # a[count] = 1
        # else:
            # a[count] = 0
        # count + 1
    # a =[0,1,0,1,0,1,1,0]
    # skill = request.POST.getlist('id',[])
    # java = Job.objects.filter(skill__contains=skill)
    # return render_to_response('jobRecommend.html',locals())
	
# def jobRecommend(request):
    # jobs = Job.objects.filter(cluster =13)[0:20]
    # return render_to_response('jobRecommend.html', locals())

#def matchskill(selectskill):
    # # import cPickle as pickle
    # # import MySQLdb
    # # import json
    # 連MySQL取26個技能start==============
    # # db = MySQLdb.connect("10.120.26.46","yang","iiizb104","project" )
    # # cursor = db.cursor()
    # # sql = "SELECT dict FROM project.dict where no = '1';"

    # 执行SQL语句
    # # cursor.execute(sql)
    # 获取所有记录列表
    # # resultdic = cursor.fetchall()
    # # dic = resultdic[0]
    # # list_skill = json.loads(dic[0])
    # # db.close()
    # 連MySQL取26個技能start==============
    # set_skill = pickle.load(file('JsonToArray/set_skill_v2_300.data'))
    
    # print list_skill
    # print "--------------------------"
    # # b = []
    # # for i in list_skill:
        # # if i in selectskill:
            # # b.append(1)
        # # else:
            # # b.append(0)
    # # return b


	
	
def TaiwanMap_test2(request):
    return render(request,'TaiwanMap_test2.html',locals())


# Create your views here.
