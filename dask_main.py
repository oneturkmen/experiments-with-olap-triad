import dask.dataframe as dd 
import time


def dask_test():
    dfs = dd.read_csv("*/*.csv", dtype={'failure': 'float64'})
    result_df = dfs.groupby("date").failure.sum()
    result_df.to_csv("results_dask.csv", single_file=True)

start_time = time.time()
dask_test()
end_time = time.time()
print(f"It took {end_time - start_time} seconds to run Dask test.")
