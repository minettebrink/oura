
import matplotlib.pyplot as plt
import pandas as pd
import os

script_dir = os.path.dirname(__file__)

full_path_readiness = os.path.join(script_dir, '../data/oura/readiness.csv')
full_path_sleep = os.path.join(script_dir, '../data/oura/sleep.csv')
full_path_workouts = os.path.join(script_dir, '../data/oura/workouts.csv')
full_path_daily_activity = os.path.join(script_dir, '../data/oura/daily_activity.csv')
full_path_heart_rate = os.path.join(script_dir, '../data/oura/heart_rate.csv')
full_path_weather = os.path.join(script_dir, '../data/weather/weather.csv')

readiness = pd.read_csv(full_path_readiness)
sleep = pd.read_csv(full_path_sleep)
workouts = pd.read_csv(full_path_workouts)
daily_activity = pd.read_csv(full_path_daily_activity)
heart_rate = pd.read_csv(full_path_heart_rate)
weather = pd.read_csv(full_path_weather)


fig, ax = plt.subplots(7, 1)

# readiness and sleep score
ax[0].plot(readiness['summary_date'], readiness['score'], label = 'readiness score')
ax[0].plot(sleep['summary_date'], sleep['score'], label ='sleep score' )
ax[0].set_xlabel('date')
ax[0].set_ylabel('score')
ax[0].set_title('Readiness and sleep score')
ax[0].legend()
ax[0].tick_params(axis='x', labelrotation = 45)


# hrv and avrage hr
ax[1].plot(sleep['summary_date'], sleep['rmssd'], label = 'hrv')
ax[1].plot(sleep['summary_date'], sleep['hr_average'], label = 'hr avrage')
ax[1].set_xlabel('date')
ax[1].set_title('Heart rate variability and avrage heartrate')
ax[1].legend()
ax[1].tick_params(axis='x', labelrotation = 45)


# Percentage change in body and outdoor temperature
ax[2].plot(sleep['summary_date'], sleep['temperature_delta'], label = 'body')
ax[2].plot(weather['date'], weather['pct_temp'], label = 'outdoor')
ax[2].set_xlabel('date')
ax[2].set_ylabel('percentage change in temperature')
ax[2].set_title('Percentage change in body and outdoor temperature')
ax[2].tick_params(axis='x', labelrotation = 45)

# average heartrate and activitytime
ax[3].plot(sleep['summary_date'], sleep['hr_average'], label = 'sleeping hr avrage')
ax[3].plot(daily_activity['day'], daily_activity['medium_activity_time'], label = 'medium activity time')
ax[3].plot(daily_activity['day'], daily_activity['low_activity_time'], label = 'low activity time')
ax[3].plot(daily_activity['day'], daily_activity['high_activity_time'], label = 'high activity time')
ax[3].set_xlabel('date')
ax[3].set_ylabel('activity time')
ax[3].set_title('Heart rate and activitytime')
ax[3].legend()
ax[3].tick_params(axis='x', labelrotation = 45)

# Percentage change in outdoor temperatrure and heratrate
ax[4].plot(weather['date'], weather['pct_temp'], label = 'temperature')
ax[4].plot(heart_rate['timestamp'], heart_rate['pct_bpm'], label = 'bpm')
ax[4].set_xlabel('time')
ax[4].set_title('Percentage change in temperature and heartrate')
ax[4].legend()
ax[4].tick_params(axis = 'x', labelrotation = 45)

# steps and readiness score
ax[5].plot(daily_activity['day'], daily_activity['pct_steps'], label = 'steps')
ax[5].plot(readiness['summary_date'], readiness['pct_score'], label = 'readiness score')
ax[5].set_xlabel
ax[5].set_title('Steps and readiness score percentage difference ')
ax[5].legend()
ax[5].tick_params(axis = 'x', labelrotation = 45)

# calories burned during a workout and hrv
ax[6].plot(workouts['day'], workouts['calories'], label = 'calories')
ax[6].plot(sleep['summary_date'], sleep['rmssd'], label = 'hrv')
ax[6].set_xlabel
ax[6].set_title('Calories burned during a workout and hrv')
ax[6].legend()
ax[6].tick_params(axis = 'x', labelrotation = 45)

plt.show()


