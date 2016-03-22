# coding=utf-8

def job_select():

    import MySQLdb
    import _mysql_exceptions
    import datetime
    import sys

    import IsJobClose
    import Rebuild

    reload(sys)
    sys.setdefaultencoding("utf-8")  # 避免字型轉碼錯誤

    today = datetime.date.today()
    one_day = datetime.timedelta(days=1)
    yesterday = today - one_day

    filename = 'log/JobSelectLog' + ''.join(str(yesterday).split('-')) + '.txt'
    f = open(filename, 'w')

    Rebuild.rebuild_table()  # 重製job裡面的資料

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

        if IsJobClose.isJobClose(url) == False:

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

# ---------------------------------------------------------------------------------------------------------------------

job_select()
