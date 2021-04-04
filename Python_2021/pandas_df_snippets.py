import pandas as pd
import numpy as np

# 1.) RENAMING A COLUMNS
df = pd.DataFrame()
df = df.rename(columns={'col1': 'col11', 'col2': 'col22'})

# 2.) Change the datatype to NUMERIC, use downcast to get the whole number
pd.to_numeric('columns_name', downcast='integer', errors='coerce')

# 3.) Change the DF datetime to python datetime
pd.to_datetime('col_name', format='%Y-%m-%d').dt.date

# 4.) Divide one column by another..with inf values handle
df[['col_name']].div(df['col_name2'].replace(0, np.inf), axis=0).fillna(0)
