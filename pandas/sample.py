import pandas as pd
salary = {'sno':[0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9],'Name':['satya','mohan','teja','ram','pavan','vijay','sai','lakshman','bhanu','subbu'],'Income':[20000 , 30000 , 40000 , 10000 , 50000 , 10000 , 30000 , 20000 , 70000 , 20000]}
df= pd.DataFrame(salary)
print(df)

df.info()

df.query('Income > 10000').plot(kind = 'scatter' , x = 'sno' , y = 'Income')

