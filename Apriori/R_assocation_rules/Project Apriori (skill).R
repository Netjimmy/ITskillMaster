# http://www.idatacamp.com/2015/09/09/%E7%94%A8r%E8%AF%AD%E8%A8%80%E8%BF%9B%E8%A1%8C%E8%B4%AD%E7%89%A9%E7%AF%AE%E5%88%86%E6%9E%90%EF%BC%88%E5%85%B3%E8%81%94%E8%A7%84%E5%88%99%EF%BC%89/

install.packages("arules")
library(arules)

workpath <- "E:/Project/Analysis/R_assocation_rules"
setwd(workpath)     # Set working directory. Make c:\temp directory and copy csv file to the directory
getwd()             # Get working directory

data = read.transactions('data/skill.txt', format = 'basket', sep = ',', cols = NULL, encoding = 'utf-8')

# data = read.transactions(file, format =('basket', 'single'), sep = NULL, cols = NULL / n / c(n, n), rm.duplicates = FALSE, encoding = 'unknown')
# file : Data file.

# format : Can be 'basket' or 'single'

# basket : 
# item1,item2
# item1
# item2,item3

# single :
# ID1 item1
# ID2 item1
# ID2 item2

# sep : Default = ' '

# cols:
# > basket : col = 1                    col = null
#            ID1 item1, item2           item1, item2
#            ID2 item1                  item1
#            ID3 item2, item3           item2, item3
# > single : col = c(1,2)
#            ID1 item1
#            ID2 item1
#            ID2 item2

# rm.duplicates : Remove duplicate data.

rules <- apriori(data, parameter = list(supp = 0.02, conf = 0.5, minlen = 2, target='rules'))
rules
inspect(rules[1:26])

rules.sorted_lift = sort(rules, by = 'lift')
rules.sorted_lift
inspect(rules.sorted_lift)

itemset <- apriori(data, parameter = list(supp = 0.02, conf = 0.5, minlen = 4, target='frequent itemsets'))
itemset
inspect(itemset)

# rules / itemset <- apriori(data,  parameter = list(supp = 0.1, conf = 0.8, maxlen = 10, minlen = 1, target = 'rules' / 'frequent itemsets'))
# parameter : Default setting > parameter = list(supp = 0.1, conf = 0.8, maxlen = 10, minlen = 1, target = 'rules' / 'frequent itemsets')
# supp = support
# conf = confidence
# maxlen / minlen = n
# target : 'rules' / 'frequent itemsets'

# rules.sorted_sup = sort(rules, by = 'support')
# rules.sorted_con = sort(rules, by = 'confidence')
# rules.sorted_lift = sort(rules, by = 'lift')

