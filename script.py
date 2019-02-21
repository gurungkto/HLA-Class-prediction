
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import sklearn
from sklearn import datasets
import os
os.getcwd()
os.chdir('C:\\Users\\HGURUNG1\\Desktop\\HG\\scripts')

data = sns.load_dataset("diamonds")
data.shape
data.describe

sns.boxplot(data.color, data.price)
