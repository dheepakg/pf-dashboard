import pandas as pd
import sqlite3


txn_date = ['2022-06-03', '2022-06-17','2022-08-02','2022-09-02','2022-09-21',
            '2022-10-04','2022-11-02','2022-12-02','2023-01-03','2023-01-27','2023-02-02']

top_up = [False,True,False,False,True,False,False,False,False,True,False]
price_paid = [5000,10000,5000,5000,5000,5000,5000,5000,5000,5000,5000]

number_of_transaction = {len(txn_date), len(top_up), len(price_paid)}

# A Transaction is complete if it has txn_date, top_up, price_paid;
# If any of the above value is missing, Exit with exception
if len(number_of_transaction) > 1:
    exit('Transaction details is incomplete. Check entries')


df_ppfas = pd.DataFrame(data={
    'fund_name':['ppfas']*len(txn_date),
    'txn_date': txn_date,
    'top_up': top_up,
    'purchase_price': price_paid,
}, index=range(len(txn_date)))


df_ppfas["txn_date"] = pd.to_datetime(df_ppfas["txn_date"])

df_final = df_ppfas

conn = sqlite3.connect('data/mutual-fund.db')

df_final.to_sql('txn_dim', conn, if_exists='replace',index=True)
