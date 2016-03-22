#coding=utf-8
import cPickle as pickle
from nltk.util import ngrams
import json
import numpy as np
import numpy.linalg as LA
import random

dic_transform = pickle.load(file('dic/dic_transform_v2.data'))
set_skill = pickle.load(file('dic/set_skill_final.data'))
set_skill26 = pickle.load(file('dic/set_skill_v8_500.data'))
list_skill26 = sorted(list(set_skill26))

def changeWord(x): #傳入list
    for word in x:
        if word in dic_transform:
            loc = x.index(word)
            x[loc] = dic_transform[word]
    return x  #回傳list

def deleteWord(x): #傳入list
    x = [word for word in x if word in set_skill26]
    return x

def ngram(x): #傳入List
    # sentence = x
    outary = []
    for n in range(2,5):
        grams = ngrams(x, n)
        for gram in grams:
            soutstr = ''
            for i in range(0,n):
                if len(soutstr) == 0:
                    soutstr = gram[i]
                else:
                    soutstr = soutstr + ' ' + gram[i]
            outary.append(soutstr)
    return outary #回傳list

def dicToJson(x):
    tmpDic = {}
    for each in x:
        if each not in tmpDic:
            tmpDic[each] = 1
        else:
            tmpDic[each] += 1

    return tmpDic #回傳dict

#test sample
# my_randoms = []
# for each in range(26):
#     my_randoms.append(random.random())

def getRecommendCluster(List_skill26, clusterVec, a): #傳入JSON
    tmpList = []
    for each in List_skill26:
        if each in a:
            tmpList.append(a[each])
        else:
            tmpList.append(0)

    #若是空值陣列返回None
    if tmpList == np.zeros(len(List_skill26)).tolist():
        return None
    else:
        tmpCom = []
        for row in clusterVec:
            vec = json.loads(row[0])
            tmpCom.append(getDocDistance(vec, tmpList))

        # print ('max value:', max(tmpCom))
        return [i for i, j in enumerate(tmpCom) if j == max(tmpCom)][0] #傳出cluster數字

def getDocDistance(a, b):
    if LA.norm(a)==0 or LA.norm(b)==0:
        return -1
    return round(np.inner(a, b) / (LA.norm(a) * LA.norm(b)), 4)

#test sample
# a = {"java": 1, "c": 1, "c++": 1, "linux": 1, "oracle": 1, "freebsd": 1, "solaris": 1, "windows": 3, "windows nt": 1}
# print getRecommendCluster(a)
