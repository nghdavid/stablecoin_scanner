import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter
# Load data
file_path = 'output.csv'
data = pd.read_csv(file_path)

def human_readable_format(x, pos):
    if x >= 1e8:
        return f'{x/1e8:.1f}'  # Convert to 億
    elif x >= 1e6:
        return f'{x/1e6:.1f}M'  # Convert to millions
    elif x >= 1e3:
        return f'{x/1e3:.1f}K'  # Convert to thousands
    return str(x)

# Convert to datetime
data['created_time'] = pd.to_datetime(data['created_time'])

# Resample data to 1-hour intervals
hourly_data = data.set_index('created_time').resample('1H').mean().reset_index()

# Plotting
plt.figure(figsize=(24, 12))
plt.plot(hourly_data['created_time'], hourly_data['balance'], marker='o', linestyle='-')
plt.title('Stablecoin Balance Over Time (1-hour intervals)')
plt.xlabel('Time')
plt.ylabel('Balance')
plt.grid(True)
plt.xticks(rotation=45)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=6))  # Display a tick every hour
plt.gca().yaxis.set_major_formatter(FuncFormatter(human_readable_format))
plt.tight_layout()  # Adjusts the plot to ensure everything fits without overlapping

# Save or display the plot
plt.savefig('stablecoin_balance_1hr_intervals.png')
plt.show()
