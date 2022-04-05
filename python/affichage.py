#!/usr/bin/env python3
# coding=utf8

import requests
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

data = requests.get('http://localhost:8080/getAudits').json()
df = pd.json_normalize(data)
print(df)

print('shows a user name ... ')
user = input()





filtred_df = df[df['user'] == user]
plt.plot(filtred_df['createdon'], filtred_df['cpu'], color='green', label='CPU')
plt.plot(filtred_df['createdon'], filtred_df['memory'], color='blue', label='memory')
plt.plot(filtred_df['createdon'], filtred_df['storage'], color='yellow', label='storage')

# plot thresholds
settings = requests.get('http://localhost:8080/getSettings').json()[0]
df_settings = pd.json_normalize(settings)
plt.axhline(y=settings['threshold_storage'], linewidth=1, color='red', label='storage threshold')
plt.axhline(y=settings['threshold_memory'], linewidth=1, color='red', label='memory threshold')
plt.axhline(y=settings['threshold_cpu'], linewidth=1, color='#800000', label='cpu threshold')

plt.legend()
plt.show()
