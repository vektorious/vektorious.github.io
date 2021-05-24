# libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
from temp_fun import over_time

temp_data = pd.read_csv("temp.log", header=None)
temp_data.columns = ("Date", "Temp")
temp_data["Date"] = pd.to_datetime(temp_data["Date"], format="%Y-%m-%d_%H:%M:%S")
temp_data["hour"] = temp_data['Date'].dt.hour
temp_data["month"] = temp_data['Date'].dt.month_name()

over_time(temp_data)

plt.savefig('temp_plot.png')

print("successfully generated temperature plot")
