import pandas as pd
import os

script_dir = os.path.dirname(__file__)
full_path = os.path.join(script_dir, '../../data/oura/heart_rate_raw.csv')
print(full_path)

heart = pd.read_csv(full_path)

# print(heart)

heart_rate = heart.groupby(['timestamp']).mean().reset_index()
pct_bpm = heart_rate['bpm']
heart_rate['pct_bpm'] = pct_bpm
heart_rate['pct_bpm'] = heart_rate['pct_bpm'].pct_change()
# print(heart_rate)


hear_rate_path = os.path.join(script_dir, '../../data/oura/heart_rate.csv')
# print(hear_rate_path)

heart_rate.to_csv(hear_rate_path, mode='a', index = False)

# heart_rate.to_csv(hear_rate_path, mode='a', index = False, header=False)

