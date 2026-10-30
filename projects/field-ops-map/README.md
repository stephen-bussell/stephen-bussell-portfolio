# Field Operations Map

**Python · Pandas · Folium · Geocoding**

Application built for DSI Systems that accepts a data dump from Ossimview WebTracker and displays open work orders on an interactive map. Jobs can be filtered by status and by project type (Starlink or DTV).

## What It Does

- Ingests a CSV export from Ossimview WebTracker
- Geocodes ZIP codes to plot job locations
- Separates work into DTV and Starlink categories
- Clusters markers by status:
  - Open, Confirmed, En Route, On Site, Scheduled, Needs Re/Scheduled, Callback, Other
- Provides a tree-layer control to filter by project type and status
- Shows key job details in marker popups

## Tech Stack

- Python
- pandas
- folium (MarkerCluster + TreeLayerControl)
- geocoder (ArcGIS)

## Project Structure

```
field-ops-map/
├── FieldOps.ipynb      # Main notebook
└── README.md
```

## Notes

- Requires a CSV dump with the expected columns (City, State, ZIP, Project, LocationOrderStatus, etc.)
- Use anonymized or sample data for public demos
- Built for operational use at DSI Systems

---

*Part of the [Stephen Bussell Data Analytics Portfolio](https://github.com/stephen-bussell/stephen-bussell-portfolio)*
