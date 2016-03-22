# coding=utf-8

def push_skill_into_table():

    import json
    import MySQLdb
    import _mysql_exceptions
    import datetime
    import sys

    reload(sys)
    sys.setdefaultencoding("utf-8")  # 避免字型轉碼錯誤

    today = datetime.date.today()
    one_day = datetime.timedelta(days=1)
    yesterday = today - one_day

    db = MySQLdb.connect(host="localhost", user="root", passwd="iiizb104", db="project")
    db.set_character_set('utf8')

    c = db.cursor()
    c.execute("SET names utf8")
    sql_query = "SELECT jobno, skill FROM project.jobstorage WHERE skill NOT REGEXP '{}' AND postdate = '" \
                + str(yesterday) + "';"

    c.execute(sql_query)

    row = c.fetchall()  # 整個資料庫為一個list，而每筆個別資料被視為一個list中的元素。

    for i in row:
        jobno = i[0]
        skill = json.loads(i[1])
        for key in skill.keys():
            data = str(jobno) + ', "' + key + '"'

            sql_insert = "INSERT INTO project.skill (jobno, skill) VALUES (" + data + ")"

            try:
                c.execute(sql_insert)
            except _mysql_exceptions.IntegrityError as e:
                print "Data duplicate entry!"
                print "Error message is %s" % e
                print jobno + '\t' + key
            except _mysql_exceptions.OperationalError as e:
                print "Incorrect string value!"
                print "Error message is %s" % e
                print jobno + '\t' + key
            except _mysql_exceptions.DataError as e:
                print "Data too long for column!"
                print "Error message is %s" % e
                print jobno + '\t' + key
            except Exception as e:
                print "Unknown exception!"
                print "Error message is %s" % e
                print jobno + '\t' + key

            db.commit()

    c.close()
    db.close()

# ---------------------------------------------------------------------------------------------------------------------

push_skill_into_table()
