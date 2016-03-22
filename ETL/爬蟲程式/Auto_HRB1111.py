# coding=utf-8

def hrb1111():

    import _mysql_exceptions
    import requests as rs
    from bs4 import BeautifulSoup as bs
    import time
    import datetime
    import MySQLdb
    import sys

    reload(sys)
    sys.setdefaultencoding("utf-8")  # 避免字型轉碼錯誤

    today = datetime.date.today()
    one_day = datetime.timedelta(days=1)
    yesterday = today - one_day

    filename = 'E:\TextFile/InsertCopy_1111_' + \
               ''.join(str(yesterday).split('-')) + '.txt'

    f = open(filename, 'w')

    src = '1111人力銀行'
    count = 0
    address = 'http://www.1111.com.tw/mobileWeb/job-index.asp?role=1%2C2%2C4%2C16&keys=&c0Cht=&c0=&d0Cht=' \
              '%E8%BB%9F%E9%AB%94%E5%B7%A5%E7%A8%8B%2C%E7%B3%BB%E7%B5%B1%E8%A6%8F%E5%8A%83%2C%E7%B6%B2%E8' \
              '%B7%AF%E7%AE%A1%E7%90%86&d0=140200%2C140300%2C140400&t0Cht=&t0=&gr=&ex=&wk=&si=1&page={}'
    # 1111 human resource bank - 軟體工程(SE) + 系統規劃(SA) + 網路管理(MIS)

    for page in range(1, 120):  # 換頁迴圈
        address_format = address.format(page)
        res = rs.get(address_format)
        # print res.encoding - 'utf-8'
        soup = bs(res.text, 'html.parser')
        jobList = soup.select('.jobList li')
        for li in jobList:  # 職缺列表迴圈
            jobTitle = ''.join(li.select('.list_content p')[0].text.encode('utf-8').split(','))
            # 職稱
            company = ''.join(li.select('.black')[0].text.encode('utf-8').split(','))
            # 公司名稱
            postDate = ''.join(li.select('.gray')[1].text.encode('utf-8')[15:].split(','))
            # 公告日期
            jobURL = 'http:' + li.select('a')[0]['href'].encode('utf-8')
            # 職缺網址

            if postDate == str(yesterday):

                try:
                    res2 = rs.get(jobURL)  # 要求進入工作內容細節
                    soup2 = bs(res2.text, 'html.parser')
                    jobContent = soup2.select('#jobcontent')  # 來自 jobURL (soup2)
                    dic = {'工作性質：': '', '工作內容：': '', '工作經驗：': '', '工作待遇：': '',
                           '工作地點：': '', '電腦專長：': '', '附加條件：': ''}  # 建立字典抓取資料
                    for data in jobContent[0].select('li'):  # 職缺細節迴圈
                        tle = data.select('.tle')
                        info = data.select('.info')
                        if len(tle) > 0:
                            if tle[0].text.encode('utf-8') in dic:
                                dic[tle[0].text.encode('utf-8')] = ''.join(info[0].text.strip().split(','))

                    empType = dic.get('工作性質：').encode('utf-8')
                    # 雇用性質
                    exp = dic.get('工作經驗：').encode('utf-8')
                    # 年資要求
                    salary = dic.get('工作待遇：').encode('utf-8')
                    # 薪水
                    content = dic.get('工作內容：') + dic.get('電腦專長：') + dic.get('附加條件：')
                    content = ''.join(content.strip().encode('utf-8').split('\n'))
                    # 工作內容
                    # skill = GetSkill.getsSkill(content)
                    # 內容中的職缺技能
                    location = dic.get('工作地點：').encode('utf-8')
                    # 地址

                    companyDescription = soup2.select('#companyDescription')  # 來自 jobURL (soup2)
                    companyURL = 'http://www.1111.com.tw/mobileWeb/' + companyDescription[0]['href']
                    res3 = rs.get(companyURL)  # 要求進入公司資料
                    soup3 = bs(res3.text, 'html.parser')
                    company_jobContent = soup3.select('#jobcontent')
                    company_dic = {'　行業別：': ''}
                    for data in company_jobContent[0].select('li'):  # 公司資料迴圈
                        tle = data.select('.tle')
                        info = data.select('.info')
                        if len(tle) > 0:
                            if tle[0].text.encode('utf-8') in company_dic:
                                company_dic[tle[0].text.encode('utf-8')] = ''.join(info[0].text.strip().split(','))

                    industry = company_dic.get('　行業別：').encode('utf-8')
                    # 產業別
                except rs.exceptions.ConnectionError as e:
                    print "Can not connect to this address!"
                    print "Error message is %s" % e
                    print jobTitle + '\t' + jobURL
                except IndexError as e:
                    print "List index out of range!"
                    print "Error message is %s" % e
                    print jobTitle + '\t' + jobURL
                except Exception as e:
                    print "Unknown exception!"
                    print "Error message is %s" % e
                    print jobTitle + '\t' + jobURL

                time.sleep(0.5)

                row_data = '{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}'\
                    .format(src, postDate, jobTitle, company, industry, location, empType, exp, salary, content, jobURL)

                row_data = ''.join(row_data.split('\t'))
                # 欄位 => 來源 張貼日期 職稱 公司名稱 產業別 地址 雇用類型 年資要求 薪水 工作內容 連結

                f.write(row_data.encode('utf-8') + '\n')

                db = MySQLdb.connect(host="localhost", user="yang", passwd="iiizb104", db="project")
                db.set_character_set('utf8')
                cursor = db.cursor()
                sql = (
                    'insert into '
                    'project.jobstored(srcno, postdate, title, company, industry, locno, emptypeno, exp, salary, content, url)'
                    ' VALUES '
                    '("' + src + '","' + postDate + '","' + jobTitle + '","' + company + '","' + industry + '","' + location + '","' + empType + '","' + exp + '","' + salary + '","' + content + '","' + jobURL + '")'
                )

                try:
                    cursor.execute(sql)
                    count += 1
                except _mysql_exceptions.IntegrityError as e:
                    print "Data duplicate entry!"
                    print "Error message is %s" % e
                    print jobTitle + '\t' + jobURL
                except _mysql_exceptions.OperationalError as e:
                    print "Incorrect string value!"
                    print "Error message is %s" % e
                    print jobTitle + '\t' + jobURL
                except _mysql_exceptions.DataError as e:
                    print "Data too long for column!"
                    print "Error message is %s" % e
                    print jobTitle + '\t' + jobURL
                except Exception as e:
                    print "Unknown exception!"
                    print "Error message is %s" % e
                    print jobTitle + '\t' + jobURL

                db.commit()

                cursor.close()
                db.close()

    # f.close()
    print str(yesterday) + ' 匯入MySQL的資料筆數共 ' + str(count) + ' 筆'

# hrb1111()



