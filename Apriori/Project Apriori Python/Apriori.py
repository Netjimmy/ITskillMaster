# py3
# coding=utf-8

import sys

reload(sys)
sys.setdefaultencoding("utf-8")  # 避免字型轉碼錯誤

def apriori(D, minSup):
    # 频繁項目集用keys表示，key表示項目集中的某一項，cutKeys表示經過修剪的某k項目集。C表示某k項目集的每一項在D中的支持個數

    C1 = {}
    for T in D:  # 跑最外面的list
        for I in T:  # 跑每個大list裡面的小list
            if I in C1:  # 如果裡面的內容有在字典裡面，有的話+1，沒有的話，加入字典初始為1
                C1[I] += 1
            else:
                C1[I] = 1

    _keys1 = C1.keys()  # 取出c1.keys()成為另一個暫時變數(變數名前加上_,為暫時變數)

    keys1 = []  # 把每個keys把他變成獨立的list然後再塞入一個list 成[[A],[B],[C].....]
    for i in _keys1:
        keys1.append([i])

    n = len(D)
    cutKeys1 = []
    for k in keys1[:]:  # 跑keys1裡的項目，如果項目數量大於最小支持數的話，則加入cutkeys1
        if C1[k[0]] * 1.0 / n >= minSup:
            cutKeys1.append(k)
    cutKeys1.sort()  # 排序

    keys = cutKeys1  # 目前項目集裡面的項目(keys)
    all_keys = []
    while keys != []:
        C = getC(D, keys)  # 計算目前所有個key所在T的數量
        cutKeys = getCutKeys(keys, C, minSup, D)  # 刪掉沒有大於最小支持數的項目keys
        for key in cutKeys:
            all_keys.append(key)
        keys = aproiri_gen(cutKeys)
    return all_keys

def getC(D, keys):
    # 對目前尚有的keys進行計數

    C = []
    for key in keys:
        c = 0
        for T in D:
            have = True
            for k in key:
                if k not in T:
                    have = False
            if have:
                c += 1
        C.append(c)
    return C

def getCutKeys(keys, C, minSup, D):
    # 判斷這個項目有沒有大於最小支持數

    for key in keys[:]:
        num = 0
        for T in D:
            if keyInT(key, T):
                num += 1
        if num * 1.0 / len(D) < minSup:
            keys.remove(key)

    return keys

def keyInT(key, T):
    # 判斷項目keys有沒有在項目集T裡面

    for k in key:
        if k not in T:
            return False
    return True

def aproiri_gen(keys1):
    # 連起來

    keys2 = []
    for k1 in keys1:
        for k2 in keys1:
            if k1 != k2:
                key = []
                for k in k1:
                    if k not in key:
                        key.append(k)
                for k in k2:
                    if k not in key:
                        key.append(k)
                key.sort()
                if key not in keys2:
                    keys2.append(key)
    return keys2

# ---------------------------------------------------------------------------------------------------------------------

# testData = [['牛奶', '尿布', '啤酒'], ['牛奶', '香菸', '啤酒'], ['牛奶', '啤酒', '尿布']]

import Apriori_Data as AD

Data = AD.get_skill_list()

F = apriori(Data, 0.01)
for i in F:
    if len(i) >= 2:
        print (",".join(i)).encode('utf-8')
