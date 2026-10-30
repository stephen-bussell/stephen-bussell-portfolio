# Five-Year Weather Analysis

**Python • Open-Meteo API • Pandas • SQLAlchemy / SQLite • Unit Tests**

A command-line tool that retrieves five years of historical weather data for a chosen location and date, computes key aggregates, and stores the results in a SQLite database.

This project was completed as part of WGU’s D493 Scripting and Programming Applications course.

## What It Does

- Accepts latitude, longitude, month, day, and year
- Calls the Open-Meteo Archive API once per year (five years)
- Calculates:
  - Five-year mean temperature (°F)
  - Five-year maximum wind speed (mph)
  - Five-year total precipitation (inches)
- Stores the aggregated results in a local SQLite database via SQLAlchemy
- Prints a summary table of stored records
- Includes unit tests for the core calculation methods

## Tech Stack

- Python 3.8+
- `requests` — API calls
- `pandas` — data handling and aggregation
- `SQLAlchemy` — ORM / SQLite
- `tabulate` — formatted table output
- `unittest` / `pytest` — tests

## Project Structure

```
five-year-weather-analysis/
├── main.py              # Demo entry point
├── weather.py           # Weather and Weather_DB classes
├── test.py              # Unit tests
├── requirements.txt     # Dependencies
└── .gitignore
```

## How to Run

```bash
pip install -r requirements.txt
python main.py
python -m pytest test.py
```

The demo uses coordinates near Sioux Falls, SD (43.55, -96.70) for October 10.

## Notes

- The database file (`weather.db`) is created at runtime and is gitignored.
- API calls use the free Open-Meteo Archive endpoint.
- Unit tests mock the Weather object so they run without network access.

---

*Part of the [Stephen Bussell Data Analytics Portfolio](https://github.com/stephen-bussell/stephen-bussell-portfolio)*