import pandas as pd
import numpy as np

from datetime import datetime, timedelta
from dateutils import relativedelta
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.dates as mdates

daytime = ('00:00', '20:00')

isabel_timestamps = [
    '10-27', '10-28', '11-17'
]
pablo_timestamps = [
    '10-29', '10-30', '11-18'
]
rishi_timestamps = [
    '11-05', '11-06', '11-21'
]
johanna_timestamps = [
    '11-12', '11-13', '11-13'
]

timestamps_ALL = np.stack([
    rishi_timestamps,
    isabel_timestamps,
    johanna_timestamps,
    pablo_timestamps
])

names = [
    'A: 1800', 'B: 1896', 'C: 2007', 'D: 2019'
]

scenarios = [
    'A', 'B', 'C'
]

cmap = mpl.colormaps['tab20b']

def zero_data(df):

    new_df = df.copy()
    # minutes = new_df['UTC Date/Time'].dt.minutes
    # hours = new_df['UTC Date/Time'].dt.hours
    # new_df['Time since Midnight'] = minutes + hours

    dates = new_df['UTC Date/Time']
    new_df['Time since Midnight'] = (dates - dates.min()).astype('timedelta64[s]').astype(int) / 3600

    return new_df.sort_values(by='Time since Midnight')

def get_data_period(df, ts_date):

    date = datetime.strptime(ts_date, r'%m-%d') + relativedelta(year=2025)

    new_data = df[(df['UTC Date/Time'] > date) & (df['UTC Date/Time'] < date + relativedelta(hours = 24))]

    return zero_data(new_data)

full_data = pd.read_csv('./data/processed_FULL.csv', parse_dates=['UTC Date/Time'])

day_data = get_data_period(full_data, '11-13')

plt.plot(day_data['Time since Midnight'], day_data['CO2 (ppm) raw'])
plt.show()