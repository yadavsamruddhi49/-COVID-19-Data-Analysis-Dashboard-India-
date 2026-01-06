


# STEP 1: Import Required Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# STEP 2: Load the Dataset

df = pd.read_csv(r"C:\Users\Samruddhi Yadav\Desktop\GitHub\Covid 19\covid19_india_data.csv")
df.head()

# STEP 3: Describes Dataset

df.describe()

# STEP 5: Convert Date Column

df["Date"] = pd.to_datetime(df["Date"])

# STEP 6: Total Cases by State

state_wise = df.groupby("State")[["Confirmed","Recovered","Deaths","Active"]].sum()
print(state_wise)

# STEP 7: Most Affected State

most_cases = state_wise.sort_values(by="Confirmed", ascending=False)
most_cases

# STEP 8: Recovery Rate Calculation

state_wise["Recovery_Rate (%)"] = (
    state_wise["Recovered"] / state_wise["Confirmed"]
) * 100

state_wise

# STEP 9: Death Rate Calculation

state_wise["Death_Rate (%)"] = (
    state_wise["Deaths"] / state_wise["Confirmed"]
) * 100

state_wise

## STEP 10 :  Visualizations : 

# Bar chart for confirmed cases by state

plt.figure()
plt.bar(state_wise.index, state_wise["Confirmed"])
plt.xticks(rotation=45)
plt.xlabel("State")
plt.ylabel("Confirmed Cases")
plt.title("Confirmed COVID-19 Cases by State")
plt.show()

# Active Cases Trend (Line Chart)

date_wise = df.groupby("Date")["Active"].sum()

plt.figure()
plt.plot(date_wise.index, date_wise.values)
plt.xlabel("Date")
plt.ylabel("Active Cases")
plt.title("Active COVID-19 Cases Over Time")
plt.show()

# Recovered vs Deaths (Bar Chart)

plt.figure()
plt.bar(state_wise.index, state_wise["Recovered"], label="Recovered")
plt.bar(state_wise.index, state_wise["Deaths"], bottom=state_wise["Recovered"], label="Deaths")
plt.xticks(rotation=45)
plt.legend()
plt.title("Recovered vs Deaths by State")
plt.show()

# STEP 11 : Key Insights (Write in Notebook / Report)

print("Most affected state:", most_cases.index[0])
print("Highest recovery rate:", state_wise["Recovery_Rate (%)"].idxmax())
print("Lowest death rate:", state_wise["Death_Rate (%)"].idxmin())

