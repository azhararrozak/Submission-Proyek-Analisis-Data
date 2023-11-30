import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
bike_day_df = pd.read_csv("https://raw.githubusercontent.com/azhararrozak/Submission-Proyek-Analisis-Data/main/dataset/day.csv")

# Judul Dashboard
st.title("Dashboard: Analisis Data Peminjaman Sepeda")

# Menampilkan Dataset
st.subheader("Dataset Peminjaman Sepeda")
st.write(bike_day_df.head())

# Tambahkan Sidebar with image
st.sidebar.image("https://img.freepik.com/free-vector/bicycle-sport-recreation_138676-2035.jpg", width=300)
st.sidebar.title("Belajar Data Analisis")
st.sidebar.markdown("Azhar Arrozak")


# Visualisasi Peminjaman sepeda berdasarkan cuaca
st.subheader("Peminjaman Sepeda berdasarkan Kondisi Cuaca")
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x="weathersit", y="cnt", data=bike_day_df, palette="viridis", ax=ax)
plt.xlabel("Kondisi Cuaca")
plt.ylabel("Jumlah Pengguna Sepeda")
plt.title("Jumlah Pengguna Sepeda Berdasarkan Kondisi Cuaca")
st.pyplot(fig)

# Tambahan Informasi
st.markdown("### Informasi Tambahan:")
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

# Tambahkan Footer CopyRight
st.markdown("---")
st.markdown("CopyRight © 2021 | Azhar Arrozak")



