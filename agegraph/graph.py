import numpy as np
import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt

data = {
    'Name':['satya' , 'Murali' , 'vijay' ,'pavan' ,'mohan' , 'durga', 'sam' , 'ram' ,'kalyan' ,'mani' , 'satish' , 'teja' , 'surya' , 'chandra'] , 'Age':[21 , 24 ,22 , 34 ,35, 24, 27, 31, 24, 23, 25 , 29 , 31, 29] ,'Department':['IT','IT','MECH','IT','PETROLIUM','ITI','CIVIL','MERINE','AERONAUTICS','HR','CIVIL','DOCTOR','AGRICULTURE','MECH']
}

df = pd.DataFrame(data)

df

#scatter plot:

import matplotlib.pyplot as plt
sns.FacetGrid(data = df , hue = 'Name' , size = 8).map(plt.scatter , 'Age' ,'Department').add_legend()
plt.show()



#bar plot:

import matplotlib.pyplot as plt
sns.FacetGrid(data = df , hue = 'Name' , size = 8).map(plt.bar , 'Age' ,'Department').add_legend()
plt.show()
