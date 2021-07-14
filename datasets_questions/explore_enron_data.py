#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

# print(type(enron_da))
# print(enron_data.keys())
# print(len(enron_data[list(enron_data.keys())[0]]))
cnt=0
cnt1=0
for person in enron_data.keys():
    if enron_data[person]['poi']:
        cnt1+=1
        if enron_data[person]['total_payments']=="NaN":
            cnt+=1
    

print(cnt1,cnt)

# a= enron_data["SKILLING JEFFREY K"]['total_payments']
# b= enron_data["LAY KENNETH L"]['total_payments']
# c= enron_data["FASTOW ANDREW S"]['total_payments']

# print(max(a,b,c))


