import numpy as np
import pandas as pd


data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 
print("-----------------") 
print(df.loc[['day1', 'day2']])


