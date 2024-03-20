# Experiments with OLAP libraries

This repository contains supplementary information and artifacts
for [the blog post](https://batyr.dev/tech/2024/03/17/data-analysis-with-less-memory.html) I wrote about data analysis with
larger-than-memory data.

## Setup

The setup assumes you have `poetry` installed locally.

1. Download raw data from [Backblaze's website](https://www.backblaze.com/cloud-storage/resources/hard-drive-test-data#downloadingTheRawTestData) and unzip them in the root directory.

2. Set up Python environment:

- `poetry shell`
- `poetry install`

3. Run experiments (e.g. polars):

- `python polars_main.py`
- `python duckdb_main.py`
- `python dask_main.py`