import pandas as pd
import os

script_dir = os.path.dirname(__file__)
full_path = os.path.join(script_dir, '../../data/weather/weather_raw.csv')
# print(full_path)

weather = pd.read_csv(full_path)

weather['date'] = pd.to_datetime(weather['time']).dt.date
weather['time'] = pd.to_datetime(weather['time']).dt.time 
weather.drop(columns = ['time'], inplace=True)

daily_weather = weather.groupby(['date']).mean().reset_index()
pct_temp = daily_weather['temp']
daily_weather['pct_temp'] = pct_temp
daily_weather['pct_temp'] = daily_weather['pct_temp'].pct_change()

daily_weather_path = os.path.join(script_dir, '../../data/weather/weather.csv')
daily_weather.to_csv(daily_weather_path, mode='a', index = False)
# daily_weather.to_csv(daily_weather_path, mode='a', index = False, header=False)

# print(daily_weather)