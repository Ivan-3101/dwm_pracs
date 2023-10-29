from apriori_python import apriori
# itemSetList = [['eggs', 'bacon', 'soup'],
#                 ['eggs', 'bacon', 'apple'],
#                 ['soup', 'bacon', 'banana']]
itemSetList = [['M', 'O', 'N','K','E','Y'],
                ['D', 'O', 'N','K','E','Y'],
                ['M', 'A','K','E'],
               ['M', 'U', 'C','K','Y'],
               ['C', 'O', 'O','K','E']]

freqItemSet, rules = apriori(itemSetList, minSup=0.6, minConf=0.8)
print(rules)  
# [[{'beer'}, {'rice'}, 0.6666666666666666], [{'rice'}, {'beer'}, 1.0]]
# rules[0] --> rules[1], confidence = rules[2]