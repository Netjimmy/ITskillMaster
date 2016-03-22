


#抓104職缺連結
import requests as rs
import time
from bs4 import BeautifulSoup as bs
address = 'http://www.104.com.tw/jobbank/joblist/joblist.cfm?jobsource=n104bank1&ro=0&jobcat=2007000000&isnew=0&order=2&asc=0&page={}&psl=L_A'
for page in range(1,125):
    address_format = address.format(page)
    res = rs.get(address_format)
    #print res.encoding
    soup = bs(res.text)
    job_cont = soup.select('.j_cont.line_bottom')
    domain = 'http://www.104.com.tw/'
    for li in job_cont:
        print domain + li.select('a')[0]['href']
















import requests as rs
import time
import string
from bs4 import BeautifulSoup as bs
#joblist3 = open('joblist3.txt', 'w')

f= open("20160219worklist.txt","w")

for line in open('20160219.txt'):
#因為104有獵人頭、接案等不同的網頁格式，所以要用try、except來踢除
    try:
        w = rs.get(line)
        wedsite = bs(w.text)
        main = wedsite.select('.main')[0]
        cont = main.select('.content')[0]
        cont2 = main.select('.content')[1]
        #日期
        jobdate = main.select('.update')[0].text.encode('utf-8').split()[0]
        jobdate = jobdate[15:]
        #職稱
        job_title = main.select('h1')[0].text.strip().encode('utf-8').split()[0]
        job_title = main.select('.header.static')[0]
        title = job_title.select('.center')
        jobtitle1 = job_title.select('h1')[0].text.strip().encode('utf-8').split(' ')[0]
        jobtitle2 = job_title.select('h1')[0].text.strip().encode('utf-8').split(' ')[1]
        jobtitle3 = job_title.select('h1')[0].text.strip().encode('utf-8').split(' ')[2]
        jobtitle4 = job_title.select('h1')[0].text.strip().encode('utf-8').split(' ')[3]
        jobtitle5 = job_title.select('h1')[0].text.strip().encode('utf-8').split(' ')[4]
        jobtitle6 = job_title.select('h1')[0].text.strip().encode('utf-8').split(' ')[5]
        jobtitle = jobtitle1 + jobtitle2 + jobtitle3 + jobtitle4 + jobtitle5 + jobtitle6
        #公司名
        companyname = main.select('.cn')[0].text.encode('utf-8')
        #公司屬性
        companyaddr = main.select('.company a')[0]['href']
        res = rs.get(companyaddr)
        res.encoding ='utf-8'#因為抓出為亂碼，需轉換
        soup = bs(res.text)
        company_addr = soup.select('#cont_main')[0]
        companytype = company_addr.select('.intro')[0]
        companytype = companytype.select('dd')[0].text.encode('utf-8')   
        #工作性質
        jobtype = cont.select('dd')[2].text.encode('utf-8')
        #工作待遇
        salary = cont.select('dd')[1].text.encode('utf-8')
        #工作地址
        addr = cont.select('dd')[3].text.strip().encode('utf-8').split()[0]
        #工作經歷
        jobexp = cont2.select('dd')[1].text.encode('utf-8')
        #工作內容
        #jobcont = cont.select('p')[0].text.encode('utf-8')
        #jobcontent = "".join(jobcont.split('\<br\>'))
        #擅長工具
        tool = cont2.select('dd')[5].text.strip().encode('utf-8')
        #工作技能
        skill = cont2.select('dd')[6].text.strip().encode('utf-8')
        #其他條件
        other = cont2.select('dd')[7].text.strip().encode('utf-8')
        content = tool + skill + other
        #因為雙引號包覆功能較強,避免存入格式時跑掉
        total = '"' + '104人力銀行' + '",' + '"'+ jobdate + '",' + '"'+ jobtitle+ '",' +'"'+companyname + '",' + '"'+companytype+ '",' + '"'+addr + '",'+ '"'+jobtype + '",' + '"'+jobexp + '",' + '"'+salary + '",' +'"'+ content + '",' + '"'+line
        f.write(total)
        #print total

    except Exception as detail:
        print line,detail
        
        
f.close()