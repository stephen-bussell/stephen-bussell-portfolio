import requests
import sqlalchemy as sql
import sqlalchemy.orm as orm
import pandas as pd
from tabulate import tabulate

# C1 class
class Weather:
    def __init__(self, lat, lon, month, day, year):
        self.lat = lat
        self.lon = lon
        self.month = month
        self.day = day
        self.year = year

        df = pd.DataFrame(columns=['date',
                                   'temperature_2m_min',
                                   'temperature_2m_mean',
                                   'temperature_2m_max',
                                   'precipitation_sum',
                                   'wind_speed_min',
                                   'wind_speed_mean',
                                   'wind_speed_max'])

        for i in range(self.year - 5, self.year):
            self.date = f'{i}-{self.month:02d}-{self.day:02d}'
            url = 'https://archive-api.open-meteo.com/v1/archive'
            params = {
                'latitude': self.lat,
                'longitude': self.lon,
                'start_date': self.date,
                'end_date': self.date,
                'daily': ['temperature_2m_max', 'temperature_2m_min', 'temperature_2m_mean', 'precipitation_sum',
                          'rain_sum'],
                'hourly': 'wind_speed_10m',
                'temperature_unit': 'fahrenheit',
                'wind_speed_unit': 'mph',
                'precipitation_unit': 'inch',
            }
            response = requests.get(url, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()

            daily = data['daily']
            hourly = data['hourly']
            avg_wind = sum(hourly['wind_speed_10m']) / len(hourly['wind_speed_10m'])

            row = [{'date': hourly['time'][0],
                    'temperature_2m_min': daily['temperature_2m_min'][0],
                    'temperature_2m_mean': daily['temperature_2m_mean'][0],
                    'temperature_2m_max': daily['temperature_2m_max'][0],
                    'precipitation_sum': daily['precipitation_sum'][0],
                    'wind_speed_min': min(hourly['wind_speed_10m']),
                    'wind_speed_mean': avg_wind,
                    'wind_speed_max': max(hourly['wind_speed_10m'])}]

            row_df = pd.DataFrame.from_dict(row)
            df = pd.concat([df, row_df])

        self.five_year_mean_temp = round(df['temperature_2m_mean'].mean(), 2)
        self.five_year_min_temp = df['temperature_2m_min'].min()
        self.five_year_max_temp = df['temperature_2m_max'].max()
        self.five_year_mean_wind = round(df['wind_speed_mean'].mean(), 2)
        self.five_year_min_wind = df['wind_speed_min'].min()
        self.five_year_max_wind = df['wind_speed_max'].max()
        self.five_year_sum_precip = df['precipitation_sum'].sum()
        self.five_year_min_precip = df['precipitation_sum'].min()
        self.five_year_max_precip = df['precipitation_sum'].max()

    # C2 method for mean temperature in Fahrenheit
    def get_mean_temp(self):
        return self.five_year_mean_temp

    # C2 method for maximum wind speed in miles per hour
    def get_max_wind(self):
        return self.five_year_max_wind

    # C2 method for precipitation sum in inches
    def get_precip_sum(self):
        return self.five_year_sum_precip

# C4 class
class Weather_DB:
    def __init__(self, weather_obj):
        self.lat = weather_obj.lat
        self.lon = weather_obj.lon
        self.month = weather_obj.month
        self.day = weather_obj.day
        self.year = weather_obj.year
        self.five_year_mean_temp = weather_obj.five_year_mean_temp
        self.five_year_min_temp = weather_obj.five_year_min_temp
        self.five_year_max_temp = weather_obj.five_year_max_temp
        self.five_year_mean_wind = weather_obj.five_year_mean_wind
        self.five_year_min_wind = weather_obj.five_year_min_wind
        self.five_year_max_wind = weather_obj.five_year_max_wind
        self.five_year_sum_precip = weather_obj.five_year_sum_precip
        self.five_year_min_precip = weather_obj.five_year_min_precip
        self.five_year_max_precip = weather_obj.five_year_max_precip

    # C6  method that queries the table created in SQLite and retrieves the data stored in part C5
    def get_sql(self):
        engine = sql.create_engine('sqlite:///weather.db')

        class Base(orm.DeclarativeBase):
            pass

        class Table(Base):
            __tablename__ = 'weather'

            id: orm.Mapped[int] = orm.mapped_column(sql.Integer, primary_key=True)
            location_latitude: orm.Mapped[float] = orm.mapped_column(sql.Float)
            location_longitude: orm.Mapped[float] = orm.mapped_column(sql.Float)
            month: orm.Mapped[int] = orm.mapped_column(sql.Integer)
            day_of_month: orm.Mapped[int] = orm.mapped_column(sql.Integer)
            year: orm.Mapped[int] = orm.mapped_column(sql.Integer)
            five_year_mean_temp: orm.Mapped[float] = orm.mapped_column(sql.Float)
            five_year_min_temp: orm.Mapped[float] = orm.mapped_column(sql.Float)
            five_year_max_temp: orm.Mapped[float] = orm.mapped_column(sql.Float)
            five_year_mean_wind: orm.Mapped[float] = orm.mapped_column(sql.Float)
            five_year_min_wind: orm.Mapped[float] = orm.mapped_column(sql.Float)
            five_year_max_wind: orm.Mapped[float] = orm.mapped_column(sql.Float)
            five_year_sum_precip: orm.Mapped[float] = orm.mapped_column(sql.Float)
            five_year_min_precip: orm.Mapped[float] = orm.mapped_column(sql.Float)
            five_year_max_precip: orm.Mapped[float] = orm.mapped_column(sql.Float)

        Base.metadata.create_all(engine)
        session = orm.Session(engine)

        with orm.Session(engine):
            session.add(Table(location_latitude=self.lat,
                              location_longitude=self.lon,
                              month=self.month,
                              day_of_month=self.day,
                              year=self.year,
                              five_year_mean_temp=self.five_year_mean_temp,
                              five_year_min_temp=self.five_year_min_temp,
                              five_year_max_temp=self.five_year_max_temp,
                              five_year_mean_wind=self.five_year_mean_wind,
                              five_year_min_wind=self.five_year_min_wind,
                              five_year_max_wind=self.five_year_max_wind,
                              five_year_sum_precip=self.five_year_sum_precip,
                              five_year_min_precip=self.five_year_min_precip,
                              five_year_max_precip=self.five_year_max_precip
                              ))
            session.commit()

        with orm.Session(engine) as session:
            rows = session.scalars(sql.select(Table)).all()

        print(tabulate([(t.id, t.location_latitude, t.location_longitude, t.month, t.day_of_month,
                         t.year, t.five_year_mean_temp, t.five_year_min_temp, t.five_year_max_temp,
                         t.five_year_mean_wind, t.five_year_min_wind, t.five_year_max_wind,
                         t.five_year_sum_precip, t.five_year_min_precip, t.five_year_max_precip) for t in rows],
                       headers=['id', 'location_latitude', 'location_longitude', 'month', 'day_of_month',
                                'year', 'five_year_mean_temp', 'five_year_min_temp', 'five_year_max_temp',
                                'five_year_mean_wind', 'five_year_min_wind', 'five_year_max_wind',
                                'five_year_sum_precip',
                                'five_year_min_precip', 'five_year_max_precip'],
                       tablefmt='simple'))
