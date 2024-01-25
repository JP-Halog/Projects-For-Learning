import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import date2num, num2date, DateFormatter, AutoDateLocator

# Assuming df is your DataFrame and it has been loaded with your data
df['ttb_dateReported'] = pd.to_datetime(df['ttb_dateReported'])
df = df.sort_values('ttb_dateReported')

plt.figure(figsize=(15, 10))  # Adjust the size of the figure

y_positions = {}

for index, row in df.iterrows():
    # Collect events and their dates
    events = ['td_dateOpened', 'td_dateClosed', 'td_dateLastActive', 'td_dateLastPayment', 'td_dateMajorDelinquency']
    dates = [date2num(row[event]) if pd.notnull(row[event]) else None for event in events]
    events += [column for column in df.columns if column.startswith('NC_') and row[column]]
    dates += [date2num(row['ttb_dateReported']) if pd.notnull(row['ttb_dateReported']) else None for _ in range(len(events) - len(dates))]

    # Remove None dates and corresponding events
    events, dates = zip(*[(event, date) for event, date in zip(events, dates) if date is not None])

    # Convert tuples to lists
    events = list(events)
    dates = list(dates)

    # Sort events by date
    events = [x for _, x in sorted(zip(dates, events))]
    dates.sort()

    # Plot events
    plt.plot(dates, [1]*len(dates), '-o')

    # Add labels
    for i, event in enumerate(events):
        if dates[i] in y_positions:
            y_positions[dates[i]] += 0.05
        else:
            y_positions[dates[i]] = 1
        plt.text(dates[i], y_positions[dates[i]], event, rotation=45)  # Rotate labels 45 degrees

plt.xlabel('ttb_dateReported')
plt.ylabel('Events')

# Set the x-ticks to be the dates corresponding to the plotted dots
plt.xticks(dates, [num2date(date).strftime('%Y-%m-%d') for date in dates], rotation=45)

plt.ylim(0, max(y_positions.values()) + 0.05)  # Set the limits of the y-axis

plt.show()