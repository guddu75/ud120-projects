#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()





#########################################################
### your code goes here ###

# x = len(features_train)
# y = len(labels_train)

# features_train = features_train[:(x//100)]
# labels_train = labels_train[:(y//100)]

# ls= [10.0,100.0,1000.0,10000.0]
# # ls= [1.0]

# for c in ls:
#     clf = SVC(kernel="rbf",C=c, gamma= "auto")

#     t0 = time()

#     clf.fit(features_train,labels_train)

#     print("training time: ", round(time()-t0,3) , "s" )

#     t0 = time()

#     pred=clf.predict(features_test)

#     print("prediction time: ", round(time()-t0,3) , "s" )


#     score = accuracy_score(labels_test,pred)

#     print("C =",c,",score =",score);

clf = SVC(kernel="rbf",C=10000.0, gamma= "auto")

t0 = time()

clf.fit(features_train,labels_train)

print("training time: ", round(time()-t0,3) , "s" )

t0 = time()

pred=clf.predict(features_test)

print("prediction time: ", round(time()-t0,3) , "s" )

# print(pred[10],pred[26],pred[50])
cnt=0
for i in pred:
    if i:
        cnt+=1

print(cnt)

# score = accuracy_score(labels_test,pred)


# print(score)

#########################################################


