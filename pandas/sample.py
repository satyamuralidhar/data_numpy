import pandas as pd
salary = {'sno':[0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9],'Name':['satya','mohan','teja','ram','pavan','vijay','sai','lakshman','bhanu','subbu'],'Income':[20000 , 30000 , 40000 , 10000 , 50000 , 10000 , 30000 , 20000 , 70000 , 20000]}
df= pd.DataFrame(salary)
print(df)

df.info()

df.query('Income > 10000').plot(kind = 'scatter' , x = 'sno' , y = 'Income')

df.mean(0)

df.mean(1)

df.sum(0 , skipna = False)

df.sum(0 , skipna = 'True')

df.sum(1 , skipna = False)

df.sum(1 , skipna = 'True')

df.describe()

df.describe(percentiles = [.25 , .85 , .99])


import numpy as np
data = np.random.randint(100 , 200 , size = 10)

print(data)

import pandas as pd
pd.Series(data).value_counts()

import pandas as pd
pd.Series(data).mode()
