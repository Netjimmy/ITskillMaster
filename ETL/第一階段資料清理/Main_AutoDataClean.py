# coding=utf-8

from nltk.util import ngrams
import numpy as np
import numpy.linalg as LA
import re
import string
import json
import MySQLdb
import _mysql_exceptions
import datetime
import sys

# 區分工作地點的行政區

def loc_cluster(loc):

    loc = '台'.join(loc.split('臺'))
    loc_list = ['台北市', '新北市', '桃園市', '台中市', '台南市', '高雄市', '基隆市', '新竹市', '嘉義市', '新竹縣', '苗栗縣',
                '彰化縣', '南投縣', '雲林縣', '嘉義縣', '屏東縣', '宜蘭縣', '花蓮縣', '台東縣', '澎湖縣', '金門縣', '連江縣']

    if loc not in loc_list:
        loc = '其他地區'

    return loc

# ---------------------------------------------------------------------------------------------------------------------

# 薪資與年資的資料轉值

def range_split(ss):   # 區間範圍切分

    if re.match('\d{0,}\D{0,}\d{1,}\D{0,}-\d{0,}\D{0,}\d{1,}\D{0,}', ss):
        ss1 = ss.split('-')[0]
        ss2 = ss.split('-')[1]
    elif re.match('\d{0,}\D{0,}\d{1,}\D{0,}~\d{0,}\D{0,}\d{1,}\D{0,}', ss):
        ss1 = ss.split('~')[0]
        ss2 = ss.split('~')[1]
    elif re.match('\d{0,}\D{0,}\d{1,}\D{0,}至\d{0,}\D{0,}\d{1,}\D{0,}', ss):
        ss1 = ss.split('至')[0]
        ss2 = ss.split('至')[1]
    elif re.match('\d{0,}\D{0,}\d{1,}\D{0,}', ss):
        ss1 = ss
        ss2 = ss
    else:
        ss1 = 0
        ss2 = 0

    slist = [ss1, ss2]

    return slist

def number_transfer(amount):  # 中文數字轉阿拉伯數字

    amount = '千'.join(amount.split('仟'))
    amount = '1'.join(amount.split('一'))
    amount = '2'.join(amount.split('二'))
    amount = '3'.join(amount.split('三'))
    amount = '4'.join(amount.split('四'))
    amount = '5'.join(amount.split('五'))
    amount = '6'.join(amount.split('六'))
    amount = '7'.join(amount.split('七'))
    amount = '8'.join(amount.split('八'))
    amount = '9'.join(amount.split('九'))
    if re.search('十', amount):
        if re.match('\D{0,}\d{1,}十\d{1,}\D{0,}', amount):  # 前數字後數字
            amount = ''.join(amount.split('十'))  # 十拿掉 ex:3十2=>32
        elif re.match('\D{0,}十\d{1,}\D{0,}', amount):  # 前非數字後數字
            amount = '1'.join(amount.split('十'))  # 十變成1 ex:十二=>12
        elif re.match('\D{0,}\d{1,}十\D{0,}', amount):  # 前數字後非數字
            amount = '0'.join(amount.split('十'))  # 十變成0 ex:3十=>30
        else:  # 前後非數字
            amount = '10'.join(amount.split('十'))  # 十變成10 ex: 十萬=>10萬

    return amount

def full2half(s):  # 符號全形轉半形

    s = ','.join(s.split('，'))
    s = '-'.join(s.split('－'))
    s = '~'.join(s.split('～'))
    s = '1'.join(s.split('１'))
    s = '2'.join(s.split('２'))
    s = '3'.join(s.split('３'))
    s = '4'.join(s.split('４'))
    s = '5'.join(s.split('５'))
    s = '6'.join(s.split('６'))
    s = '7'.join(s.split('７'))
    s = '8'.join(s.split('８'))
    s = '9'.join(s.split('９'))
    s = '0'.join(s.split('０'))
    s = 'k'.join(s.split('ｋ'))
    s = 'K'.join(s.split('Ｋ'))

    return s

def salary_sub_modify(amount):

    if re.match('[0-9]+[K|k]$', amount):  # 結尾有k,例如22K
        return amount[0:-1] + '000'  # 去掉K改乘上1000
    elif re.search('[萬|千]', amount):
        if amount.split('萬')[1]:
            amount2 = int(amount.split('萬')[0]) * 10000 + int(((amount.split('萬')[1]).split('千'))[0]) * 1000
        else:
            amount2 = int(amount.split('萬')[0]) * 10000
        return amount2
    else:
        return amount

def salary_year_modify(amount):

    amount2 = string.join(amount.split(' '), '')  # 移除空白
    amount2 = string.join(amount2.split(','), '')  # 移除薪水數字中的','
    amount2 = string.join(amount2.split('至'), '-')  # 至 改成 -
    amount2 = string.join(amount2.split('到'), '-')  # 到 改成 -

    if amount == '面議' or amount == '依公司規定' or amount == '論件計酬':
        return 0
    if re.search('時薪', amount):  # 時薪 return 0
        return 0
    if re.search('日薪', amount):  # 時薪 return 0
        return 0

    dic = {'月薪': 1, '年薪': 12, 'NTD': 1, 'USD': 0.03, '年': 1, 'year': 1, 'Year': 1, 'YEAR': 1, '元': 1,
           '日薪': 1/30, '時薪': 1, 'permonth': 1, 'peryear': 12}  # 年薪與幣別:要除的數字(月數或匯率)
    for f in dic.keys():
        if re.search(f, amount):  # 若原始傳入資料有dic中的key的字樣時
            amount2 = string.join(amount2.split(f), '')  # 把dic中的key的字樣刪除,免得後面計算時發生錯誤
    amount2 = number_transfer(amount2)  # 中文數字轉阿拉伯數字
    alist = range_split(amount2)  # 範圍資料切分成list
    # outcome = 處理資料list,若原始資料是區間則list中的兩筆分別代表最小值與最大值,若原始資料非區間則兩筆相同
    try:
        outcome = [salary_sub_modify(i) for i in alist]
    except:
        return 0  # 若有錯誤則丟出0

    outcome2 = []
    for oo in outcome:
        if type(oo) == str:
            oo = filter(str.isdigit, oo)  # 只取數字的部分
        outcome2.append(int(oo))
    # outcome2 = [int(o) for o in outcome2 if (o >= '0' and o <= '9')]#只取數字的部份並轉成數字
    outcome2 = np.mean(outcome2)  # 取平均
    for f in dic.keys():  # 原始傳入資料中若有dic中的key
        if re.search(f, amount):
            outcome2 = float(outcome2 / dic.get(f))  # 把數字除以dic中的value,也就是要除的數字
    return outcome2

# ---------------------------------------------------------------------------------------------------------------------

# 取出內容中的相關技能關鍵字

def strQ2B(ustring):  # 需傳入unicode
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 0x3000:
            inside_code = 0x0020
        else:
            inside_code -= 0xfee0
        if inside_code < 0x0020 or inside_code > 0x7e:
            rstring += uchar
        rstring += unichr(inside_code)
    return rstring

def get_skill(jobdesc):  # 傳入工作技能相關文字txt檔名
    lineskill = []  # 一行的技能,代表一筆職缺中的技能
    jobdesc = jobdesc  # .decode('utf-8')#change to unicode
    skill = ''  # 單一技能
    for w in jobdesc:
        if re.match(u'[Ａ-Ｚａ-ｚ０-９／＃]', w):
            w = strQ2B(w)
            w = w.encode('utf-8')  # change back to utf-8

        if re.match('[a-zA-Z0-9+.#]', w):  # 讀到的字母如果符合英文或數字或/或#視為技能
            w = w.lower()  # 都轉小寫
            skill = skill + w  # 把字母加到單一技能

        else:
            if re.match('^[a-zA-Z.][a-zA-Z0-9+.#]{0,}', skill):  # 如果技能符合第一碼英文字或.開頭才視為技能

                if len(skill) > 1 or skill == 'c' or skill == 'r':
                    if ('.' not in skill) or ('.net' in skill) or ('.Net' in skill) or ('.NET' in skill):
                        # 排除.開頭但非.net之技能
                        skill.strip()  # 去掉單一skill中的空白
                        lineskill.append(skill)  # 將單一skill加到該筆職缺技能,並加個空白與後面隔開
                        # print lineskill
            skill = ''  # 清空此單一技能使後面重新寫入

    return lineskill

# ---------------------------------------------------------------------------------------------------------------------

# Ngram

def ngram(x):  # 傳入List
    outary = []
    for n in range(1, 5):
        grams = ngrams(x, n)
        for gram in grams:
            soutstr = ''
            for i in range(0, n):
                if len(soutstr) == 0:
                    soutstr = gram[i]
                else:
                    soutstr = soutstr + ' ' + gram[i]
            outary.append(soutstr)
    return outary  # 回傳list

# ---------------------------------------------------------------------------------------------------------------------

# 技能資料清理

'''
dic_transform = pickle.load(file('dic/dic_transform_v2.data'))
set_skill = pickle.load(file('dic/set_skill_final.data'))
set_skill26 = pickle.load(file('dic/set_skill_v8_500.data'))
list_skill26 = sorted(list(set_skill26))
'''

# 同義字與錯別字的轉換

def changeWord(dic_transform, x):  # 傳入list
    for word in x:
        if word in dic_transform:
            loc = x.index(word)
            x[loc] = dic_transform[word]
    return x  # 回傳list

# 依照字典刪除其他不需要的字詞

def deleteWord(List_skill, x):  # 傳入list
    x = [word for word in x if word in List_skill]
    return x

# 將資料由list轉換成JSON格式

def dicToJson(x):
    tmpDic = {}
    for each in x:
        if each not in tmpDic:
            tmpDic[each] = 1
        else:
            tmpDic[each] += 1

    return tmpDic

# 藉由分析將資料分發到與其較為相似的群體中

def getRecommendCluster(List_skill26, clusterVec, a):  # 傳入JSON
    tmpList = []
    for each in List_skill26:
        if each in a:
            tmpList.append(a[each])
        else:
            tmpList.append(0)

    # 若是空值陣列返回None
    if tmpList == np.zeros(len(List_skill26)).tolist():
        return None
    else:
        tmpCom = []
        for row in clusterVec:
            vec = json.loads(row[0])
            tmpCom.append(getDocDistance(vec, tmpList))

        # print ('max value:', max(tmpCom))
        return [i for i, j in enumerate(tmpCom) if j == max(tmpCom)][0]  # 傳出cluster數字

def getDocDistance(a, b):
    if LA.norm(a) == 0 or LA.norm(b) == 0:
        return -1
    return round(np.inner(a, b) / (LA.norm(a) * LA.norm(b)), 4)

# ---------------------------------------------------------------------------------------------------------------------

# main auto_data_clean()

def auto_data_clean():

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

    sql = "SELECT dict FROM project.dict where no = 3;"
    c.execute(sql)
    results = c.fetchone()
    dic_transform = json.loads(results[0])

    sql = "SELECT dict FROM project.dict where no = 2;"
    c.execute(sql)
    results = c.fetchone()
    List_skill = json.loads(results[0])    # 舊技能字典

    sql = "SELECT dict FROM project.dict where no = 1;"
    c.execute(sql)
    results = c.fetchone()
    List_skill26 = json.loads(results[0])  # 新技能字典

    sql = "SELECT clusterVector FROM project.cluster;"
    c.execute(sql)
    clusterVec = c.fetchall()

    sql_query = "select * from jobstored where postdate = '" + str(yesterday) + "';"
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
        loc = loc_cluster(i[6][:9])
        emptype = i[7]
        exp = salary_year_modify(i[8][0:9])
        salary = salary_year_modify(i[9])
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

        skill = get_skill(content)
        skill = ngram(skill)
        skill = changeWord(dic_transform, skill)
        # 新技能列
        skill26 = deleteWord(List_skill26, skill)
        skill26 = dicToJson(skill26)
        skill26JSON = json.dumps(skill26, ensure_ascii=False)
        # 舊技能列
        skill = deleteWord(List_skill, skill)
        skill = dicToJson(skill)
        skillJSON = json.dumps(skill, ensure_ascii=False)

        cluster = getRecommendCluster(List_skill26, clusterVec, skill)
        url = i[11]

        if 0 <= cluster <= 14:
            line = "%s, '%s', '%s', '%s', '%s', '%s', '%s', '%s', %s, %s, '%s', '%s', '%s', '%s', %s" % \
                   (jobno, src, postdate, title, company, industry, loc, emptype, exp, salary, content, skillJSON,
                    skill26JSON, url, cluster)

            sql = "INSERT INTO project.jobstorage" \
                  "(jobno, src, postdate, title, company, industry, loc, emptype, exp, salary, content, skill, " \
                  "skill26, url, cluster) " \
                  "VALUES (" + line + ")"
        else:
            line = "%s, '%s', '%s', '%s', '%s', '%s', '%s', '%s', %s, %s, '%s', '%s', '%s', '%s'" % \
                   (jobno, src, postdate, title, company, industry, loc, emptype, exp, salary, content, skillJSON,
                    skill26JSON, url)

            sql = "INSERT INTO project.jobstorage" \
                  "(jobno, src, postdate, title, company, industry, loc, emptype, exp, salary, content, skill, " \
                  "skill26, url) " \
                  "VALUES (" + line + ")"

        # print line

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

auto_data_clean()  # 執行每日資料清理動作
