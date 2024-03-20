import duckdb
import time


def duckdb_test():
    duckdb.sql("""
        SET preserve_insertion_order = false;
        SET temp_directory = './temp';
        CREATE VIEW metrics AS 
        SELECT date, SUM(failure) as failures
        FROM read_csv('*/*.csv', union_by_name = true)
        GROUP BY date;
    """)

    duckdb.sql("""
        COPY metrics TO 'results_duckdb.csv';
    """)

start_time = time.time()
duckdb_test()
end_time = time.time()
print(f"It took {end_time - start_time} seconds to run DuckDB test.")
