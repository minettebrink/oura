from numpy import source
import pandas as pd
import requests  
import json
import os

from sympy import expand







def get_data(url, params): #function to get data from api with different url and time
    headers = { 
    'Authorization': 'Bearer OURA_TOKEN' 
    }
    response = requests.request('GET', url, headers=headers, params=params)
    response = json.loads(response.text) #för att få text fil till dictonary 
    return response


def data_frame(x): #to get the data to a data frame
    value = x['data'] 
    df = pd.DataFrame.from_dict(value)
    return df

def sleep_data_frame(x): #to get the data to a data frame
    value = x['sleep'] 
    df = pd.DataFrame.from_dict(value)
    return df

def readiness_data_frame(x): #to get the data to a data frame
    value = x['readiness'] 
    df = pd.DataFrame.from_dict(value)
    return df

def main():
    script_dir = os.path.dirname(__file__)

    sleep = sleep_data_frame(get_data('https://api.ouraring.com/v1/sleep?start=2021-08-28&end=2022-03-15', 
                         {'start_datetime': '2021-08-28', 'end_datetime': '2022-03-15'}))
    sleep[['bedtime_end','extra']] = sleep.bedtime_end.str.split("+",expand=True,)
    sleep[['bedtime_start','extra1']] = sleep.bedtime_start.str.split("+",expand=True,)
    sleep.drop(columns= ['timezone', 'rmssd_5min','hypnogram_5min', 'score_latency','score_disturbances', 'score_alignment', 
                        'score_efficiency', 'score_deep', 'score_rem', 'score_total', 'hr_5min', 'period_id', 'extra', 'extra1', 
                        'is_longest', 'midpoint_at_delta', 'breath_average', 'midpoint_time', 
                        'temperature_trend_deviation', 'temperature_deviation'], inplace=True)
    pct_hr_avrage = sleep['hr_average']
    sleep['pct_hr_avrage'] = pct_hr_avrage
    sleep['pct_hr_avrage'] = sleep['pct_hr_avrage'].pct_change()
    sleep_path = os.path.join(script_dir, '../../data/oura/sleep.csv') 
    # print(sleep)
   

    readiness = readiness_data_frame(get_data('https://api.ouraring.com/v1/readiness?start=2021-08-28&end=2022-03-15', 
                         {'start_datetime': '2021-08-28', 'end_datetime': '2022-03-15'}))
    readiness.drop(columns= ['period_id', 'rest_mode_state', 'score_resting_hr', 'score_sleep_balance',
                            'score_temperature', 'rest_mode_state', 'score_hrv_balance', 'score_activity_balance',
                            'score_previous_night', 'score_previous_night','score_recovery_index', 'score_previous_day'], inplace=True) 
    pct_score = readiness['score']
    readiness['pct_score'] = pct_score
    readiness['pct_score'] = readiness['pct_score'].pct_change()
    readiness_path = os.path.join(script_dir, '../../data/oura/readiness.csv')
    # print(readiness)
    
    


    heart_rate = data_frame(get_data('https://api.ouraring.com/v2/usercollection/heartrate', 
                        params={ 'start_datetime': '2022-03-02T00:00:00-08:00', 'end_datetime': '2022-3-15T00:00:00-08:00'}))
    heart_rate[['timestamp','Extra']] = heart_rate.timestamp.str.split('+',expand=True,)
    heart_rate[['timestamp','Extra1']] = heart_rate.timestamp.str.split('.',expand=True,)
    heart_rate[['timestamp', 'hour']] = heart_rate.timestamp.str.split('T', expand = True)
    heart_rate.drop(columns = ['Extra', 'Extra1','source', 'hour'], inplace = True)
    hert_rate_path = os.path.join(script_dir, '../../data/oura/heart_rate_raw.csv')
    # print(heartrate)
    

    workouts= data_frame(get_data('https://api.ouraring.com/v2/usercollection/workout',
                        {'start_date': '2021-08-28', 'end_date': '2022-03-15'})) 
    workouts.dropna(subset = ['calories'], inplace=True) 
    workouts.reset_index(inplace=True)
    workouts.drop(columns=['start_datetime', 'end_datetime', 'source', 'label', 'index'], inplace=True)
    workouts_path = os.path.join(script_dir, '../../data/oura/workouts.csv')
    # print(workouts)


    daily_activity= data_frame(get_data('https://api.ouraring.com/v2/usercollection/daily_activity', 
                        {'start_date': '2021-08-28', 'end_date': '2022-03-15'}))
    daily_activity.dropna(subset = ['score'], inplace=True)
    daily_activity.reset_index(inplace=True) 
    daily_activity[['timestamp','Extra']] = daily_activity.timestamp.str.split("+",expand=True,)
    daily_activity.drop(columns= ['Extra','class_5_min', 'index','sedentary_met_minutes', 'average_met_minutes', 'contributors', 
                                    'target_meters', 'sedentary_time', 'non_wear_time', 'met', 'meters_to_target', 
                                    'low_activity_met_minutes', 'inactivity_alerts', 'high_activity_met_minutes', 
                                    'medium_activity_met_minutes','equivalent_walking_distance', 'target_calories' ], inplace=True)
    sum_column = daily_activity['high_activity_time'] + daily_activity['low_activity_time']+daily_activity['medium_activity_time']
    daily_activity['activity_time'] = sum_column
    pct_activitytime = daily_activity['activity_time']
    daily_activity['pct_activitytime'] = pct_activitytime
    daily_activity['pct_activitytime'] = daily_activity['pct_activitytime'].pct_change()
    pct_steps = daily_activity['steps']
    daily_activity['pct_steps'] = pct_steps
    daily_activity['pct_steps'] = daily_activity['pct_steps'].pct_change()
    daily_activity_path = os.path.join(script_dir, '../../data/oura/daily_activity.csv')
    
    # print(daily_activity)
    
    sleep.to_csv(sleep_path, mode='a', index = False)
    # daily_activity.to_csv(daily_activity_path, mode='a', index = False)
    # workouts.to_csv(workouts_path, index = False)
    # heart_rate.to_csv(hert_rate_path, mode='a', index = False)
    # readiness.to_csv(readiness_path, mode='a', index = False)

    # sleep.to_csv(sleep_path, mode='a', index = False, header=False)
    # daily_activity.to_csv(daily_activity_path, mode='a', index = False, header=False)
    # workouts.to_csv(workouts_path, mode='a', index = False, header=False)
    # heart_rate.to_csv(hert_rate_path, mode='a', index = False, header=False)
    # readiness.to_csv(readiness_path, mode='a', index = False, header=False)


if __name__ == '__main__':  
    main()