import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
bike_day_df = pd.read_csv("https://raw.githubusercontent.com/azhararrozak/Submission-Proyek-Analisis-Data/main/dataset/day.csv")

# Judul Dashboard
st.title("Dashboard: Analisis Data Peminjaman Sepeda")

# Menampilkan Dataset
st.subheader("Dataset Preview")
st.write(bike_day_df.head())

# Visualisasi Peminjaman sepeda berdasarkan cuaca
st.subheader("Bike Rentals Based on Weather Condition")
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x="weathersit", y="cnt", data=bike_day_df, palette="viridis", ax=ax)
plt.xlabel("Kondisi Cuaca")
plt.ylabel("Jumlah Pengguna Sepeda")
plt.title("Jumlah Pengguna Sepeda Berdasarkan Kondisi Cuaca")
st.pyplot(fig)

# Tambahan Informasi
st.markdown("### Additional Information:")
st.markdown(
    "**Weather Situation Codes:**\n"
    "   - 1: Clear\n"
    "   - 2: Cloudy\n"
    "   - 3: Rain\n"
)

# Visualisasi Peminjaman sepeda pada tahun 2011 dan 2012
dtedayPD = pd.to_datetime(bike_day_df['dteday'])

st.subheader("Peminjaman Sepeda pada Tahun 2011 dan 2012")
fig, ax = plt.subplots(figsize=(8, 6))
sns.lineplot(x=dtedayPD, y="cnt", data=bike_day_df, hue="yr", palette="viridis", ax=ax)
plt.xlabel("Tanggal")
plt.ylabel("Total Peminjaman Sepeda")
plt.title("Tren Peminjaman Sepeda pada Tahun 2011 dan 2012")
plt.xticks(rotation=45)
st.pyplot(fig)


