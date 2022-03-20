import streamlit as st
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



st.write("# Minettes Oura")

st.write("""
On this app, I'm showing analysis from my Oura ring data. It is just to showcase my skills to work with 
datasets and analyze data. If you have an Oura ring, you can get almost all the information I've studied 
from the app. You can find the code on my Github to see how I've done this. Enjoy!
""")

st.write("## Different graphs")
st.write("""
I'm going to present different graphs below. Some have more exciting results than others, 
and some conclusions can be drawn in some cases. This is the first version, 
and I plan to do some tweaks, but it is up and running now. 
""")
st.write("### Readiness and sleep score")
st.write("""
I started by comparing my readiness and sleep score. It was relatively easy for me to imagine how 
the chart would look because the Oura app has good graphics. So, I could focus more on the coding and 
look at the chart and see if something had gone wrong. 
""")

sleep_and_readiness_score = pd.concat([sleep['summary_date'], sleep['score'], readiness['score']], axis = 1)
sleep_new = sleep.rename(columns={'score':'sleep score'})
readiness_new = readiness.rename(columns={'score': 'readiness score'})
sleep_and_readiness_score = pd.concat([sleep_new['summary_date'], sleep_new['sleep score'], readiness_new['readiness score']], axis = 1)
# sleep_and_readiness_score = sleep_and_readiness_score.set_index('summary_date')
sleep_and_readiness = pd.DataFrame(sleep_and_readiness_score[:198], columns=['sleep score', 'readiness score'])
st.line_chart(sleep_and_readiness)

st.write("""
My sleep score and readiness score mostly follow the same pattern, but there are some exceptions. 
In the beginning, my readiness score was a bit higher than my sleep score, which doesn't happen later on. 
This can be because my Oura was new and hadn't yet gotten a pattern over my sleeping habits. My readiness 
score has dipped in two periods, but my sleep score is higher. The dips have happened because I've been 
stressed, overtrained, or sick. When both my sleep and readiness score has dipped, it's because I've been 
to a party or dinner and drank some wine, and I stayed up late. On the other hand, when both scores are 
high, I live a well-balanced life. 
""")

st.write("### Heart rate variability and avrage heartrate")

st.write("""
Heart rate and hrv are good ways to see if you recovered well. Both heart rate and the heart rate 
variability (hrv) are tracked from my sleep, and each observation is an average number from observations 
during the night. The lower your heart rate is and the higher your hrv is, the better you have recovered. 
I must point out that there is no point in staring at one observation but instead looking at the trend. 
If your heart rate is higher and hrv lower than usual for several weeks, you should reflect on your 
everyday habits (exercise, stress, amount of rest, eating habits, etc.). However, the most important thing 
is listening to your body and reacting to that. If your body feels good and energetic, you are good to go 
even though your heart rate and hrv say otherwise. 
""")

sleep1 = sleep.rename(columns={'hr_average':'heart rate'})
sleep1 = sleep1.rename(columns={'rmssd':'heart rate variability'})
hr_and_hrv = pd.DataFrame(sleep1[:180], columns=['heart rate', 'heart rate variability'])
st.line_chart(hr_and_hrv)

st.write("""
You can observe that when my heart rate is low, my hrv is high, and vice versa. From index 54 to 133, 
my heart rate is higher, and my hrv is lower due to stress. During this time, I finished my master thesis 
and tried to find a good balance between recovery and exercises after long-covid. During this time, I felt 
that my body was stressed. I felt my heart rate pounding, a bit harder to focus, and when my muscles 
relaxed, I could feel minor spasms in them. During the rest of the time that I have observed, I have felt 
energetic and have had a good balance between exercise, work, and rest. There are also small dips in my 
hrv and peeks in heart rate, but that is usually due to intense exercise, or I have drunk a glass of wine 
in the evening. 
""")

st.write("### Percentage change in body and outdoor temperature")

st.write("""
I drew this chart to compare the percentage change in my body temperature and the temperature outdoors in 
this chart. The data has only 13 observations, so it is too small to conclude anything. As an intuitive 
thought, I would say that they are independent of each other, but we will see if I can come to any 
conclusions when I gather more data. Even though, I thought it would be interesting to see if there is a 
similar pattern because I sleep better when it is a cooler temperature outside. After all, my apartment 
is quite drafty, so the outdoor temperature affects my apartment's temperature.
""")

sleep2 = sleep.rename(columns= {'temperature_delta':'body temperature'})
weather1 = weather.rename(columns={'temp':'outdoor temperature'})
body_and_outdoor_temp = pd.concat([weather1['date'], sleep2['body temperature'], weather1['outdoor temperature']], axis = 1)
body_and_outdoor_temp_df = pd.DataFrame(body_and_outdoor_temp[:14], columns = ['body temperature', 'outdoor temperature'])
st.line_chart(body_and_outdoor_temp_df)



st.write("### Percentage change in heart rate and activitytime")

st.write("""
In this chart, I've decided to depict the percentage change in my nightly average heart rate 
and the percentage change in my activity time during the day. But first, I started with comparing absolute 
values, which made the chart messy, and it was hard to compare the two different observations. The 
activity time consists of three different types of activity, low, medium, and high activity. I thought 
it might be interesting to compare these to my heart rate, but it had the same result when comparing 
absolute values. It was too messy to read. So, then I decided to compare percentage change which made the 
chart much easier to read. 
""")

sleep3 = sleep.rename(columns= {'pct_hr_avrage':'heart rate'})
daily_activity1 = daily_activity.rename(columns={'pct_activitytime':'activity time'})
sleep_and_activity = pd.concat([daily_activity1['day'], sleep3['heart rate'], daily_activity1['activity time']], axis = 1)
sleep_and_activity_df = pd.DataFrame(sleep_and_activity[:189], columns=['heart rate', 'activity time'])
st.line_chart(sleep_and_activity_df)

st.write("""
My activity time is changing almost every day, one day, it's high, and the next, it is low. This is 
natural because I usually feel more tired after an active day. I want to note that the changes in the 
chart might look big, but a 1 % change is not much in absolute values. My heart rate is lower when my 
activity has decreased the day before. On the other hand, if I had had an active day before, my heart rate 
would have increased. 
""")

st.write("### Percentage change in outdoor temperature and heartrate")

st.write("""
I've got the same problem as before when using temperature data back in this chart. I don't have enough 
observations to draw any conclusions. It might be that I can't conclude anything from this chart because 
there are so many factors contributing to my heart rate more than just the outdoor temperature. But it 
will be interesting to see when I have more data if there are any trends. 
""")

weather1 = weather.rename(columns={'pct_temp': 'temperature'})
heart_rate1 = heart_rate.rename(columns= {'pct_bpm':'heart rate'})
temperature_and_heartrate = pd.concat([weather1['date'], weather1['temperature'], heart_rate1['heart rate']], axis = 1)
temperature_and_heartrate_df = pd.DataFrame(temperature_and_heartrate[1:11],columns=['temperature', 'heart rate'])
st.line_chart(temperature_and_heartrate_df)

st.write("### Percentage difference steps and readiness score percentage difference")

st.write("""
In this chart, my percentage difference in steps varies much more than the change in my score. 
There is a trend between these two, and they follow the same pattern. When I have walked a lot during the 
day, my readiness score is also higher. The comparison number in the steps is 13 166, and my readiness 
score is 85 out of 100. 
""")

daily_activity1 = daily_activity.rename(columns={'pct_steps': 'percentage difference in steps'})
readiness1 = readiness.rename(columns= {'pct_score':'percentage difference in score'})
steps_and_readiness_score = pd.concat([readiness1['summary_date'], daily_activity1['percentage difference in steps'], readiness1['percentage difference in score']], axis = 1)
steps_and_readiness_score_df = pd.DataFrame(steps_and_readiness_score[1:180], columns=['percentage difference in steps', 'percentage difference in score'])
st.line_chart(steps_and_readiness_score_df)

st.write("### Calories burned during a workout and hrv")

st.write("""
I've compared calories burned during a workout and my average hrv during sleep. I can assume that the 
more calories I've burned during an exercise, the heavier it has been for my body. Therefore I can believe 
that it would affect my hrv when sleeping. Hrv is affected by many different factors, so it may not always 
be the case that I've burned many calories during a workout and have lower hrv and vice versa. 
""")

sleep1 = sleep.rename(columns={'rmssd': 'heart rate variability'})
hrv_and_calories = pd.concat([sleep1['summary_date'], sleep1['heart rate variability'], workouts['calories']], axis = 1)
hrv_and_calories_df = pd.DataFrame(hrv_and_calories[:200], columns=['calories', 'heart rate variability'])
st.line_chart(hrv_and_calories_df)

st.write("""
There are some trends in my chart. My hrv and how many calories have burned follow the same direction 
in some cases. If I've burned many calories, my hrv is lower and vice versa.
""")