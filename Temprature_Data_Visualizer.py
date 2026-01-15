import pandas as pd
import matplotlib.pyplot as plt

<<<<<<< HEAD

# LOAD DATA
=======
# 1. LOAD DATA

>>>>>>> ae56dd79f7d21473507de1e86fa0e1f6ba44b203
df = pd.read_csv("Temperature Avg.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

print("\nRaw Climate Data:\n")
print(df.head())

# FILTER DATA FOR ONE CITY

cities = ['Ahmedabad', 'Bengaluru', 'Bhopal', 'Chennai', 'Delhi', 'Hyderabad', 'Jaipur', 'Kolkata', 'Lucknow', 'Mumbai']
city = input(f""" Enter a City from the Below List:
{cities}: """)
if city == "" or city not in cities:
    print("!!! INVALID ENTRY !!!")
    exit()

city_name = city
city_df = df[df["City"] == city_name].copy()

# Set Date as index
city_df.set_index("Date", inplace=True)

# DAILY, WEEKLY, MONTHLY AVERAGES
<<<<<<< HEAD
=======

>>>>>>> ae56dd79f7d21473507de1e86fa0e1f6ba44b203
daily_temp = city_df["Temperature_Avg (°C)"]

weekly_avg = daily_temp.resample("W").mean()
monthly_avg = daily_temp.resample("M").mean()

print("\nWeekly Average Temperature:\n", weekly_avg.head())
print("\nMonthly Average Temperature:\n", monthly_avg.head())

<<<<<<< HEAD
# PLOTTING USING SUBPLOTS (ALL AT ONCE)
=======
#PLOTTING

>>>>>>> ae56dd79f7d21473507de1e86fa0e1f6ba44b203
plt.figure(figsize=(14, 10))
plt.suptitle(
    f"Temperature Analysis for {city_name}",
    fontsize=16,
    fontweight="bold"
)

# ---------------- Daily Temperature ----------------
plt.subplot(2, 2, 1)
plt.plot(daily_temp.index, daily_temp.values)
plt.title("Daily Average Temperature")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")

# ---------------- Weekly Average ----------------
plt.subplot(2, 2, 2)
plt.plot(weekly_avg.index, weekly_avg.values, marker="o")
plt.title("Weekly Average Temperature")
plt.xlabel("Week")
plt.ylabel("Temperature (°C)")

# ---------------- Monthly Average ----------------
plt.subplot(2, 2, 3)
plt.plot(monthly_avg.index, monthly_avg.values, marker="o")
plt.title("Monthly Average Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")

# Daily temperature range (Max - Min)
daily_range = (
    city_df["Temperature_Max (°C)"] -
    city_df["Temperature_Min (°C)"]
)
plt.subplot(2, 2, 4)
plt.plot(daily_range.index, daily_range.values, color="orange")
plt.title("Daily Temperature Range (Max − Min)")
plt.xlabel("Date")
plt.ylabel("Range (°C)")
plt.tight_layout()
plt.show()
