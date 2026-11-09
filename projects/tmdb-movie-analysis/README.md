# TMDb Movie Data Analysis

**Python · Pandas · NumPy · Exploratory Data Analysis**

Analysis of ~10,000 movies from The Movie Database (TMDb) exploring factors related to profit, changes in movie quality over time, and the relationship between budget and ratings.

## Questions Explored

1. **What factors are associated with higher profit?**
   - Examined runtime, genre, director, cast, and production company
   - No strong link between runtime and profit
   - Certain genres, directors, cast members, and studios appeared more frequently among high-profit films

2. **How has movie quality changed over time?**
   - Average rating has declined since the 1970s
   - Average budget has risen
   - Average profit has also declined over the same period

3. **Is there a relationship between budget and rating?**
   - Correlation of ~0.04 (very weak)
   - Higher budgets are not associated with higher ratings in this dataset

## Tech Stack

- Python
- pandas
- NumPy
- Matplotlib (for visualizations)

## Key Findings

- Financial analyses used ~3,700 movies with complete budget/revenue data
- Average ratings have trended downward while budgets increased
- No meaningful relationship between production budget and user rating

## Limitations

- Many movies missing financial data
- Averages by director/cast/studio can be skewed by small sample sizes
- Possible changes in how TMDb calculates ratings over time

## Project Structure

```
tmdb-movie-analysis/
├── Investigate_a_Dataset.ipynb   # Full analysis notebook
└── README.md
```

---

*Part of the [Stephen Bussell Data Analytics Portfolio](https://github.com/stephen-bussell/stephen-bussell-portfolio)*
