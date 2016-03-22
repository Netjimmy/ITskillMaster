import numpy as np
import numpy.linalg as LA
import random
import MySQLdb
import json

def getDocDistance(a, b):
    if LA.norm(a)==0 or LA.norm(b)==0:
        return -1
    return round(np.inner(a, b) / (LA.norm(a) * LA.norm(b)), 4)

#test sample
my_randoms = []
for each in range(26):
    my_randoms.append(random.random())

def getRecommendCluster(a): #輸入向量
    db = MySQLdb.connect("10.120.26.46","yang","iiizb104","project" )
    cursor = db.cursor()
    sql = "SELECT clusterVector FROM project.cluster;"

    cursor.execute(sql)
    results = cursor.fetchall()

    tmpCom = []
    for row in results:
        vec = json.loads(row[0])
        tmpCom.append(getDocDistance(vec, a))

    # print ('max value:', max(tmpCom))
    return [i for i, j in enumerate(tmpCom) if j == max(tmpCom)][0]

def getRecommendSKill(vec, cluster): #分別輸入向量和群
    db = MySQLdb.connect("10.120.26.46","yang","iiizb104","project" )
    cursor = db.cursor()
    sql = "SELECT clusterVector FROM project.cluster where cID = {};".format(cluster)
    sql2 = "SELECT dict FROM project.dict where no = 1;"

    cursor.execute(sql)
    Vector = cursor.fetchone()
    cVector = json.loads(Vector[0])

    cursor.execute(sql2)
    skills = cursor.fetchone()
    skill_list = json.loads(skills[0])

    # vec = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]

    ind = [i for i, j in enumerate(vec) if j == 0]

    skill_list_new = []
    cVector_new = []

    for each in ind:
        skill_list_new.append(skill_list[each])
        cVector_new.append(cVector[each])

    recSkill = skill_list_new[cVector_new.index(max(cVector_new))]

    return recSkill