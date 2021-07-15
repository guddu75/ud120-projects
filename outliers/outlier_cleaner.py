#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    a=[]
    b=[]
    c=[]
    for i in range(len(ages)):
        a.append((abs(predictions[i][0]-net_worths[i][0]))**2)
        b.append(ages[i][0])
        c.append(net_worths[i][0])
    # print(a)
    # print(b)
    # print(c)
    lst=[]
    for i in range(len(ages)):
        lst.append((a[i],b[i],c[i]));
    
    lst.sort()
    for a,b,c in lst:
        print(a,b,c)
    
    cleaned_data = []
    for error , age , nw in lst:
        cleaned_data.append((age,nw,error))
    ### your code goes here
    cleaned_data = cleaned_data[:81]

    
    return cleaned_data

