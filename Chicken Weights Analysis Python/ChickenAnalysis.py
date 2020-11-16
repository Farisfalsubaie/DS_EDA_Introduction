import math 
import pandas as pd 
import numpy as np 
import seaborn as sns
from scipy import stats
from scipy.stats import ttest_ind
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.formula.api import ols


Chick_DATA = pd.read_csv('data/Chick_Weights.txt')
Chick_DATA.columns = ["weight","feed"]
print(Chick_DATA)
Chick_DATA.info()
Chick_DATA.describe()
#Calculate the mean and standard deviation for each group.
np.mean(Chick_DATA['weight']).describe()
np.mean(weight)
np.std('weight')
np.std(Chick_DATA['weight']).describe()
#Calculate the number of chicks in each group.
Chick_DATA.groupby('feed')[['weight']].len()
#Calculate a within-group z-score.
model = ols("weight ~ feed", Chick_DATA)

results = model.fit()
results.summary()
#Produce a strip chart showing each chick as an individual data point
sns.catplot(x="feed", y="weight", data=Chick_DATA)

#Calculate a 1-way ANOVA.
aov_table = sm.stats.anova_lm(results, typ=2)

aov_table
#Calculate Tukey’s post-hoc test (i.e. p-values for all pair-wise t-tests)