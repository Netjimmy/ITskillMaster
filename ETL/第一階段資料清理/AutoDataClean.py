# coding=utf-8

import MySQLdb
import _mysql_exceptions
import datetime
import sys

import GetSkill as gs
import WordTransform as wt
import Ngram as n
import ExpAndSalaryModify as m
import LocTransform as lt

reload(sys)
sys.setdefaultencoding("utf-8")  # 避免字型轉碼錯誤

today = datetime.date.today()
one_day = datetime.timedelta(days=1)
yesterday = today - one_day

filename = 'C:/Users/BigData/PycharmProjects/project/DataClean/log/logfile' + \
           ''.join(str(yesterday).split('-')) + '.txt'

f = open(filename, 'w')

db = MySQLdb.connect(host="localhost", user="root", passwd="iiizb104", db="project")
db.set_character_set('utf8')

c = db.cursor()
c.execute("SET names utf8")
sql_query = "select * from jobstored where postdate = '" + str(yesterday) + "'"
c.execute(sql_query)

row = c.fetchall()  # 整個資料庫為一個list，而每筆個別資料被視為一個list中的元素。
# print row

for i in row:
    jobno = i[0]
    src = i[1]
    postdate = i[2]
    title = " ".join(i[3].split("'"))
    company = " ".join(i[4].split("'"))
    industry = " ".join(i[5].split("'"))
    loc = lt.loc_cluster(i[6][:9])
    emptype = i[7]
    exp = m.salary_year_modify(i[8][0:9])
    salary = m.salary_year_modify(i[9])
    content = " ".join(i[10].split("'"))
    content = "1. ".join(content.split("1."))
    content = "2. ".join(content.split("2."))
    content = "3. ".join(content.split("3."))
    content = "4. ".join(content.split("4."))
    content = "5. ".join(content.split("5."))
    content = "6. ".join(content.split("6."))
    content = "7. ".join(content.split("7."))
    content = "8. ".join(content.split("8."))
    content = "9. ".join(content.split("9."))
    content = "0. ".join(content.split("0."))
    skill = gs.get_skill(content)
    skill = n.ngram(skill)
    skill = wt.changeWord(skill)
    skill = wt.deleteWord(skill)
    skill = wt.dicToJson(skill)
    url = i[11]

    line = "%s, '%s', '%s', '%s', '%s', '%s', '%s', '%s', %s, %s, '%s', '%s', '%s'" % \
           (jobno, src, postdate, title, company, industry, loc, emptype, exp, salary, content, skill, url)
    # print line

    sql = "INSERT INTO project.jobstorage" \
          "(jobno, src, postdate, title, company, industry, loc, emptype, exp, salary, content, skill, url) " \
          "VALUES (" + line + ")"

    try:
        c.execute(sql)
    except _mysql_exceptions.IntegrityError as e:
        log = "Data duplicate entry!" + '\n' + "Error message is %s" % e + '\n' + str(jobno) + '\t' + url + '\n'
        f.write(log.encode('utf-8') + '\n')
        print log
    except _mysql_exceptions.OperationalError as e:
        log = "Incorrect value!" + '\n' + "Error message is %s" % e + '\n' + str(jobno) + '\t' + url + '\n'
        f.write(log.encode('utf-8') + '\n')
        print log
    except _mysql_exceptions.DataError as e:
        log = "Data too long for column!" + '\n' + "Error message is %s" % e + '\n' + str(jobno) + '\t' + url + '\n'
        f.write(log.encode('utf-8') + '\n')
        print log
    except Exception as e:
        log = "Unknown exception!" + '\n' + "Error message is %s" % e + '\n' + str(jobno) + '\t' + url + '\n'
        f.write(log.encode('utf-8') + '\n')
        print log

    db.commit()

c.close()
db.close()
f.close()
