# version 4
# coding=utf-8

def strQ2B(ustring):  # 需傳入unicode
    # print ustring
    # print repr(ustring)
    # ustring = ustring.decode('utf-8')#把utf-8轉unicode
    # print repr(ustring)
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
# test
# a = strQ2B(u"ａｂｃ１２３４５")
# print a

# ==============================================================

def get_skill(jobdesc):  # 傳入工作技能相關文字txt檔名
    import re
    import string
    import requests
    lineskill = []  # 一行的技能,代表一筆職缺中的技能
    jobdesc = jobdesc  # .decode('utf-8')#change to unicode
    skill = ''  # 單一技能
    for w in jobdesc:
        if re.match(u'[Ａ-Ｚａ-ｚ０-９／＃]', w):
            w = strQ2B(w)
            w = w.encode('utf-8')  # change back to utf-8

        if re.match('[a-zA-Z0-9+.#]', w):  # 讀到的字母如果符合英文或數字或/或#視為技能
            w = w.lower()  # 都轉小寫
            # print w
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

'''
# test case:
print get_skill('【工作內容】1.網站系統前台、後台程式開發。2.所開發網站之維運，系統問題排除。3.具有1年網站程式開發經驗，對網站開發流程有'
                '了解。【擅用工具】HTML + CSS + javascript     製作為基礎運用：1.對任一種有開發經驗：PHP(加分)/Ruby/Python/Perl'
                '/RoR/ASP.NET。2.熟悉JavaScript(加分)、jQuery的使用。3.熟悉MySQL資料庫。4.熟悉Html。5.熟悉CSS(加分)。【人格特質'
                '】1.學歷背景：大學以上資工、資管、資訊，或其他理工相關系所畢業。2.熱忱的學習態度，對HTML 5(加分)有關注。3.獨立解決與思'
                '辨問題的能力。4.樂於與使用者溝通。5.高度團隊合作精神。6.提供作品尤佳。【薪資待遇】1.歡迎人才好手主動應徵與面試談得好薪'
                '情！2.誠摯歡迎您能夠加入我們的行列。台語 : 略懂 ')
print get_skill('1. 協助工程師寫ASP.net (VB.net/C#  HTML  JavaScript) 2. 有程式基礎或喜歡寫程式 3. 喜歡與人溝通 4. 對英文有興趣'
                '或英文能力佳不拘')
print get_skill('熟悉微軟Windows Server系統為佳，必須具備MCSE  CCNA等相關證照，對電腦必須有高度的興趣及熱誠，願意學習新的電腦相關事務'
                '，有強烈企圖心不拘')
print get_skill('工作內容說明: 1.具備軟體開發設計及 Internet 程式設計概念2.熟悉 C# 語言及 .NET Framework 平台架構佳3.具關聯式資料庫'
                '概念，熟悉 SQL 語法佳4.有獨立程式開發能力，擅溝通協調與團隊合作5.無經驗可C#.NET')
print get_skill('1.負責系統分析、業務流程規劃設計及專案管理2.支援營業單位提供契客系統支援服務契約客戶專案規劃、問題溝通解決以及流程改善等'
                '。Word、PowerPoint、Outlook、Excel、Internet Explorer、MS SQL、Windows 2003、Windows 2000、Windows XP')
a = '1.Word、PowerPoint、Outlook、Excel、Internet Explorer、MS SQL、Windows 2003、Windows 2000、Windows XP'
a = "1. ".join(a.split("1."))
print get_skill(a)
'''

