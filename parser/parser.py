import pandas as pd

df = pd.read_csv('TestData.csv', names=['first_name', 'last_name', 'born_date', 'register_date']
, skiprows=1)
for row in df.iterrows():
    first_name = row[1]['first_name']
    last_name = row[1]['last_name']
    born_date = row[1]['born_date']
    register_date = row[1]['register_date']
    print(register_date)
