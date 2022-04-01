import pandas as pd
import numpy as np
import time

def logger(func):
    def wrapper(*args, **kwargs):
        print("Running the Sequential Program")
        t1 = time.time()
        func(*args)
        print(f"Time Take {time.time() - t1} secs...")

    return wrapper

@logger
def process_csv(df=pd.DataFrame()):
    """using Dataframes"""
    df["col3"] = df[['col1']].add(df['col2'].replace(0, np.inf), axis=0).fillna(0)
    return df

def read_csv(file_name="input.csv"):
    try:
        df = pd.read_csv(file_name)
        return df
    except Exception as ex:
        print("Exception while reading the file", ex)

def write_csv(df=pd.DataFrame(), file_name="output.csv"):
    df.to_csv('output.csv', index=False)

if __name__ == "__main__":
    df = read_csv()
    process_csv(df)
    # write_csv(df)