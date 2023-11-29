import streamlit as st
import pandas as pd

# Load data
bike_day_df = pd.read_csv("https://raw.githubusercontent.com/azhararrozak/Submission-Proyek-Analisis-Data/main/dataset/day.csv")

# Set page title
st.title("Bike Sharing Data Dashboard")

# Display the dataset
st.subheader("Dataset Preview")
st.dataframe(bike_day_df.head())

# Summary statistics
st.subheader("Summary Statistics")
st.write(bike_day_df.describe())

# Line chart for temperature and total rentals
st.subheader("Line Chart: Temperature vs Total Rentals")
st.line_chart(bike_day_df[['temp', 'cnt']])

# Bar chart for season-wise rentals
st.subheader("Bar Chart: Season-wise Rentals")
season_counts = bike_day_df['season'].value_counts()
st.bar_chart(season_counts)

# Scatter plot for temperature and total rentals
st.subheader("Scatter Plot: Temperature vs Total Rentals")
st.scatter_chart(bike_day_df[['temp', 'cnt']])

# Histogram of total rentals
st.subheader("Histogram: Total Rentals Distribution")
st.hist(bike_day_df['cnt'], bins=30, edgecolor='black')
st.xlabel("Total Rentals")
st.ylabel("Frequency")

# Show the dashboard
st.show()
