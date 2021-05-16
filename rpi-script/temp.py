# libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter

temp_data = pd.read_csv("temp.log", header=None)
temp_data.columns = ("Date", "Temp")
temp_data["Date"] = pd.to_datetime(temp_data["Date"], format="%Y-%m-%d_%H:%M:%S")

# Split data
temp_data_morning = temp_data[temp_data['Date'].dt.hour < 11]
temp_data_afternoon = temp_data[temp_data['Date'].dt.hour > 12]

# Create figure and plot space
fig, ax = plt.subplots(1,figsize=(18, 6))

# Add x-axis and y-axis
ax.plot(temp_data_morning.Date, temp_data_morning.Temp, color="midnightblue", label="Morning")
ax.plot(temp_data_afternoon.Date, temp_data_afternoon.Temp, color="darkviolet", label="Afternoon")

# Set title and labels for axes
ax.set(xlabel="",
       ylabel="Temperature [°C]",
       title="Temperature over Time")

ax.yaxis.label.set_size(15)
ax.title.set_size(20)


# Always show the whole month
datemin = np.datetime64(temp_data['Date'][0], 'M')
datemax = np.datetime64(temp_data['Date'].iloc[-1], 'M') + np.timedelta64(1, 'M')
ax.set_xlim(datemin, datemax)

# Define the date format
date_form = DateFormatter("%B")
ax.xaxis.set_minor_formatter(date_form)
ax.xaxis.set_minor_locator(mdates.MonthLocator(bymonthday=15))
ax.xaxis.set_major_formatter(plt.NullFormatter())
ax.xaxis.set_major_locator(mdates.MonthLocator())

ax.yaxis.grid(True)
ax.tick_params(axis='x', which='major', labelsize=20, direction='out', length=8, width=1, pad=15)
ax.tick_params(axis='y', which='major', labelsize=15, direction='out', grid_alpha=0.5, length=0, width=0, pad=15)
ax.tick_params(axis='both', which='minor', labelsize=15,  direction='out', length=0, width=0, pad=15)
ax.legend(frameon=False)

plt.savefig('temp_plot.png')

print("successfully generated temperature plot")
