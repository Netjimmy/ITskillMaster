# coding: utf-8

# In[9]:

import requests
import os
from bs4 import BeautifulSoup as bs
import re
import datetime

#取昨天日期
def getYesterday(): 
    import datetime
    today=datetime.date.today() 
    oneday=datetime.timedelta(days=1) 
    yesterday=today-oneday  
    return yesterday

#-----------------------------------------------------------------------------------

def getJobContent(x):

    #取昨天日期---------------
    yesterday = getYesterday()
    res = requests.get(x)
    res.encoding = "UTF-8"
    #print res.text
    soup = bs(res.text)
    # '更新日期字串:'
    jobdate=soup.select('p.jobupdate')[0].text
    #print jobdate
    djobdate = datetime.date(int(jobdate[7:11]),int(jobdate[12:14]),int(jobdate[15:17]))
    #print jobdate[7:17]
    if (djobdate != yesterday):
        return
    #yesterday轉成字串
    yesterday = yesterday.strftime('%Y-%m-%d')
    # '工作內容字串:'
    jobdesc = ''
    for p in (soup.select('dd.spc-col')):
        jobdesc = jobdesc+ p.select('p')[0].text.strip('\n')
    #加上擅長工具字串
    jobdesc = jobdesc  + soup.select('dl.clearfix dd')[16].text
    #print repr(jobdesc)
    #print '=============='
    jobdesc2 = ''.join(jobdesc.split('\n'))
    jobdesc2 = ''.join(jobdesc2.split('\r'))
    #薪水
    salarydesc = ' '.join(soup.select('dl.clearfix dd')[3].text.split(','))
    '''
    if re.search('[0-9]',soup.select('dl.clearfix dd')[3].text):
        try:
            salarydesc = str(salary_year_modify(soup.select('dl.clearfix dd')[3].text.encode('utf-8')))
            print type(salarydesc)
            print salarydesc
        except:
            salarydesc = str(' '.join(soup.select('dl.clearfix dd')[3].text.split(',')).encode('utf-8'))
            print 'bbb'
    else:
        salarydesc = ' '.join(soup.select('dl.clearfix dd')[3].text.split(','))
    '''
    # '地點字串:'
    addr = soup.select('.address-col')[0].text.strip('\n')
    addr2 = addr[2:addr.find(u'地圖')]
    #編號,來源,公告日期,職稱,公司名稱,產業別,地址,雇用類別,工作經驗要求,工作待遇,工作內容,工作連結
    #編號,來源,公告日期,
    srcno = u'518人力銀行'
    outstr = srcno+jobdate[7:17]+','
    # '職稱:'
    title = ' '.join(soup.select('.job-title')[0].text.strip('\n').split(','))
    outstr = outstr + ' '.join(soup.select('.job-title')[0].text.strip('\n').split(','))+','
    # '公司名稱:'
    company = ' '.join(soup.select('div.company-info a')[0].text.split(','))
    outstr = outstr +  ' '.join(soup.select('div.company-info a')[0].text.split(','))+','
    # '產業別:'
    industry = ' '.join(soup.select('div.company-info p a')[2].text.split(','))
    outstr = outstr +  ' '.join(soup.select('div.company-info p a')[2].text.split(','))+','
    # '地點:'
    locno = ' '.join(addr2.split(','))
    outstr = outstr +  ' '.join(addr2.split(','))+','
    # '工作性質/僱用類別:'
    emptypeno = ' '.join(soup.select('dl.clearfix dd')[4].text.split(','))
    outstr = outstr +  ' '.join(soup.select('dl.clearfix dd')[4].text.split(','))+','
    # '年資/工作經驗要求:'
    exp = ' '.join(soup.select('dl.clearfix dd')[12].text.split(','))
    outstr = outstr +  ' '.join(soup.select('dl.clearfix dd')[12].text.split(','))+','
    # '工作待遇/薪資:'
    salary = salarydesc
    outstr = outstr + salarydesc +','
    # '工作內容+擅長工具:'
    content = ' '.join(jobdesc2.split(','))
    outstr = outstr +  ' '.join(jobdesc2.split(','))+','
    #工作連結
    url = x
    outstr = outstr +  x
    #換行
    #outstr = outstr + '\n'
    #寫文字檔

    #寫入MySQL資料庫
    import MySQLdb

    # 打开数据库连接
    db = MySQLdb.connect("10.120.26.46","chang","iiizb104","project" )
    #print 'db conn ok'
    db.set_character_set('utf8')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 插入语句
    sql = "INSERT INTO project.jobstored(srcno, postdate, title,company,industry,locno,emptypeno,exp,salary,content,url) VALUES ('"+srcno+"','"+jobdate[7:17]+"','"+title+"','"+company+"','"+industry+"','"+locno+"','"+emptypeno+"','"+exp+"','"+salary+"','"+content+"','"+url+"')"
    #print sql
    try:
        #执行sql语句
        cursor.execute(sql)

        #提交到数据库执行
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()
        #寫失敗記錄檔

# 关闭数据库连接
    db.close()

    #print '=============================================='
#test case:
#getJobContent('http://www.518.com.tw/Internet%E7%A8%8B%E5%BC%8F%E8%A8%AD%E8%A8%88%E5%B8%AB-%E5%8F%B0%E4%B8%AD%E5%B8%82-%E5%8D%97%E5%8D%80-job-1109739.html')
#getJobContent('http://www.518.com.tw/(%E5%85%A7%E6%B9%96%E7%B8%BD%E5%85%AC%E5%8F%B8)%20%E7%B3%BB%E7%B5%B1%E8%A8%AD%E8%A8%88%20Java%20Architect-%E5%8F%B0%E5%8C%97%E5%B8%82-%E5%85%A7%E6%B9%96%E5%8D%80-job-1050177.html')
#getJobContent('http://www.518.com.tw/%E5%85%AC%E5%8F%B8%E7%B6%B2%E7%AB%99%E7%AE%A1%E7%90%86.%E7%B6%B1%E7%AB%99%E6%9E%B6%E8%A8%AD%E7%B6%AD%E8%AD%B7%E9%83%A8%E9%96%80%E8%AB%B8%E5%82%99%E4%B8%BB%E7%AE%A1,%E9%9A%94%E9%80%B1%E4%BC%91-%E5%8F%B0%E5%8C%97%E5%B8%82-%E5%A4%A7%E5%AE%89%E5%8D%80-job-803809.html')
#getJobContent('http://www.518.com.tw/Internet%E7%A8%8B%E5%BC%8F%E8%A8%AD%E8%A8%88%E5%B8%AB-%E6%96%B0%E5%8C%97%E5%B8%82-%E5%85%A8%E5%8D%80-job-1113832.html')
#getJobContent('http://www.518.com.tw/%E8%AA%A0%E5%BE%B5%E5%B0%88%E6%A5%AD%E7%B6%B2%E7%AB%99%E6%9E%B6%E8%A8%AD%E7%B6%AD%E8%AD%B7%E7%B4%84%E8%81%98%E4%BA%BA%E5%93%A1.%E6%97%A5%E8%96%AA1360%E8%B5%B7%20%20%E7%B0%BD%E7%B4%84%E5%8D%8A%E5%B9%B4%20%E5%8F%AF%E7%BA%8C%E7%B0%BD-%E5%8F%B0%E5%8C%97%E5%B8%82-%E5%A4%A7%E5%AE%89%E5%8D%80-job-1003894.html')
#----------------------------------------------------------------------------------------------------
def getPageContent(y):
    import requests
    from bs4 import BeautifulSoup as bs
    import time
    res = requests.get(y)
    res.encoding = "UTF-8"
    #print res.text

    soup = bs(res.text)
    #print soup.select('tr')[3].text
    #totalpage =  soup.select('span.pagecountnum')[0].text
    #print int(totalpage[4:7])
    for tr in (soup.select('li.title')):
        #print tr.select('a')[0].text , tr.select('a')[0]['href']
        #print tr.select('a')[0]['href']
        con = tr.select('a')[0]['href']
        con711 = con[7:11]
        #print tr.select('a')[0]['href']
        #print con
        #print (con711 != 'case')
        if (con711 != 'case'):
            getJobContent(tr.select('a')[0]['href'])
        time.sleep(10)
#test case:
#getPageContent('http://www.518.com.tw/job-index-P-12.html?i=1&am=1&ab=2032001,2032002,')
#getPageContent('http://www.518.com.tw/job-index-P-81.html?i=1&am=1&ab=2032001,2032002,')
#----------------------------------------------------------------------------------------------------
import string
import requests
import time
#取昨天日期
yesterday=getYesterday()
#print yesterday
#yesterday轉成字串
yesterday = yesterday.strftime('%Y-%m-%d')
#print type(yesterday)


from bs4 import BeautifulSoup as bs
res = requests.get('http://www.518.com.tw/job-index-P-1.html?i=1&am=1&ab=2032001,2032002,&al=3')
res.encoding = "UTF-8"
soup = bs(res.text)
totalpage =  soup.select('span.pagecountnum')[0].text
#print totalpage
#print totalpage[4:-1]
totalpagenum = int(totalpage[4:-1])+1
#print totalpagenum
page_format = 'http://www.518.com.tw/job-index-P-{}.html?i=1&am=1&ab=2032001,2032002,&al=3'
res = requests.get(page_format)
res.encoding = "UTF-8"
soup = bs(res.text)
#print res.text
#先建檔由底下程式寫
#fid = open('C:\\Users\BigData\\518\\ITData\\518_'+yesterday+'.csv','w')
#fid.write('')
#fid.close()
for p in range(1, totalpagenum):
    print p
    getPageContent(page_format.format(p))
    time.sleep(30)
    #print outpage
    #fid.write(outpage.encode('utf-8'))
print "End========"


# In[ ]:
