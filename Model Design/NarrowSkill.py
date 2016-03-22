#coding=utf-8
import time
import MySQLdb
import cPickle as pickle
import pandas as pd

t1 = time.time()

db = MySQLdb.connect("10.120.26.46","yang","iiizb104","project" )
cursor = db.cursor()
sql = 'SELECT jobno, content FROM project.jobstored'

ListIndex = []
ListContent = []

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        ListIndex.append(row[0])
        ListContent.append(row[1])

except Exception as e:
    print e.args

db.close


t2 = time.time()

print t2 - t1