import duckdb
import time


def duckdb_test():
    # create a connection to a file called 'file.db'
    with duckdb.connect("persistent_database.db") as con:
        con.sql("""
            SET preserve_insertion_order = false;
            SET temp_directory = './temp';
            CREATE VIEW metrics AS 
            SELECT date, SUM(failure) as failures
            FROM read_csv('*/*.csv', union_by_name = true)
            GROUP BY date;
        """)

        con.sql("""
            COPY metrics TO 'results_persistentmode_duckdb.csv';
        """)

start_time = time.time()
duckdb_test()
end_time = time.time()
print(f"It took {end_time - start_time} seconds to run DuckDB test.")
