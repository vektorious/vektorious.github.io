def over_time(temp_data):
    if temp_data is None:
        raise ValueError("Please provide some data")

    import matplotlib.pyplot as plt
    import numpy as np
    import matplotlib.dates as mdates
    from matplotlib.dates import DateFormatter

    # Split data
    temp_data_morning = temp_data.query("hour < 12")
    temp_data_afternoon = temp_data.query("18 > hour > 12")
    temp_data_night = temp_data.query("hour > 18")

    # Create figure and plot space
    fig, ax = plt.subplots(2, 1,figsize=(18, 20))

    ##### First plot
    # Add x-axis and y-axis
    ax[0].plot(temp_data_morning.Date, temp_data_morning.Temp, color="midnightblue", label="Morning",linewidth=2, alpha=.7)
    ax[0].plot(temp_data_afternoon.Date, temp_data_afternoon.Temp, color="darkviolet", label="Afternoon", linewidth=2, alpha=.7)
    #ax.plot(temp_data_night.Date, temp_data_night.Temp, color="black", label="Night")

    # Set title and labels for axes
    ax[0].set(xlabel="",
           ylabel="Temperature [°C]",
           title="Temperature over Time")

    ax[0].yaxis.label.set_size(15)
    ax[0].title.set_size(20)


    # Always show the whole month
    datemin = np.datetime64(temp_data['Date'][0], 'M')
    datemax = np.datetime64(temp_data['Date'].iloc[-1], 'M') + np.timedelta64(1, 'M')
    ax[0].set_xlim(datemin, datemax)

    # Define the date format
    date_form = DateFormatter("%B")
    ax[0].xaxis.set_minor_formatter(date_form)
    ax[0].xaxis.set_minor_locator(mdates.MonthLocator(bymonthday=15))
    ax[0].xaxis.set_major_formatter(plt.NullFormatter())
    ax[0].xaxis.set_major_locator(mdates.MonthLocator())

    ax[0].yaxis.grid(True)
    ax[0].tick_params(axis='x', which='major', labelsize=20, direction='out', length=8, width=1, pad=15)
    ax[0].tick_params(axis='y', which='major', labelsize=15, direction='out', grid_alpha=0.5, length=0, width=0, pad=15)
    ax[0].tick_params(axis='both', which='minor', labelsize=15,  direction='out', length=0, width=0, pad=15)
    ax[0].legend(frameon=False, fontsize=15)


    ##### Second Plot
    ax[1].plot(temp_data_morning.Date, temp_data_morning.Temp, color="midnightblue", label="Morning", linewidth=2, alpha=.7)
    ax[1].plot(temp_data_afternoon.Date, temp_data_afternoon.Temp, color="darkviolet", label="Afternoon", linewidth=2, alpha=.7)

    # Set title and labels for axes
    ax[1].set(xlabel="",
           ylabel="Temperature [°C]",
           title="Temperature over the last 40 days")

    ax[1].yaxis.label.set_size(15)
    ax[1].title.set_size(20)


    # Sho the last 30 days
    datemin = np.datetime64(temp_data['Date'].iloc[-1], 'D') -np.timedelta64(40, 'D')
    datemax = np.datetime64(temp_data['Date'].iloc[-1], 'D')

    ax[1].set_xlim(datemin, datemax)

    av_temp = np.average(temp_data["Temp"][temp_data.Date >= datemin])
    ax[1].hlines(y=av_temp, xmin = datemin, xmax = datemax, linewidth=3, color='grey', label= "Average", linestyle ="--", alpha=.7)

    # Define the date format
    date_form_major = DateFormatter("%d. %B")
    date_form_minor = DateFormatter("%d.")

    ax[1].xaxis.set_minor_formatter(date_form_minor)
    ax[1].xaxis.set_minor_locator(mdates.DayLocator(interval=2))
    ax[1].xaxis.set_major_formatter(date_form_major)
    ax[1].xaxis.set_major_locator(mdates.MonthLocator())

    ax[1].yaxis.grid(True)
    ax[1].tick_params(axis='x', which='major', labelsize=15, direction='out', length=28, width=1, pad=15)
    ax[1].tick_params(axis='y', which='major', labelsize=15, direction='out', grid_alpha=0.5, length=0, width=0, pad=15)
    ax[1].tick_params(axis='y', which='minor', labelsize=15,  direction='out', length=0, width=0, pad=15)
    ax[1].tick_params(axis='x', which='minor', labelsize=15,  direction='out', length=4, width=1, pad=15)

    ax[1].legend(frameon=False, fontsize=15)

    #sns.boxplot(ax=ax[2],x=temp_data["month"], y=temp_data["Temp"], color="midnightblue")
    #ax[2].set(xlabel="",
    #       ylabel="Temperature [°C]",
    #       title="Monthly Temperature Range")


    #ax[2].yaxis.label.set_size(15)
    #ax[2].title.set_size(20)

    #ax[2].yaxis.grid(True)
    #ax[2].tick_params(axis='x', which='major', labelsize=15, direction='out', length=8, width=1, pad=15)
    #ax[2].tick_params(axis='y', which='major', labelsize=15, direction='out', grid_alpha=0.5, length=0, width=0, pad=15)
    #ax[2].tick_params(axis='both', which='minor', labelsize=15,  direction='out', length=0, width=0, pad=15)

    plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.9,
                    top=0.8,
                    wspace=0.4,
                    hspace=0.4)

    plt.savefig('temp_plot.png')
