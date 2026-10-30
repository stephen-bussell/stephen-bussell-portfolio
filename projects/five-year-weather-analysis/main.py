from weather import Weather, Weather_DB

# create an instance of the class in part C1 to call the methods used in
# part C2 for the daily weather variables.

weather = Weather(43.55, -96.70, 10, 10, 2026)

print(f'Mean temp: {weather.get_mean_temp()}')
print(f'Max wind: {weather.get_max_wind()}')
print(f'Precipitation sum: {weather.get_precip_sum()}')

# C5 Populate the table created in part C4 with the weather data
# for the chosen location and date.

sql_weather = Weather_DB(weather)
sql_weather.get_sql()
