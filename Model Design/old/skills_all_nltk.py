# -*- coding: utf8 -*-
import nltk
stemmer = nltk.PorterStemmer()

print stemmer.stem('analytic')
print stemmer.stem('analytical')
print stemmer.stem('analyzer')
print stemmer.stem('analyzing')

# rfile=open('skills_all.txt','r')
# skillset = rfile.readlines()
#
# rfile.close()
#
# skillset = skillset[0].split(',')
#
# wfile=open('skills_all_nltk.txt','w')
#
# for each in skillset:
#     w=''
#     eln = each.split(' ')
#     for word in eln:
#         w += stemmer.stem(word) + ' '
#     wfile.write(w + ',')
#
# wfile.close()