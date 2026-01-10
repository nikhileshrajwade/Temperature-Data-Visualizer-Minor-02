import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read temperature data
df = pd.read_csv("Data.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

print("\nDaily Temperature Data:\n")
print(df.head())

# Set Date as index
df.set_index("Date", inplace=True)

# Calculate weekly and monthly averages
weekly_avg = df.resample("W").mean()
monthly_avg = df.resample("M").mean()

print("\nWeekly Average Temperature:\n", weekly_avg)
print("\nMonthly Average Temperature:\n", monthly_avg)

# Plot daily temperature variation
plt.figure(figsize=(15, 5))
plt.plot(df.index, df["Temperature"].values, marker = "o")
plt.title("Daily Temperature Variation")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.show()

# Plot weekly average temperature
plt.figure(figsize=(15, 5))
plt.plot(weekly_avg.index, weekly_avg["Temperature"].values, marker = "o")
plt.title("Weekly Average Temperature")
plt.xlabel("Week")
plt.ylabel("Average Temperature (°C)")
plt.show()

# Plot monthly average temperature
plt.figure(figsize=(15, 5))
plt.plot(monthly_avg.index, monthly_avg["Temperature"].values, marker = "o")
plt.title("Monthly Average Temperature")
plt.xlabel("Month")
plt.ylabel("Average Temperature (°C)")
plt.show()
