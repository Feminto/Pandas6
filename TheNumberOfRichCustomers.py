# Method 1
import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    df = store[store['amount'] > 500]
    df = df['customer_id'].drop_duplicates()

    return pd.DataFrame([len(df)], columns = ['rich_count'])

# Method 2
import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    cust_set = set()
    for i in range(len(store)):
        a = store['amount'][i]
        c = store['customer_id'][i]

        if a > 500:
            cust_set.add(c)

    return pd.DataFrame([len(cust_set)],columns = ['rich_count'])

# Method 3
import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    df = store[store['amount'] > 500]
    df = df['customer_id'].nunique()

    return pd.DataFrame([df], columns = ['rich_count'])