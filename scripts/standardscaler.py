import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
import seaborn as sns

np.random.seed(1)
df = pd.DataFrame({
    'x1':np.random.normal(0,1,100),
    'x2':np.random.normal(1,5,100),
    'x3':np.random.normal(-1,5,100)
})
df

#import dataframe into scaled_df and then converted into standard scaler
scaler = preprocessing.StandardScaler()
scaled_df = scaler.fit_transform(df)
scaled_df = pd.DataFrame(scaled_df , columns = ['x1','x2','x3'])
scaled_df

fig, (ax1,ax2)=plt.subplots(ncols=2 , figsize=(14,8))
ax1.set_title("before scaling")
sns.kdeplot(df['x1'],ax=ax1)
sns.kdeplot(df['x2'],ax=ax1)
sns.kdeplot(df['x3'],ax=ax1)
ax2.set_title("after Standard Scaling")
sns.kdeplot(scaled_df['x1'],ax=ax2)
sns.kdeplot(scaled_df['x2'],ax=ax2)
sns.kdeplot(scaled_df['x3'],ax=ax2)
plt.show()
