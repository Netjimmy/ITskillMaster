# coding=utf-8

import MySQLdb
import _mysql_exceptions
import datetime
import requests
from bs4 import BeautifulSoup as bs
import re
import time
import sys

# 重建網頁所連結之資料表job

def rebuild_table():

    db = MySQLdb.connect(host="localhost", user="root", passwd="iiizb104", db="project")
    db.set_character_set('utf8')

    c = db.cursor()
    c.execute("SET names utf8")

    sql_drop = "DROP TABLE IF EXISTS job;"
    sql_create = "CREATE TABLE IF NOT EXISTS job (" \
                 "jobno int not null auto_increment primary key, " \
                 "src varchar(50), " \
                 "postdate date, " \
                 "title varchar(150), " \
                 "company varchar(150), " \
                 "industry varchar(100), " \
                 "loc varchar(50), " \
                 "emptype varchar(50), " \
                 "exp decimal(3,1), " \
                 "salary decimal(10,2), " \
                 "content text(65535), " \
                 "skill json, " \
                 "skill26 json, " \
                 "url varchar(200) not null unique, " \
                 "cluster int);"

    c.execute(sql_drop)
    c.execute(sql_create)
    db.commit()

    c.close()
    db.close()

# ---------------------------------------------------------------------------------------------------------------------
'''
def is518jobclose(x):
    try:
        res = requests.get(x)
        res.encoding = "UTF-8"
        soup = bs(res.text, "html.parser")
        return len(soup.select('p.job_be_close')) > 0
        time.sleep(15)
    except Exception as e:
        print "Unknown exception!" + '\n' + "Error message is %s" % e

def is104jobclose(x):
    try:
        res = requests.get(x)
        res.encoding = "UTF-8"
        soup = bs(res.text, "html.parser")
        return len(soup.select('div.wrap.closed')) > 0
    except Exception as e:
        print "Unknown exception!" + '\n' + "Error message is %s" % e

def is1111jobclose(x):
    try:
        res = requests.get(x)
        res.encoding = "UTF-8"
        soup = bs(res.text, "html.parser")
        return len(soup.select('.WRAPPER')) > 0
    except Exception as e:
        print "Unknown exception!" + '\n' + "Error message is %s" % e

def is178jobclose(x):
    try:
        res = requests.get(x)
        res.encoding = "UTF-8"
        soup = bs(res.text, "html.parser")
        return u'職缺已關閉' in soup.select('ul.path li')[0].text
    except Exception as e:
        print "Unknown exception!" + '\n' + "Error message is %s" % e

def isMitJobsjobclose(x):
    res = requests.get(x)
    res.encoding = "UTF-8"
    soup = bs(res.text, "html.parser")
    return "The page you were looking for doesn't exist" in soup.select('title')[0].text

def isYes123jobclose(x):
    try:
        res = requests.get(x)
        res.encoding = "UTF-8"
        soup = bs(res.text, "html.parser")
        r = soup.select('#container tr td')[0].text
        if re.search(u"該企業已關閉此職缺，請您重新查詢", r):
            return 'True'
        else:
            return 'False'
    except Exception as e:
        print "Unknown exception!" + '\n' + "Error message is %s" % e

# 判斷該連結是否失效

def isJobClose(x):

    if re.search('www.yes123.com.tw', x):
        return isYes123jobclose(x)
    if re.search('www.518.com.tw', x):
        return is518jobclose(x)
    if re.search('mit.jobs', x):
        return isMitJobsjobclose(x)
    if re.search('www.job178.com.tw', x):
        return is178jobclose(x)
    if re.search('www.1111.com.tw', x):
        return is1111jobclose(x)
    if re.search('www.104.com.tw', x):
        return is104jobclose(x)

    return 'ERROR'
'''
# ---------------------------------------------------------------------------------------------------------------------

# main job_select()

def job_select():

    reload(sys)
    sys.setdefaultencoding("utf-8")  # 避免字型轉碼錯誤

    today = datetime.date.today()
    one_day = datetime.timedelta(days=1)
    yesterday = today - one_day

    filename = 'log/JobSelectLog' + ''.join(str(yesterday).split('-')) + '.txt'
    f = open(filename, 'w')

    rebuild_table()  # 重製job裡面的資料

    db = MySQLdb.connect(host="localhost", user="root", passwd="iiizb104", db="project")
    db.set_character_set('utf8')

    c = db.cursor()

    sql = "SELECT jobno, src, MAX(postdate), title, company, industry, loc, emptype, exp, salary, content, skill, " \
          "skill26, url, cluster FROM jobstorage GROUP BY url;"

    c.execute("SET names utf8")
    c.execute(sql)

    row = c.fetchall()  # 整個資料庫為一個list，而每筆個別資料被視為一個list中的元素。

    for i in row:
        jobno = i[0]
        src = i[1]
        postdate = i[2]
        title = i[3]
        company = i[4]
        industry = i[5]
        loc = i[6]
        emptype = i[7]
        exp = i[8]
        salary = i[9]
        content = i[10]
        skill = i[11]
        skill26 = i[12]
        url = i[13]
        cluster = i[14]

        if 0 <= cluster <= 14:
            line = "%s, '%s', '%s', '%s', '%s', '%s', '%s', '%s', %s, %s, '%s', '%s', '%s', '%s', %s" % \
                   (jobno, src, postdate, title, company, industry, loc, emptype, exp, salary, content, skill,
                    skill26, url, cluster)

            sql = "INSERT INTO project.job" \
                  "(jobno, src, postdate, title, company, industry, loc, emptype, exp, salary, content, skill, " \
                  "skill26, url, cluster) " \
                  "VALUES (" + line + ")"
        else:
            line = "%s, '%s', '%s', '%s', '%s', '%s', '%s', '%s', %s, %s, '%s', '%s', '%s', '%s'" % \
                   (jobno, src, postdate, title, company, industry, loc, emptype, exp, salary, content, skill,
                    skill26, url)

            sql = "INSERT INTO project.job" \
                  "(jobno, src, postdate, title, company, industry, loc, emptype, exp, salary, content, skill, " \
                  "skill26, url) " \
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
            log = "Data too long!" + '\n' + "Error message is %s" % e + '\n' + str(jobno) + '\t' + url + '\n'
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

# ---------------------------------------------------------------------------------------------------------------------

job_select()  # 執行每日更新網站資料庫動作
