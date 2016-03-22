# coding: utf-8
# In[1]:
def hrb178():

    import requests as rs
    import time
    import MySQLdb
    import _mysql_exceptions
    from bs4 import BeautifulSoup as bs
    import sys

    reload(sys)
    sys.setdefaultencoding("utf-8")  # 避免字型轉碼錯誤

    def getYesterday():
        import datetime
        today = datetime.date.today()
        oneday = datetime.timedelta(days=1)
        yesterday = today - oneday
        return yesterday

    count = 0

    filename = 'C:/Users/BigData/PycharmProjects/project/WriteIntoMySQL/TextFile/InsertCopy_178_' + \
               ''.join(str(getYesterday()).split('-')) + '.txt'

    f = open(filename, 'w')

    address = 'http://www.job178.com.tw/jobs/find_jobs?ext=html&occ_id=10600000&dummy&p={}'
    for page in range(1, 11):
        address_format = address.format(page)
        res = rs.get(address_format)
        res.encoding = 'utf-8'
        soup = bs(res.text, "lxml")
        job_cont = soup.select('.joblist')
        domain = 'http://www.job178.com.tw'
        time.sleep(0.5)

        for tr in job_cont[0].select('tr'):

            # 剔除標頭欄位
            if len(tr.select('td')) > 0:
                # 抓日期
                date = tr.select('td')[0].text.strip()
                postdate = '2016-' + '-'.join(date.split("/"))  # 日期

                yesterday = getYesterday()

                if str(postdate) == str(yesterday):

                    # 公司網址
                    com_web = domain + tr.select('a')[1]['href']
                    com_webs = rs.get(com_web)
                    com_word = bs(com_webs.text, "lxml")

                    # 剔除178獵才公司
                    if com_web != 'http://www.job178.com.tw/company_3606':

                        # 抓產業別
                        com_domain = com_word.select('.body.company_detail')
                        com = com_domain[0].select('h3')[0].text.strip()  # 產業別

                        # 職缺網址
                        web = domain + tr.select('a')[0]['href']
                        webs = rs.get(web)
                        word = bs(webs.text, "lxml")
                        webweb = web  # 連結

                        # 抓職缺、公司
                        domain2 = word.select('.j_title')
                        job = domain2[0].select('h1')[0].text.strip()  # 職稱
                        company = domain2[0].select('a')[0].text.strip()  # 公司

                        # 抓工作內容
                        domain4 = word.select('.Cr2')
                        tool = ''.join(domain4[0].select('.body.work_content')[0].text.strip().split())

                        # 抓178人力銀行
                        domain5 = word.select('.path')
                        title = domain5[0].select('a')[0].text.strip()  # 178人力銀行

                        # 抓所在地、年資
                        domain3 = word.select('.condition_panel')
                        place = domain3[0].select('p')[4].text.strip()  # 地址
                        years = domain3[0].select('p')[3].text.strip()  # 年資要求
                        salary = domain3[0].select('p')[2].text.strip()  # 薪水

                        # 建字典抓擅長工具、工作技能
                        dic = {'擅長工具': '', '工作技能': ''}
                        for i in domain3[0].select('li'):
                            if i.select('b')[0].text.strip() in dic:
                                dic[i.select('b')[0].text.strip()] = ''.join(i.select('p')[0].text.strip().split())

                        # 合併資料得到工具
                        tools = tool + dic['擅長工具']+dic['工作技能']
                        emptype = ''

                        row_data = '{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}'\
                            .format(title, postdate, job, company, com, place, emptype, years, salary, tools, webweb)
                        row_data = ''.join(row_data.split('\t'))
                        # 欄位 => 來源 張貼日期 職稱 公司名稱 產業別 地址 雇用類型 年資要求 薪水 工作內容 連結
                        # print row_data
                        f.write(row_data.encode('utf-8') + '\n')

                        db = MySQLdb.connect(host="localhost", user="jao", passwd="iiizb104", db="project")
                        db.set_character_set('utf8')
                        cursor = db.cursor()

                        sql = (
                            "insert into "
                            "project.jobstored(srcno, postdate, title, company, industry, locno, emptypeno, exp, salary, content, url)"
                            " VALUES "
                            "('" + title + "','" + postdate + "','" + job + "','" + company + "','" + com + "','" + place + "','" + emptype + "','" + years + "','" + salary + "','" + tools + "','" + webweb + "')"
                        )

                        try:
                            cursor.execute(sql)
                            count += 1
                        except _mysql_exceptions.IntegrityError as e:
                            print "Data duplicate entry!"
                            print "Error message is %s" % e
                            print job + '\t' + webweb
                        except _mysql_exceptions.OperationalError as e:
                            print "Incorrect string value!"
                            print "Error message is %s" % e
                            print job + '\t' + webweb
                        except _mysql_exceptions.DataError as e:
                            print "Data too long for column!"
                            print "Error message is %s" % e
                            print job + '\t' + webweb
                        except Exception as e:
                            print "Unknown exception!"
                            print "Error message is %s" % e
                            print job + '\t' + webweb

                        db.commit()

                        cursor.close()
                        db.close()

    f.close()
    print str(yesterday) + ' 匯入MySQL的資料筆數共 ' + str(count) + ' 筆'
	
hrb178()

