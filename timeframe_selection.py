## modules

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

october_data_path = './data/october_RAW.csv'
november_data_path = './data/november_RAW.csv'
raw_data = pd.read_csv(october_data_path, parse_dates=['UTC Date/Time'])


## select useful columns
raw_data = raw_data[[
    'UTC Date/Time',
    'CO2 (ppm) raw'
]]

raw_data['UTC Date/Time'] = raw_data['UTC Date/Time'].dt.tz_localize(None)

## 1: snapping (rounding) to nearest minute

rounded_data = raw_data.copy()

rounded_data['UTC Date/Time'] = rounded_data['UTC Date/Time'].dt.round(freq='min')
rounded_data.plot(x='UTC Date/Time', y='CO2 (ppm) raw')

start_date = pd.Timestamp(2025, 10, 16)
end_date = start_date + pd.Timedelta(days=2) # pd.Timestamp(2025, 10, 15)

date_mask = (rounded_data['UTC Date/Time'] >= start_date) & (rounded_data['UTC Date/Time'] <= end_date)

cut_data = rounded_data[date_mask]
# cut_data.plot(x='UTC Date/Time', y='CO2 (ppm) raw')

plt.show()