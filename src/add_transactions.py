import pandas as pd
import sqlite3


txn_date = ['2022-06-03', '2022-06-17','2022-08-02','2022-09-02','2022-09-21',
            '2022-10-04','2022-11-02','2022-12-02','2023-01-03','2023-01-27',
            '2023-02-02']

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



txn_date = ['2020-04-30', '2020-06-01', '2020-07-01', '2020-08-03', '2020-09-01',
            '2020-10-01', '2020-11-02', '2020-12-01', '2021-01-01', '2021-02-05',
            '2021-03-02', '2021-04-05', '2021-04-12', '2021-05-04', '2021-06-02',
            '2021-07-02', '2021-08-03', '2021-09-02', '2021-10-04', '2021-11-02',
            '2021-12-02', '2022-01-04', '2022-02-02', '2022-03-03', '2022-04-04',
            '2022-05-04', '2022-06-02', '2022-06-17', '2022-07-04', '2022-08-02',
            '2022-09-02', '2022-09-26', '2022-10-04', '2022-11-02', '2022-12-02',
            '2023-01-03', '2023-02-02']

top_up = [False, False, False, False, False,
          False, False, False, False, False,
          False, False, True,  False, False,
          False, False, False, False, False,
          False, False, False, False, False,
          False, False,  True, False, False,
          False,  True, False, False, False,
          False, False,
          ]
price_paid = [3000,   3000,  3000,  3000,  3000,
              5000,   5000,  5000,  5000,  5000,
              5000,   5000, 10000,  5000, 10000,
              10000, 10000, 10000, 10000, 10000,
              10000, 10000, 10000, 10000, 10000,
              10000, 10000,  5000, 10000, 10000,
              10000, 10000, 10000, 10000, 10000,
              10000, 10000]


df_nifty50 = pd.DataFrame(data={
    'fund_name':['nifty50']*len(txn_date),
    'txn_date': txn_date,
    'top_up': top_up,
    'purchase_price': price_paid,
}, index=range(len(txn_date)))

df_final = pd.concat([df_ppfas, df_nifty50], axis=0, ignore_index=True)


df_final["txn_date"] = pd.to_datetime(df_final["txn_date"])
print(df_final)

conn = sqlite3.connect('data/mutual-fund.db')

df_final.to_sql('txn_dim', conn, if_exists='replace',index=True)
