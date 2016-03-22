# coding=utf-8

import json
import MySQLdb
import sys

reload(sys)
sys.setdefaultencoding("utf-8")  # 避免字型轉碼錯誤

filename = 'C:/Users/BigData/Desktop/skill.txt'
# filename = 'C:/Users/BigData/Desktop/skill.csv'

f = open(filename, 'w')

db = MySQLdb.connect(host="localhost", user="root", passwd="iiizb104", db="project")
db.set_character_set('utf8')

c = db.cursor()
c.execute("SET names utf8")
sql_query = "SELECT skill FROM project.jobstorage WHERE skill NOT REGEXP '{}';"
# sql_query = "SELECT skill26 FROM project.jobstorage WHERE skill26 NOT REGEXP '{}';"

c.execute(sql_query)

row = c.fetchall()  # 整個資料庫為一個list，而每筆個別資料被視為一個list中的元素。

for i in row:
    skill = json.loads(i[0])
    skillList = []
    rowData = ''
    for key in skill:
        rowData = rowData + key
        skillList.append(rowData)
        rowData = ''
    basket = ','.join(skillList)
    f.write(basket.encode('utf-8') + '\n')

c.close()
db.close()
f.close()

# --------------------------------------------------------------------------------------------------------------------
