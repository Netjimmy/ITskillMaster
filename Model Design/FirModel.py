#coding=utf-8
import time
import pandas as pd
import DicToChangeWord
import numpy as np

ts = time.time()

#匯入技能原始資料
rfile=open('skills_all.txt','r')
raw = rfile.readlines()
rfile.close()
rawData=raw[0].split(',')

#相似字轉為同一個字
rawData = DicToChangeWord.changeWord(rawData)

#所有原始技能
rawSkillSet = set()
for sen in rawData:
    for word in sen:
        if word not in rawSkillSet:
            rawSkillSet.add(word)

rawSkillList = sorted(rawSkillSet)

#為每筆資料建立dic並計算技能出現次數

zeroDic = {}
for each in rawSkillSet:
    zeroDic[each] = 0

List_of_dic = []
for sen in rawData:
    tempDic = zeroDic.copy()
    for word in sen:
        if word in rawSkillSet:
            tempDic[word] += 1
    List_of_dic.append(tempDic)

#建立2-D list
list_of_lists = []
for row in List_of_dic:
    tempList = []
    for each in rawSkillList:
        tempList.append(row[each])
    list_of_lists.append(tempList)

#轉為panda dataframe格式
rawDF = pd.DataFrame(list_of_lists, columns=rawSkillList)

#技能轉向量 (C跟C++會不見的套件)
# from sklearn.feature_extraction.text import CountVectorizer
# vectorizer = CountVectorizer()
# skill_matrix = vectorizer.fit_transform(skillset)
# skill=vectorizer.get_feature_names()

# print skill

# skillFilter = set()
#
# skill_ndarray = skill_matrix.sum(0).view(type=np.ndarray)[0]
#
# for each in range(0, len(skill_ndarray)-1, 1):
#     if skill_ndarray[each] <= 1:
#         skillFilter.add(skill[each])
#
# # print skill_matrix.toarray())
#
# skill_set = set(skill)
#
# #5000常用字 + skillFilter踢字
# wfile=open('5000words.txt','r')
# dicCommon = set()
#
# for i in wfile.readlines():
#     dicCommon.add(i[:-1])
# wfile.close()
#
# fskill_set=(skill_set.difference(dicCommon | skillFilter)) #skill_減去(兩個set合在一起)
#
# fskill_list=sorted(fskill_set)
#
# print len(fskill_list)
#
# wfile=open('skills_all_filter.txt','w')
# for each in fskill_list:
#     wfile.write('{}\n'.format(each))
# wfile.close()

# # 每一筆資料中 skill - fskill
# tmp=[]
#
# for each in skill:
#     if each not in fskill_set:
#         tmp.append(skill.index(each))
#
# new_skill_matrix=np.delete(skill_matrix.toarray(), np.s_[tmp], axis=1)
#
# #TFIDF
# from sklearn.feature_extraction.text import TfidfTransformer
# transformer = TfidfTransformer()
# tfidf = transformer.fit_transform(new_skill_matrix)
#
# print tfidf.toarray()

te = time.time()

print te - ts