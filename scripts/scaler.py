import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
import seaborn as sns

np.random.seed(1)
df = pd.DataFrame({
    'x1':np.random.normal(2,5,100),
    'x2':np.random.normal(1,2,100),
    'x3':np.random.normal(-1,5,100)
})
df

#import dataframe into scaled_df and then converted into standard scaler
scaler = preprocessing.MinMaxScaler()
scaled_df = scaler.fit_transform(df)
scaled_df = pd.DataFrame(scaled_df , columns = ['x1','x2','x3'])
scaled_df
scaler2= preprocessing.Normalizer()
scaled_df2 = scaler2.fit_transform(df)
scaled_df2 = pd.DataFrame(scaled_df2, columns = ['y1', 'y2' , 'y3'])
scaled_df2
scaler3= preprocessing.StandardScaler()
scaled_df3 = scaler3.fit_transform(df)
scaled_df3 = pd.DataFrame(scaled_df3, columns = ['z1', 'z2' , 'z3'])
scaled_df3

fig, (ax1,ax2,ax3,ax4)=plt.subplots(ncols=4 , figsize=(25,7))
ax1.set_title("before scaling")
sns.kdeplot(df['x1'],ax=ax1)
sns.kdeplot(df['x2'],ax=ax1)
sns.kdeplot(df['x3'],ax=ax1)

ax2.set_title("after min max Scaling")
sns.kdeplot(scaled_df['x1'],ax=ax2)
sns.kdeplot(scaled_df['x2'],ax=ax2)
sns.kdeplot(scaled_df['x3'],ax=ax2)

ax3.set_title("after normalizer scaling")
sns.kdeplot(scaled_df2['y1'],ax=ax3)
sns.kdeplot(scaled_df2['y2'],ax=ax3)
sns.kdeplot(scaled_df2['y3'],ax=ax3)

ax4.set_title("after standard scaler")
sns.kdeplot(scaled_df3['z1'],ax=ax4)
sns.kdeplot(scaled_df3['z2'],ax=ax4)
sns.kdeplot(scaled_df3['z3'],ax=ax4)
plt.show()
