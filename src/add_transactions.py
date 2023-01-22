import pandas as pd
import sqlite3

df = pd.DataFrame(data={
    'fund_name':['ppfas','ppfas','ppfas','ppfas','ppfas','ppfas','ppfas','ppfas','ppfas',],
    'txn_date':['2022-06-03', '2022-06-17','2022-08-02','2022-09-02','2022-09-21','2022-10-04','2022-11-02','2022-12-02','2023-01-03'],
    'top_up':[False,True,False,False,True,False,False,False,False],
    'purchase_price':[5000,10000,5000,5000,5000,5000,5000,5000,5000],
    'allotted_units':[101.37, 220.09, 98.72, 97.72, 96.17, 98.86, 96.7, 94.55, 97.6]
}, index=range(9))

print(df)

conn = sqlite3.connect('data/mutual-fund.db')

df.to_sql('txn_dim', conn, if_exists='replace',index=True)
