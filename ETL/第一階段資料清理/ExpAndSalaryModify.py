# coding=utf-8

def range_split(ss):   # 區間範圍切分
    import re

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
    import re

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
        '''
        if (amount[amount.find(u'十')-1:1] and amount[amount.find(u'十')-1:1] in ('1','2','3','4','5','6','7','8','9')):#前有數字
            #a = amount[amount.find(u'十')-1:1]+'0'
            #print 'a=' + a
            #print type(a)
            #print amount[amount.find('十')-1:4]
            amount = '0'.join(amount.split('十'))#前數字串接0
            #print amount[amount.find('十')-1:1
        elif (amount[amount.find(u'十')+1:1] and amount[amount.find(u'十')+1:1] in ('1','2','3','4','5','6','7','8','9')):#前無數字但後有數字
            amount = '1'.join(amount.split('十'))#十=>1
        else:#前後都不是數字
            amount = '10'.join(amount.split('十'))#十轉成10
        '''
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
    import re

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
    import string
    import re

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
    # try:
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

    import numpy as np
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
