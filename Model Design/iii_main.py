#coding=utf-8
import WordTransform as wt
import json
import MySQLdb

#ngram 由wordTransform傳回會出現問題故寫在這裡
from nltk.util import ngrams
def ngram(x): #傳入List
    # sentence = x
    outary = []
    for n in range(1,5):
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

db = MySQLdb.connect("10.120.26.46","yang","iiizb104","project" )
cursor = db.cursor()

sql = "SELECT dict FROM project.dict where no = 3;"
cursor.execute(sql)
results = cursor.fetchone()
dic_transform = json.loads(results[0])

sql = "SELECT dict FROM project.dict where no = 2;"
cursor.execute(sql)
results = cursor.fetchone()
List_skill = json.loads(results[0])

sql = "SELECT dict FROM project.dict where no = 1;"
cursor.execute(sql)
results = cursor.fetchone()
List_skill26 = json.loads(results[0])

sql = "SELECT clusterVector FROM project.cluster;"
cursor.execute(sql)
clusterVec = cursor.fetchall()

#for test
tmpList = ['html','css','css','php','I','like','python','ror']

#將字解成 4-gram
tmpList = ngram(tmpList)

#相似字和錯別字轉換
tmpList = wt.changeWord(dic_transform, tmpList)

#刪除不需要的字
tmpList = wt.deleteWord(List_skill, tmpList)

#計算技能次數後回傳dict
skilldic = wt.dicToJson(tmpList)

#將技能存成JSON格式
skillJSON = json.dumps(skilldic, ensure_ascii=False)

#回傳分群結果
clusterNum = wt.getRecommendCluster(List_skill26, clusterVec, skilldic)

print clusterNum