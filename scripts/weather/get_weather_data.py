from urllib import response
import requests
import pandas as pd
import json
from datetime import datetime
import datetime
import calendar
import os




def old_data(url_old):
    response = requests.request('GET', url_old)
    info, hourly = response.text.split('hourly')
    return json.loads(response.text)

def get_url(url):
    date = datetime.datetime.utcnow()
    dt = calendar.timegm(date.utctimetuple())
    response = requests.request('GET', url.format(dt))
    info, hourly = response.text.split('hourly')
    return json.loads(response.text)
    

def main():
    script_dir = os.path.dirname(__file__)
    # res = get_url('https://api.openweathermap.org/data/2.5/onecall/timemachine?lat=60.192059&lon=24.945831&dt={}&appid=OPEN_WEATHER_TOKEN')
    res = old_data('https://api.openweathermap.org/data/2.5/onecall/timemachine?lat=60.192059&lon=24.945831&dt=1647381604&appid=OPEN_WEATHER_TOKEN')

    time = []
    temp = []
    feels_like = []
    pressure = []
   
    for i in res['hourly']:
        time.append(i['dt'])
        temp.append(i['temp'])
        feels_like.append(i['feels_like'])
        pressure.append(i['pressure'])
       
    df = zip(time, temp, feels_like, pressure)
    df = pd.DataFrame(df)
    
    weather = df.rename(columns={0: 'time', 1 : 'temp', 2: 'feels_like', 3: 'pressure'})
    weather['temp'] = weather['temp'] - 273.5
    weather['feels_like'] = weather['feels_like'] - 273.5
    weather['time'] = pd.to_datetime(weather['time'],unit='s')
    
    
    weather_path = os.path.join(script_dir, '../../data/weather/weather_raw.csv')
    weather.to_csv(weather_path, mode='a', index = False, header=False)
   



if __name__ == '__main__':  
    main()