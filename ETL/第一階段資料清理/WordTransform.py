# coding=utf-8
import cPickle as pickle
from nltk.util import ngrams
import json

dic_transform = pickle.load(file('dic_transform_v2.data'))
set_skill = pickle.load(file('set_skill_final.data'))

def changeWord(x):  # 傳入list
    for word in x:
        if word in dic_transform:
            loc = x.index(word)
            x[loc] = dic_transform[word]
    return x   # 回傳list

def deleteWord(x):  # 傳入list
    x = [word for word in x if word in set_skill]
    return x

def ngram(x):  # 傳入List
    # sentence = x
    outary = []
    for n in range(2, 5):
        grams = ngrams(x, n)
        for gram in grams:
            soutstr = ''
            for i in range(0,n):
                if len(soutstr) == 0:
                    soutstr = gram[i]
                else:
                    soutstr = soutstr + ' ' + gram[i]
            outary.append(soutstr)
    return outary  # 回傳list

def dicToJson(x):
    tmpDic = {}
    for each in x:
        if each not in tmpDic:
            tmpDic[each] = 1
        else:
            tmpDic[each] += 1

    return json.dumps(tmpDic, ensure_ascii=False)  # 回傳JSON字串
