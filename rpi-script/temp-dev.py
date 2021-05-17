# libraries
import matplotlib.pyplot as plt
#plt.style.use('seaborn-whitegrid')
import numpy as np
import pandas as pd
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
import seaborn as sns
from plotnine import ggplot, geom_bar, aes, geom_point

temp_data = pd.read_csv("temp.log", header=None)
temp_data.columns = ("Date", "Temp")
temp_data["Date"] = pd.to_datetime(temp_data["Date"], format="%Y-%m-%d_%H:%M:%S")

# Split data
temp_data_morning = temp_data[temp_data['Date'].dt.hour < 11]
temp_data_afternoon = temp_data[temp_data['Date'].dt.hour > 12]

temp_data["Date"].max()

monthly = pd.DataFrame(columns=['min_temp', 'max_temp', 'av_temp', 'month', 'year'])


years = np.unique(temp_data["Date"].dt.year)
for year in years:
    year_data = temp_data[temp_data["Date"].dt.year == year]
    year_months = year_data["Date"].dt.month

    months = np.unique(year_data["Date"].dt.month)
    for month in months:
        month_data = year_data[year_data["Date"].dt.month == month]
        min = month_data["Temp"].min()
        max = month_data["Temp"].max()
        av = np.average(month_data["Temp"])
        monthly = monthly.append({'min_temp': min, 'max_temp': max,
            'av_temp': av, 'month': month, 'year': year}, ignore_index=True)

print(monthly)

#ggplot(monthly, aes('month','max_temp')) + geom_point()

# Create figure and plot space
fig, ax = plt.subplots(1,figsize=(18, 6))

# Add x-axis and y-axis
#ax.plot("Date","Temp", data=temp_data)
ax.plot(temp_data_morning.Date, temp_data_morning.Temp, color="midnightblue", label="Morning")
ax.plot(temp_data_afternoon.Date, temp_data_afternoon.Temp, color="darkviolet", label="Afternoon")
# ax.plot(temp_data.Date, temp_data.Temp, color="black")

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
ax.legend(frameon=False, fontsize=15)

#ax[1].bar(monthly[0])
plt.savefig('temp_plot.png')


# Create figure and plot space
fig, ax = plt.subplots(1,figsize=(18, 6))

# Add x-axis and y-axis
#ax.plot("Date","Temp", data=temp_data)
ax.plot(temp_data_morning.Date, temp_data_morning.Temp, color="midnightblue", label="Morning", linewidth=3, alpha=.7)
ax.plot(temp_data_afternoon.Date, temp_data_afternoon.Temp, color="darkviolet", label="Afternoon", linewidth=3, alpha=.7)

# Set title and labels for axes
ax.set(xlabel="",
       ylabel="Temperature [°C]",
       title="Temperature over the last 40 days")

ax.yaxis.label.set_size(15)
ax.title.set_size(20)


# Sho the last 30 days
datemin = np.datetime64(temp_data['Date'].iloc[-1], 'D') -np.timedelta64(40, 'D')
datemax = np.datetime64(temp_data['Date'].iloc[-1], 'D')

ax.set_xlim(datemin, datemax)

av_temp = np.average(temp_data["Temp"][temp_data.Date >= datemin])
ax.hlines(y=av_temp, xmin = datemin, xmax = datemax, linewidth=3, color='grey', label= "Average", linestyle ="--", alpha=.7)

# Define the date format
date_form_major = DateFormatter("%d. %B")
date_form_minor = DateFormatter("%d")

ax.xaxis.set_minor_formatter(date_form_minor)
ax.xaxis.set_minor_locator(mdates.WeekdayLocator(interval=1))
ax.xaxis.set_major_formatter(date_form_major)
ax.xaxis.set_major_locator(mdates.MonthLocator())

ax.yaxis.grid(True)
ax.tick_params(axis='x', which='major', labelsize=20, direction='out', length=8, width=1, pad=15)
ax.tick_params(axis='y', which='major', labelsize=15, direction='out', grid_alpha=0.5, length=0, width=0, pad=15)
ax.tick_params(axis='y', which='minor', labelsize=15,  direction='out', length=0, width=0, pad=15)
ax.tick_params(axis='x', which='minor', labelsize=15,  direction='out', length=4, width=1, pad=15)

ax.legend(frameon=False, fontsize=15)

plt.savefig('temp_plot_recent.png')
