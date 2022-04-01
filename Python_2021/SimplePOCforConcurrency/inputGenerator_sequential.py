import time
from random import randint
import pandas as pd
from inpurt_generator_multiprocess import write_csv

def logger(func):
    def wrapper(*args, **kwargs):
        print("Running the Sequential Program")
        t1 = time.time()
        func(*args)
        print(f"Completed in {time.time() - t1} secs...")

    return wrapper

@logger
def generate_input_data(size=10, start=1, end=100):
    df = pd.DataFrame()
    df["col1"] = None
    df["col2"] = None
    t1 = time.time()
    for idx in range(size+1):
        if idx % 10000 == 0:
            print(f"PROCESSED {idx} RECORDS in {time.time() - t1} seconds")
            t1 = time.time()
        df.loc[idx, "col1"] = randint(start, end)
        df.loc[idx, "col2"] = randint(start, end)

    return df

def write_csv(df=pd.DataFrame()):
    df.to_csv('input.csv', index=False)


if __name__ == "__main__":
    df = generate_input_data(100, 5_00_000, 50_00_000)
    print(df)
    # write_csv(df)
    # Running the Sequential Program
    # PROCESSED 0 RECORDS in 0.0 seconds
    # PROCESSED 10000 RECORDS in 4.154920816421509 seconds
    # PROCESSED 20000 RECORDS in 8.992029190063477 seconds
    # PROCESSED 30000 RECORDS in 17.9750497341156 seconds
    # PROCESSED 40000 RECORDS in 27.231124877929688 seconds
    # PROCESSED 50000 RECORDS in 34.2157039642334 seconds
    # PROCESSED 60000 RECORDS in 46.894859790802 seconds
    # PROCESSED 70000 RECORDS in 51.749632120132446 seconds
    # PROCESSED 80000 RECORDS in 57.4184045791626 seconds
    # PROCESSED 90000 RECORDS in 63.300256967544556 seconds
    # PROCESSED 100000 RECORDS in 67.7557463645935 seconds
    # Completed in 379.6987371444702 secs...
    #
    # Process finished with exit code 0