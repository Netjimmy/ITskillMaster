#coding=utf-8
import cPickle as pickle
import MySQLdb
import json
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import sys
from sklearn.metrics import silhouette_samples, silhouette_score
import matplotlib.cm as cm
import numpy as np
import time

set_skill = pickle.load(file('dic\set_skill_v8_500.data'))

list_skill = sorted(set_skill)

db = MySQLdb.connect("10.120.26.46","yang","iiizb104","project" )
cursor = db.cursor()
# sql = "SELECT skill FROM project.job where jobno between 1 AND 1000"
sql = "SELECT jobno, skill FROM project.jobstorage WHERE skill NOT REGEXP '{}';"
cursor.execute(sql)
results = cursor.fetchall()

list_of_lists = []
jobnoList = []

for row in results:
    jobnoList.append(row[0])
    tmpdic = json.loads(row[1])
    # for each in tmpdic:
    #     tmpdic[each]=1
    for each in set_skill:
        if each not in tmpdic:
            tmpdic[each]=0
    tmpList = []
    for each in list_skill:
        tmpList.append(tmpdic[each])
    # 空值陣列踢除
    # if tmpList != np.zeros(len(set_skill)).tolist():
    list_of_lists.append(tmpList)
db.close()

transformer = TfidfTransformer()
X = transformer.fit_transform(list_of_lists)

print sys.getsizeof(list_of_lists)
# 畫圖

cBegin = 10
interval = 10
cEnd = 101

dic_record = []
time_record = []
y_savg = []
x_clusters = []


for cluster in range(cBegin,cEnd,interval):
    ts = time.time()
    np.set_printoptions(threshold='nan')

    from sklearn.cluster import KMeans
    cluster_labels = KMeans(n_clusters=cluster).fit_predict(X)

    te = time.time()
    # sample_silhouette_values = silhouette_samples(X, cluster_labels)

    time_record.append(te-ts)

    print ('cluster ' + str(cluster) + ':' + str(te-ts))

#     # 各群分布圖
#     fig, ax = plt.subplots()
#     fig.set_size_inches(18, 7)
#
#     ax.set_xlim([-0.1, 1])
#     ax.set_ylim([0, len(X.toarray()) + (cluster + 1) * 10])
#
#     silhouette_avg = silhouette_score(X, cluster_labels)
#     # print("For n_clusters =", cluster,\
#     #       "The average silhouette_score is :", silhouette_avg)
#
#     # 各群趨勢圖
#     x_clusters.append(cluster)
#     y_savg.append(silhouette_avg)
#
#     y_lower = 10
#     for i in range(cluster):
#         # Aggregate the silhouette scores for samples belonging to
#         # cluster i, and sort them
#         ith_cluster_silhouette_values = \
#             sample_silhouette_values[cluster_labels == i]
#
#         ith_cluster_silhouette_values.sort()
#
#         size_cluster_i = ith_cluster_silhouette_values.shape[0]
#         y_upper = y_lower + size_cluster_i
#
#         color = cm.spectral(float(i) / cluster)
#         ax.fill_betweenx(np.arange(y_lower, y_upper),
#                           0, ith_cluster_silhouette_values,
#                           facecolor=color, edgecolor=color, alpha=0.7)
#
#         # Label the silhouette plots with their cluster numbers at the middle
#         ax.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))
#
#         # Compute the new y_lower for next plot
#         y_lower = y_upper + 10  # 10 for the 0 samples
#
#     ax.set_title("The silhouette plot for the various clusters.")
#     ax.set_xlabel("The silhouette coefficient values")
#     ax.set_ylabel("Cluster label")
#
#     # The vertical line for average silhoutte score of all the values
#     ax.axvline(x=silhouette_avg, color="red", linestyle="--")
#
#     ax.set_yticks([])  # Clear the yaxis labels / ticks
#     ax.set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])
#
#     plt.show()
#
# plt.plot(x_clusters, y_savg)

# print [i for i, j in enumerate(y_savg) if j == max(y_savg)]
# print ('max value:', max(y_savg))

# plt.show()

dic_record.append(x_clusters)
dic_record.append(time_record)
dic_record.append(y_savg)

with open('time_record_v3.json', 'w') as f:
    json.dump(dic_record, f)



