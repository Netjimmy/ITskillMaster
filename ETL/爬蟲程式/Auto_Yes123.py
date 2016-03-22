# -*- coding: utf-8 -*-
# !/usr/bin/python

def yes123():

    import re
    import MySQLdb
    import _mysql_exceptions
    import requests
    from bs4 import BeautifulSoup as bs
    import sys
    from time import strftime

    def get_yesterday():
        import datetime
        get_today = datetime.date.today()
        yesterday = get_today - datetime.timedelta(days=1)
        return yesterday

    today_format = strftime('%Y-%m-%d').encode('utf-8')

    reload(sys)
    sys.setdefaultencoding("utf-8")  # 避免字型轉碼錯誤

    count = 0

    filename = 'C:/Users/BigData/PycharmProjects/project/WriteIntoMySQL/TextFile/InsertCopy_yes123_' + \
               ''.join(str(get_yesterday()).split('-')) + '.txt'
    job_list = open(filename, "w")


    for i in range(0, 500, 20):

        payload = {'find_key1': '關鍵字', 'search_feature': '', 'search_work': '軟體／工程全部+MIS／網管全部', 'search_multi_loc': '請選擇地區',
                   'find_key2': '', 'search_multi_loc2': '請選擇地區', 'search_work2': '請選擇職務', 'search_job2': '請選擇行業',
                   'find_key3': '', 'search_multi_loc3': '請選擇地區', 'search_work3': '請選擇職務', '_rdo_1': '1', 'search_subj': '',
                   'search_work4': '請選擇職務', 'search_multi_loc4': '請選擇地區', 'search_multi_loc5': '請選擇地區', '_rdo_2': '1',
                   'search_work6': '請選擇職務', 'search_work7': '請選擇職務', 'search_multi_loc6': '請選擇地區', 'search_work8': '請選擇職務',
                   'search_multi_loc7': '請選擇地區', 'find_sf_subj_mode1': '', 's_find_sf_subj_mode1': '',
                   'find_se_work_mode1': '', 's_find_se_work_mode1': '', 'find_zone_mode1': '', 'find_zone_mode2': '',
                   'find_zone_mode3': '', 'find_zone_mode4': '', 'find_zone_mode5': '', 'find_zone_mode6': '',
                   'find_zone_mode7': '', 'find_zone_mode8': '', 'find_zone_mode9': '', 'find_zone_mode10': '',
                   's_find_zone_mode1': '', 's_find_zone_mode2': '', 's_find_zone_mode3': '', 's_find_zone_mode4': '',
                   's_find_zone_mode5': '', 's_find_zone_mode6': '', 's_find_zone_mode7': '', 's_find_zone_mode8': '',
                   's_find_zone_mode9': '', 's_find_zone_mode10': '', 'find_metro_mode1': '', 'find_metro_mode2': '',
                   'find_metro_mode3': '', 'find_metro_mode4': '', 'find_metro_mode5': '', 'find_metro_mode6': '',
                   'find_metro_mode7': '', 'find_metro_mode8': '', 'find_metro_mode9': '', 'find_metro_mode10': '',
                   's_find_metro_mode1': '', 's_find_metro_mode2': '', 's_find_metro_mode3': '', 's_find_metro_mode4': '',
                   's_find_metro_mode5': '', 's_find_metro_mode6': '', 's_find_metro_mode7': '', 's_find_metro_mode8': '',
                   's_find_metro_mode9': '', 's_find_metro_mode10': '', 'find_map_mode1': '', 'find_map_mode2': '',
                   'find_map_mode3': '', 'find_map_mode4': '', 'find_indy_mode1': '', 'find_indy_mode2': '',
                   'find_indy_mode3': '', 'find_indy_mode4': '', 'find_indy_mode5': '', 'find_indy_mode6': '',
                   'find_indy_mode7': '', 'find_indy_mode8': '', 'find_indy_mode9': '', 'find_indy_mode10': '',
                   's_find_indy_mode1': '', 's_find_indy_mode2': '', 's_find_indy_mode3': '', 's_find_indy_mode4': '',
                   's_find_indy_mode5': '', 's_find_indy_mode6': '', 's_find_indy_mode7': '', 's_find_indy_mode8': '',
                   's_find_indy_mode9': '', 's_find_indy_mode10': '', 'find_work_mode1': '2_1011_0001_0000',
                   'find_work_mode2': '2_1011_0002_0000', 'find_work_mode3': '', 'find_work_mode4': '',
                   'find_work_mode5': '', 'find_work_mode6': '', 'find_work_mode7': '', 'find_work_mode8': '',
                   'find_work_mode9': '', 'find_work_mode10': '', 's_find_work_mode1': '軟體／工程全部',
                   's_find_work_mode2': 'MIS／網管全部', 's_find_work_mode3': '', 's_find_work_mode4': '',
                   's_find_work_mode5': '', 's_find_work_mode6': '', 's_find_work_mode7': '', 's_find_work_mode8': '',
                   's_find_work_mode9': '', 's_find_work_mode10': '', 'find_job_mode1': '', 'find_job_mode2': '',
                   'find_job_mode3': '', 'find_job_mode4': '', 'find_job_mode5': '', 'find_job_mode6': '',
                   'find_job_mode7': '', 'find_job_mode8': '', 'find_job_mode9': '', 'find_job_mode10': '',
                   's_find_job_mode1': '', 's_find_job_mode2': '', 's_find_job_mode3': '', 's_find_job_mode4': '',
                   's_find_job_mode5': '', 's_find_job_mode6': '', 's_find_job_mode7': '', 's_find_job_mode8': '',
                   's_find_job_mode9': '', 's_find_job_mode10': '', 'find_sche_mode1': '', 'find_sche_mode2': '',
                   'find_sche_mode3': '', 'find_sche_mode4': '', 'find_sche_mode5': '', 's_find_sche_mode1': '',
                   's_find_sche_mode2': '', 's_find_sche_mode3': '', 's_find_sche_mode4': '', 's_find_sche_mode5': '',
                   '_mu_sf_1': '', '_mu_se_1': '', '_mu_chkbox_2': '', '_mu_chkbox_3': '', '_mu_wk_1': '', '_mu_wk_2': '',
                   '_mu_wk_3': '', '_mu_wk_4': '', '_mu_wk_5': '', '_mu_job_1': '', '_mu_edu_1': '', '_mu_edu_2': '',
                   '_mu_edu_3': '', '_mu_edu_4': '', '_mu_edu_5': '', '_mu_edu_6': '', '_mu_edu_7': '', '_mu_year_1': '',
                   '_mu_year_2': '', '_mu_lang_1': '', '_mu_lang_2': '', '_mu_lang_3': '', '_mu_psn_1': '', '_mu_vc_1': '',
                   '_mu_vc_2': '', '_mu_vc_3': '', '_mu_vc_4': '', '_mu_sc_1': '', '_mu_sc_2': '', 'find_subj_mode1': '',
                   'find_subj_mode2': '', 'find_subj_mode3': '', 's_find_subj_mode1': '', 's_find_subj_mode2': '',
                   's_find_subj_mode3': '', 'find_sw_mode1': '', 'find_sw_mode2': '', 'find_sw_mode3': '',
                   'find_sw_mode4': '', 'find_sw_mode5': '', 's_find_sw_mode1': '', 's_find_sw_mode2': '',
                   's_find_sw_mode3': '', 's_find_sw_mode4': '', 's_find_sw_mode5': '', 'find_cert_mode1': '',
                   'find_cert_mode2': '', 'find_cert_mode3': '', 'find_cert_mode4': '', 'find_cert_mode5': '',
                   's_find_cert_mode1': '', 's_find_cert_mode2': '', 's_find_cert_mode3': '', 's_find_cert_mode4': '',
                   's_find_cert_mode5': '', 'order_by': 'm_date', 'order_ascend': 'desc', 'strrec': str(i),
                   'search_key_word': '關鍵字', 'search_type': 'job', 'us_menu': '', 'search_item': '1',
                   'search_from': 'joblist', 'job_show_type': 'B'}

        rs = requests.session()
        res = rs.post('http://www.yes123.com.tw/admin/job_refer_list.asp', data=payload)
        res.encoding = 'utf-8'

        soup = bs(res.text, "html.parser")
        yesterday = get_yesterday()

        for i in soup.select('.jbd'):
            front_page_date = ''.join(i.select('.date2')[0].text.strip().split()).encode('utf-8')
            postdate = '2016-' + '-'.join(front_page_date.strip().split("."))  # 將分割的地方插入'-'的符號
            yesterday = get_yesterday()
            if str(postdate) == str(yesterday):
                hr_bank = 'yes123求職網'
                front_page_date = ''.join(i.select('.date2')[0].text.strip().split()).encode('utf-8')
                title = ''.join(i.select('.t0')[0].text.strip().split()).encode('utf-8')
                com_name = ''.join(i.select('.t1')[0].text.strip().split()).encode('utf-8')
                ex = ''.join(i.select('.t2')[0].text.strip().split()).encode('utf-8')
                ex = ex.split('，')[0]
                area = ''.join(i.select('.area2')[0].text.strip().split()).encode('utf-8')
                kind = ''.join(i.select('.kind2')[0].text.strip().split()).encode('utf-8')
                url = i.select('.t0 a')[0]['href']

                if re.search('@', url):
                    web = 'http://www.yes123.com.tw/' + url.split('@')[1]
                else:
                    web = 'http://www.yes123.com.tw/' + url

                rs = requests.get(web)
                content = bs(rs.text, 'lxml')

                for des in content.select('.comp_detail'):
                    if str(''.join(des.select('h2')[0].text.strip().split()).encode('utf-8')) == '徵才說明':
                        for new_date in des.select('li'):
                            if new_date.select('.tt'):
                                if str(''.join(new_date.select('.tt')[0].text.strip().split()).encode('utf-8')) == '工作內容：':
                                    job_des = str(''.join(new_date.select('.rr')[0].text.strip().split()).encode('utf-8'))
                                elif str(''.join(new_date.select('.tt')[0].text.strip().split()).encode('utf-8')) == '工作地點：':
                                    job_address = str(''.join(new_date.select('.rr')[0].text.strip().split()).encode('utf-8'))
                                elif str(''.join(new_date.select('.tt')[0].text.strip().split()).encode('utf-8')) == '薪資待遇：':
                                    job_salary = str(''.join(new_date.select('.rr')[0].text.strip().split()).encode('utf-8'))

                for o in content.select('.comp_detail'):
                    if str(''.join(o.select('h2')[0].text.strip().split()).encode('utf-8')) == '其他條件':
                        for ot in o.select('li'):
                            other = ot.text

                for sk in content.select('.comp_detail'):
                    if str(''.join(sk.select('h2')[0].text.strip().split()).encode('utf-8')) == '技能與求職專長':
                        for ski in sk.select('li')[0]:
                            skill = str(''.join(ski.text.strip().split()).encode('utf-8'))

                domain = 'http://www.yes123.com.tw//admin/'

                for ty in content.select('.jobname_title'):
                    type_web = ty.select('a')[0]['href']
                    con_type_web = domain + type_web
                    rs = requests.get(con_type_web)
                    typecontent = bs(rs.text, 'lxml')

                    for jt in typecontent.select('.comp_detail'):
                        if str(''.join(typecontent.select('h2')[0].text.strip().split()).encode('utf-8')) == '企業資料':
                            for jt in typecontent.select('li'):
                                if jt.select('.tt'):
                                    if str(''.join(jt.select('.tt')[0].text.strip().split()).encode('utf-8')) == '行業類別：':
                                        jbty = str(''.join(jt.select('.rr')[0].text.strip().split()).encode('utf-8'))

                sentence = '{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'\
                    .format(hr_bank, postdate, title, com_name, jbty, job_address, kind, ex, job_salary, skill + job_des, web)
                # print sentence

                db = MySQLdb.connect(host="localhost", user="jao", passwd="iiizb104", db="project")
                db.set_character_set('utf8')
                cursor = db.cursor()
                sql = (
                    'insert into '
                    'project.jobstored(srcno, postdate, title, company, industry, locno, emptypeno, exp, salary, content, url)'
                    ' VALUES '
                    '("' + hr_bank + '","' + postdate + '","' + title + '","' + com_name + '","' + jbty + '","' + job_address + '","' + kind + '","' + ex + '","' + job_salary + '","' + skill + job_des + '","' + web + '")'
                )

                try:
                    cursor.execute(sql)
                    count += 1
                except _mysql_exceptions.IntegrityError as e:
                    print "Data duplicate entry!"
                    print "Error message is %s" % e
                    print title + '\t' + web
                except _mysql_exceptions.OperationalError as e:
                    print "Incorrect string value!"
                    print "Error message is %s" % e
                    print title + '\t' + web
                except _mysql_exceptions.DataError as e:
                    print "Data too long for column!"
                    print "Error message is %s" % e
                    print title + '\t' + web
                except Exception as e:
                    print "Unknown exception!"
                    print "Error message is %s" % e
                    print title + '\t' + web

                db.commit()

                cursor.close()
                db.close()

                job_list.write(sentence)

    job_list.close()
    print str(yesterday) + ' 匯入MySQL的資料筆數共 ' + str(count) + ' 筆'

yes123()
