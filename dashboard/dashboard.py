import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
bike_day_df = pd.read_csv("https://raw.githubusercontent.com/azhararrozak/Submission-Proyek-Analisis-Data/main/dataset/day.csv")

# Set page title
st.title("Bike Sharing Data Dashboard")

# Display the first few rows of the dataset
st.subheader("Dataset Preview")
st.write(bike_day_df.head())

# Visualization: Bar plot for bike rentals based on weather situation
st.subheader("Bike Rentals Based on Weather Condition")
plt.figure(figsize=(8, 6))
sns.barplot(x="weathersit", y="cnt", data=bike_day_df, palette="viridis")
plt.xlabel("Weather Situation")
plt.ylabel("Total Bike Rentals")
plt.title("Total Bike Rentals Based on Weather Condition")
st.pyplot()

# Additional information
st.markdown("### Additional Information:")
st.markdown(
    "1. **Weather Situation Codes:**\n"
    "   - 1: Clear, Few clouds, Partly cloudy, Partly cloudy\n"
    "   - 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist\n"
    "   - 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds\n"
    "   - 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog"
)
