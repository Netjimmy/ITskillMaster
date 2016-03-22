#coding=utf-8
import cPickle as pickle

#存檔
tmp = set()
w = open('dic\skillList.txt','r')
for each in w:
    tmp.add(each[:-1])

#讀檔

pickle.dump(tmp, file('dic\set_skill.data', 'w'))