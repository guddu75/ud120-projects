#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "rb") )
# print(type(data_dict))

# print(data_dict.keys())
# lst=[]
# # print(data_dict[list(data_dict.keys())[0]])
# k = list(data_dict.keys())
# print(k[103])
# print(type(data_dict[k[0]]['salary']))
# for i in range(len(k)):
#     # temp= (data_dict[k[i]]['salary'],int(i))
#     if data_dict[k[i]]['salary']=='NaN':
#         temp = (0,i);
#     else:
#         temp= (data_dict[k[i]]['salary'],i)
#     lst.append(temp)
#     # print(temp)

# lst.sort()
# print(lst)

data_dict.pop('TOTAL',0)

features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()



