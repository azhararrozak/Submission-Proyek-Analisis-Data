import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
bike_day_df = pd.read_csv("https://raw.githubusercontent.com/azhararrozak/Submission-Proyek-Analisis-Data/main/dataset/day.csv")
bike_day_df.head()

sns.set_style('darkgrid')

# Set title
st.title("Bike Sharing Data Dashboard")

# Wheather rent bike
def condition_weather_rent_df(df):
    weather_condition = df.groupby(by='weathersit').agg({'cnt': 'sum'})
    return weather_condition

min_date = pd.to_datetime(bike_day_df['dteday']).dt.date.min()
max_date = pd.to_datetime(bike_day_df['dteday']).dt.date.max

start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value= min_date,
        max_value= max_date,
        value=[min_date, max_date]
    )


main_df = bike_day_df[(bike_day_df['dteday'] >= str(start_date)) & 
                (bike_day_df['dateday'] <= str(end_date))]

weather_rent_df = condition_weather_rent_df(main_df)

# Dashboard
# Membuah jumlah penyewaan berdasarkan kondisi cuaca
st.subheader('Weatherly Rentals')

fig, ax = plt.subplots(figsize=(16, 8))

colors=["tab:blue", "tab:orange", "tab:green"]

sns.barplot(
    x=weather_rent_df.index,
    y=weather_rent_df['cnt'],
    palette=colors,
    ax=ax
)

for index, row in enumerate(weather_rent_df['cnt']):
    ax.text(index, row + 1, str(row), ha='center', va='bottom', fontsize=12)

ax.set_xlabel(None)
ax.set_ylabel(None)
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=15)
st.pyplot(fig)

"""
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
st.show()"""
