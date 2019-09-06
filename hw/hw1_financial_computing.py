# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 14:54:51 2019

@author: JF LIU
"""

import numpy as np
L = list(np.random.choice(2,100,p=[.25,.75]))

#first try Y = 1+x1/1+x2+x3 E[Y] and Var[Y]. x~bernoulli(0.5)
N = 100000
Y_value = []
indicators = []
for i in range(N):
    x = list(np.random.choice(2,3,p=[.5,.5]))
    y = (1+x[0])/(1+x[1]+x[2])
    Y_value.append(y)
    if y >= 1:
        indicators.append(1)
    else:
        indicators.append(0)
indicators = np.array(indicators)
Y_value = np.array(Y_value)
EY = np.mean(Y_value)
VarY = np.var(Y_value)
print('estimated mean = '+str(EY))
print('estimated var = '+str(VarY))
print('P(Y>=1) = '+str(np.mean(indicators)))


#the exercises
def longest_run(B):
    longest_run = 0
    run_length = 1
    for i in range(1,len(B)):
        a = B[i-1]
        if B[i] == a:
            run_length = run_length + 1            
        else:
            if run_length > longest_run:
                longest_run = run_length
            run_length = 1
    if run_length > longest_run:
            longest_run = run_length
    return(longest_run)            
    
L = list(np.random.choice(2,20))
longest_run(L)
#print(L)

## HW1
#problem 1
import numpy as np
def longest_run(L):
    max_run = 0
    runlength = 1
    for i in range(1,len(L)):
        if L[i] == L[i-1]:
            runlength = runlength + 1
        else:
            if runlength > max_run:
                max_run = runlength
            runlength = 1
    if runlength > max_run:
        max_run = runlength
    return(max_run)
def mc_longestrun(N, p):
    """
    this function is to use MC methods to estimate EY and varY
    Y is the longest run of 100 xi
    xi ~ Bernoulli(p)
    N is number of trials
    """
    Y_value = []
    for i in range(0,N):
        X = list(np.random.choice(2,100,p=[p,1-p]))
        y = longest_run(X)
        Y_value.append(y)
    np.array(Y_value)
    EY = np.mean(Y_value)
    varY = np.var(Y_value)
    print('estimated mean of Y = '+str(EY))
    print('estimated var of Y = '+str(varY))
mc_longestrun(100000, .5)
mc_longestrun(100000, .55)

#problem 2
import numpy as np
def runlengths(L):
    runlength = 1
    list_of_runlength = []
    for i in range(1,len(L)):
        if L[i] == L[i-1]:
            runlength = runlength + 1
        else:
            list_of_runlength.append(runlength)
            runlength = 1
    list_of_runlength.append(runlength)
    return(list_of_runlength)

L = list(np.random.choice(2,20))
print(L)
runlengths(L)        

#problem 3
import numpy as np
def probability_Y():
    Y_value = []
    N = 100000
    for i in range(N):
        X = np.random.choice(2,100,p=[.5,.5])
        run_lengths = runlengths(X)
        if run_lengths.count(6) >= 3:
            Y_value.append(1)
        else:
            Y_value.append(0)
    np.array(Y_value)
    return("P(least three runs of length 6 occur) = "+str(np.mean(Y_value)))
    
probability_Y()            
            









































