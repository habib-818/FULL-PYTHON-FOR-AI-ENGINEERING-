import requests
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime, timedelta

# Calculates Date
today = datetime.now()
week_ago = today - timedelta(days=7)


# Format dates for API  (YYYY-MM-DD)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")


# Get Paris weather for past wee
url = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_min,temperature_2m_max"

response = requests.get(url)
data = response.json()
print(data)
print("=" * 50)

## USEAGE OF PANDAS

# Extract the daily data
daily_time = data['daily']

# Create a DataFrame
df = pd.DataFrame({
    'date': daily_time['time'],
    'max_temp': daily_time['temperature_2m_max'],
    'min_temp': daily_time['temperature_2m_min']
})

# Convert Date strings to datetime
df['date'] = pd.to_datetime(df['date'])

print(df)
print("=" * 50)

## USEAGE OF MATPLOTLIB

# Create the plot
plt.figure(figsize=(10, 6))

plt.plot(
    df["date"],
    df["max_temp"],
    marker="o",
    label="Maximum Temperature"
)

plt.plot(
    df["date"],
    df["min_temp"],
    marker="o",
    label="Minimum Temperature"
)

plt.title("Paris Weather (Last 7 Days)")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")

plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("weather_chart.png")
plt.show()

print("Chart saved as 'weather_chart.png'")
print("=" * 50)



## SAVING USING CSV

# Create data folder if it doesnot exist
os.makedirs("data", exist_ok=True)

csv_path = "data/paris_weather.csv"

df.to_csv(csv_path, index=False)

print(f"Data successfully saved to '{csv_path}'")