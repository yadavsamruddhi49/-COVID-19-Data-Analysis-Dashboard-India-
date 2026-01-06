# -COVID-19-Data-Analysis-Dashboard-India-

📌 Project Overview

This project analyzes COVID-19 data for major Indian states to understand the spread, recovery, and impact of the pandemic using Python.
The goal is to perform Exploratory Data Analysis (EDA) and visualize trends to extract meaningful insights.

🎯 Objectives

Analyze state-wise COVID-19 confirmed cases

Study month-wise growth of cases

Calculate recovery and death rates

Identify most affected states

Visualize trends using graphs

📁 Dataset

File name: covid19_india_data.csv

Source: Sample educational dataset (India-based)

Columns:

Date

State

Confirmed

Recovered

Deaths

Active

🛠️ Tools & Technologies

Python

Pandas

Matplotlib

Jupyter Notebook / VS Code

🔍 Project Workflow

Data Loading

Data Cleaning

Exploratory Data Analysis (EDA)

Aggregation using GroupBy

Data Visualization

Insight Generation

📊 Key Analysis Performed

Total confirmed cases by state

Month-wise COVID-19 growth

Recovery rate calculation

Death rate comparison

State-wise impact analysis

📈 Sample Visualizations

Bar chart of confirmed cases by state

Line chart showing month-wise case growth

🧠 Insights

Maharashtra reported the highest number of confirmed cases

COVID-19 cases increased significantly over months

Recovery rate varied across states

Death rate remained comparatively lower than recovery rate

▶️ How to Run the Project
pip install pandas matplotlib

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("covid19_india_data.csv")
df.head()

📂 Repository Structure
├── covid19_india_data.csv
├── covid_analysis.py / notebook.ipynb
├── README.md

🚀 Future Enhancements

Add real-time COVID data

Create an interactive Streamlit dashboard

Add more states and timeline

Use Seaborn for advanced visualization

👤 Author
Samruddhi Yadav
📊 Aspiring Data Analyst
💡 Skills: Python | Pandas | Data Visualization | ED


