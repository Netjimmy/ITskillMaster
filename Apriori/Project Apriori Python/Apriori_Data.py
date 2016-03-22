# coding=utf-8

def get_skill_list():

    import json
    import MySQLdb
    import sys

    reload(sys)
    sys.setdefaultencoding("utf-8")  # 避免字型轉碼錯誤

    db = MySQLdb.connect(host="localhost", user="root", passwd="iiizb104", db="project")
    db.set_character_set('utf8')

    c = db.cursor()
    c.execute("SET names utf8")
    sql_query = "SELECT skill FROM project.jobstorage WHERE skill NOT REGEXP '{}';"

    c.execute(sql_query)

    row = c.fetchall()  # 整個資料庫為一個list，而每筆個別資料被視為一個list中的元素。

    list = []

    for i in row:
        skill = json.loads(i[0])
        skillList = []
        rowData = ''
        for key in skill:
            rowData = rowData + key
            skillList.append(rowData)
            rowData = ''
        list.append(skillList)

    c.close()
    db.close()

    return list

# --------------------------------------------------------------------------------------------------------------------
