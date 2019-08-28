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
output:
  
sno
Income
count
10.00000
10.000000
mean
4.50000
30000.000000
std
3.02765
18856.180832
min
0.00000
10000.000000
25%
2.25000
20000.000000
50%
4.50000
25000.000000
75%
6.75000
37500.000000
max
9.00000
70000.000000


