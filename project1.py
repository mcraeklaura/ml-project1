#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
    Created on Thu Oct  5 16:24:22 2017
    
    @author: lauramcrae
    """

import numpy as np
from pandas import read_csv
import pandas as pd
from sklearn.pipeline import Pipeline


## Data Preparation
dat = read_csv("/Users/lauramcrae/Desktop/train.csv")
## With and without the -1, because it could be of significance.
count_nan = len(dat) - dat.count()
print "Number of NaNs", count_nan
## There are no null values that need to be dealt with
## Make a different copy of the data to see if the -1s have a significance

## Information about the data ##
## bin to indicate binary features
## cat to indicate categorical features
## without; either continuous or ordinal
X = dat.loc[:, dat.columns != "target"]
y = dat.loc[:, "target"]

print "Values of target", y.unique()
for i in X.columns:
    print i, dat.loc[:, i].unique()
print "We can see that all the categorical columns are numbers. We can convert those"

## Transforming the -1
X_no_neg = X
y_no_neg = y
cat = pd.DataFrame()
bn = pd.DataFrame()
norm = pd.DataFrame()
for i in X.columns:
    if "cat" in i:
        # Transform Median
        cat[i] = dat.loc[:, i]
    elif "bin" in i:
        # Transform
        bn[i] = dat.loc[:, i]
    else:
        # Do something
        norm[i] = dat.loc[:, i]

#pipe = Pipeline([
#       ("remove_neg_ones", Imputer(missing_values=-1, strategy="mean")),
#        ("z-scaling", StandardScaler())
#        ])
tmp = 0
for i in cat.columns:
    cat.loc[cat[i] == -1, i] = np.median(cat.loc[cat[i] != -1,i])
    tmp = tmp + sum(cat[i] == -1)
print "Number of -1 in data:", tmp

tmp = 0
for i in bn.columns:
    tmp = tmp + sum(bn[i] == -1)
    print i, ":", tmp
print "There are no negatives in bin columns"


mx = 0
for i in norm.columns:
    tmp = 0
    tmp = tmp + sum(norm[i] == -1)
    print i, ":", tmp
    if mx < tmp:
        mx=tmp

print "~", mx/float(len(norm)) * 100, "% of the data is missing, so we are going to assume that\nthere is significance that the data is missing"
num_missing_per_row = np.zeros(len(norm))
tmp = 0
for index, row in norm.iterrows():
    print row
    break
    num_missing_per_row[index] =  sum(row == -1)

## Data Exploration

##
