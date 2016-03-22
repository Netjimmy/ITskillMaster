# coding=utf-8
from nltk.util import ngrams

def ngram(x):  # 傳入List
    # sentence = x
    outary = []
    for n in range(1,5):
        grams = ngrams(x, n)
        for gram in grams:
            soutstr = ''
            for i in range(0,n):
                if len(soutstr) == 0:
                    soutstr = gram[i]
                else:
                    soutstr = soutstr + ' ' + gram[i]
            outary.append(soutstr)
    return outary  # 回傳list

