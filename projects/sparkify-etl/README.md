# Sparkify ETL Pipeline

**Python · PostgreSQL · ETL · Star Schema**

An ETL pipeline that processes song and user activity log data into a PostgreSQL database optimized for analytical queries. Built as part of the Udacity Data Modeling with Postgres project.

## Project Overview

Sparkify is a music streaming startup. This pipeline loads song metadata and user listening logs into a star schema so analysts can query user behavior, song popularity, and artist performance efficiently.

## Database Schema

**Fact table**
- `songplays` — records of individual song plays

**Dimension tables**
- `users` — user information
- `songs` — song metadata
- `artists` — artist information
- `time` — timestamp breakdowns for time-based analysis

## Files

- `create_tables.py` — Creates the database and tables
- `etl.py` — Processes JSON song and log files and loads them into Postgres
- `sql_queries.py` — All CREATE, DROP, and INSERT statements
- `data/` — Sample song and log JSON files (full dataset used during development)

## How to Run

1. Start a local PostgreSQL instance
2. Update the connection strings in `create_tables.py` and `etl.py` if needed (defaults use `user=student` / `password=student`)
3. Create the tables:
   ```bash
   python create_tables.py
   ```
4. Run the ETL pipeline:
   ```bash
   python etl.py
   ```

## Schema Design

A star schema was chosen because it:
- Optimizes analytical queries
- Separates facts from dimensions
- Supports efficient joins for reporting

## ETL Pipeline

1. **Song data**: Extracted from JSON files and loaded into `songs` and `artists`
2. **Log data**: Filtered to `NextSong` events, timestamps converted, and loaded into `time`, `users`, and `songplays`
3. Song and artist IDs are looked up during log processing to populate foreign keys in the fact table

## Notes

- The `data/` folder contains a small sample of the original JSON files for demonstration.
- The full dataset (71 song files + 30 log files) was used when developing and testing the pipeline.

---

*Part of the [Stephen Bussell Data Analytics Portfolio](https://github.com/stephen-bussell/stephen-bussell-portfolio)*
