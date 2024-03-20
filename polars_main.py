import polars as pl
import time

# Uncomment line below for more logs.
# pl.Config.set_verbose(True)

def polars_test():
    lazy_df = pl.scan_csv("*/*.csv")

    sql = pl.SQLContext()
    sql.register("harddrives", lazy_df)   
    results = sql.execute("""
        SELECT date, SUM(failure) as failures
        FROM harddrives 
        GROUP BY date
    """)

    results_filename = "results_polars.csv"
    results_compiled = results.collect(streaming=True)
    print(results_compiled.estimated_size("kb"))
    results_compiled.write_csv(results_filename)

start_time = time.time()
polars_test()
end_time = time.time()
print(f"It took {end_time - start_time} seconds to run Polars test.")