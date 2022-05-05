# coding=utf-8

import math
import copy
import numpy as np
import pandas as pd
import os
from sklearn.impute import SimpleImputer 


mtcars=pd.read_csv('E:/MY_Github/Python-Learning-Notes/DataSet/mtcars.csv')
mtcars.rename(columns={'Unnamed: 0':'model'}, inplace=True)


mtcars.index=mtcars.model
del mtcars['model']
mtcars.head(4)
