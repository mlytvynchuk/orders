import pandas as pd
from users.models import Customer
from datetime import datetime
def run():
    df = pd.read_csv('./scripts/TestData.csv', names=['first_name', 'last_name', 'born_date', 'register_date']
    , skiprows=1)
    for row in df.iterrows():
        first_name = row[1]['first_name']
        last_name = row[1]['last_name']
        born_date = row[1]['born_date'].replace('/','-')
        register_date = row[1]['register_date'].replace('/', '-')
        new_customer = Customer.objects.create(
            first_name=first_name,
            last_name=last_name,
            born_date=born_date,
            register_date=register_date,
        )

