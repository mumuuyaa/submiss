import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import io  

st.title("Mumu's Bike")
st.subheader("by: Mudia Rahmah")

day_data = pd.read_csv("day_data.csv")
hour_data = pd.read_csv("hour_data.csv")

st.subheader("Data Harian")
st.dataframe(day_data)

st.subheader("Data Jam")
st.dataframe(hour_data)

st.subheader("Visualization & Explanatory Analysis")



st.subheader("Pertanyaan 1: Apakah ada perbedaan dalam sewa sepeda antara hari libur dan hari biasa?")

data = day_data
day_data = pd.DataFrame(data)

try:
    avg_rental_holiday = day_data.groupby('holiday')['cnt'].mean()
    avg_rental_weekday = day_data.groupby('weekday')['cnt'].mean()
except KeyError:
    st.error("Kolom 'holiday' atau 'weekday' tidak ditemukan. Periksa nama kolom atau data Anda.")
else:
    # -- Streamlit App --

    st.markdown("""**Perbandingan Sewa Sepeda antara Holiday dan Weekday**""")

    # Combine data for easier plotting
    combined_data = pd.concat([avg_rental_holiday, avg_rental_weekday], axis=1).reset_index()
    combined_data.columns = ['Hari', 'Holiday', 'Weekday']

    # Create the plot using matplotlib
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(combined_data['Hari'], combined_data['Holiday'], label='Holiday', color='skyblue')
    ax.bar(combined_data['Hari'], combined_data['Weekday'], label='Weekday', color='lightgreen')
    ax.set_xlabel('Hari')
    ax.set_ylabel('Rata-rata Sewa Sepeda')
    ax.set_title('Perbandingan Sewa Sepeda antara Holiday dan Weekday')
    ax.legend()

    # Convert plot to image for Streamlit display
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    st.image(buf.getvalue(), width=700)

    # Close the plot to avoid errors
    plt.close()

    # (Optional) Display data as a table
    st.markdown("""**Data Rata-rata Sewa Sepeda**""")
    st.dataframe(combined_data)

st.markdown("""**Insight diagram Perbandingan Sewa Sepeda antara Holiday dan Weekday:**""")
st.markdown("""
* Grafik batang menunjukkan adanya perbedaan yang cukup signifikan antara rata-rata penyewaan sepeda pada hari libur dan hari biasa.
* Rata-rata penyewaan sepeda pada hari libur cenderung lebih sedikit dibandingkan dengan hari biasa. Ini ditunjukkan oleh batang biru yang lebih pendek dibandingkan batang hijau.
* Rata-rata penyewaan sepeda pada hari biasa lebih tinggi, terutama pada hari-hari kerja.
""")


data = day_data
df = pd.DataFrame(data)

avg_rental_holiday = df.groupby('holiday')['cnt'].mean()
avg_rental_weekday = df.groupby('weekday')['cnt'].mean()  

st.markdown("""**Analisis Sewa Sepeda**""")

# Buat kolom pilihan untuk jenis hari
selected_day_type = st.selectbox("Pilih Jenis Hari", ["Holiday", "Weekday"])

# Fungsi untuk membuat plot
def plot_average_rental(day_type):
    if day_type == "Holiday":
        data = avg_rental_holiday
    else:
        data = avg_rental_weekday

    plt.figure(figsize=(10, 5))
    plt.bar(data.index, data.values, label=day_type)
    plt.xlabel(day_type)
    plt.ylabel('Rata-rata Sewa Sepeda')
    plt.title(f'Rata-rata Sewa Sepeda pada {day_type}')
    plt.legend()

    # Simpan plot ke buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    st.image(buf.getvalue(), use_column_width=True)
    plt.close()

plot_average_rental(selected_day_type)

st.markdown("""**Insight diagram Rata-rata Sewa Sepeda:**""")
st.markdown("""
* Rata-rata sewa sepeda pada hari biasa cenderung lebih tinggi dibandingkan dengan hari libur. Hal ini ditunjukkan oleh ketinggian batang pada grafik 'Rata-rata Sewa Sepeda pada Hari Biasa' yang umumnya lebih tinggi dibandingkan batang pada grafik 'Rata-rata Sewa Sepeda pada Hari Libur'.
* Fluktuasi sewa sepeda pada hari biasa lebih besar dibandingkan dengan hari libur. Hal ini terlihat dari perbedaan tinggi batang pada grafik 'Rata-rata Sewa Sepeda pada Hari Biasa', yang menunjukkan bahwa jumlah sewa sepeda pada setiap hari biasa bisa sangat berbeda.
""")






data = day_data
df = pd.DataFrame(data)

season_mapping = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
df['season_name'] = df['season'].map(season_mapping)

avg_rental_season = df.groupby('season_name')['cnt'].mean()

st.subheader("Pertanyaan 2: Apakah lebih banyak orang menyewa sepeda di musim panas atau musim dingin?")

# Buat plot
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(avg_rental_season.index, avg_rental_season.values, color='skyblue')
ax.set_xlabel('Musim')
ax.set_ylabel('Rata-rata Sewa Sepeda')
ax.set_title('Rata-rata Sewa Sepeda per Musim')

# Tampilkan plot di Streamlit
st.pyplot(fig)

# Tampilkan data dalam bentuk tabel
st.markdown("""**Rata-rata Sewa Sepeda per Musim:**""")
st.table(avg_rental_season)

st.markdown("""**Insight:**""")
st.markdown("""
* Batang yang mewakili musim panas lebih tinggi dibandingkan dengan batang yang mewakili musim dingin. Ini menunjukkan bahwa rata-rata jumlah penyewaan sepeda pada musim panas jauh lebih besar.
* Cuaca yang hangat dan cerah pada musim panas cenderung mendorong lebih banyak orang untuk beraktivitas di luar ruangan, termasuk bersepeda. Sebaliknya, cuaca dingin dan hujan pada musim dingin dapat mengurangi minat orang untuk bersepeda.
""")






data = hour_data
df = pd.DataFrame(data)

avg_rental_hour = df.groupby('hr')['cnt'].mean()

st.subheader("Pertanyaan 3: Jam berapa yang paling sibuk untuk sewa sepeda?")

# Buat plot
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(avg_rental_hour.index, avg_rental_hour.values, marker='o', color='purple')
ax.set_xlabel('Jam')
ax.set_ylabel('Rata-rata Sewa Sepeda')
ax.set_title('Jam Paling Sibuk untuk Sewa Sepeda')
ax.grid(True)

# Tampilkan plot di Streamlit
st.pyplot(fig)

# Tampilkan data dalam bentuk tabel
st.markdown("""**Rata-rata Sewa Sepeda per Jam:**""")
st.table(avg_rental_hour)

st.markdown("""**Insight:**""")
st.markdown("""
* Titik tertinggi pada grafik berada di sekitar jam 17.00, yang menunjukkan bahwa rata-rata jumlah penyewaan sepeda mencapai puncaknya pada waktu tersebut.
* Secara umum, grafik menunjukkan pola yang meningkat dari pagi hingga sore hari, mencapai puncaknya di sekitar sore hari, kemudian menurun kembali di malam hari.
""")



st.subheader("Conclusion:")
st.markdown("""
* Berdasarkan analisis kode dan grafik, dapat disimpulkan bahwa ada perbedaan yang signifikan dalam jumlah sewa sepeda antara hari libur dan hari biasa. Rata-rata, jumlah sewa sepeda lebih tinggi pada hari biasa dibandingkan dengan hari libur.
* Grafik tersebut secara jelas menunjukkan adanya preferensi yang kuat terhadap penyewaan sepeda pada musim panas dibandingkan dengan musim dingin. Faktor cuaca yang lebih menyenangkan pada musim panas menjadi salah satu faktor utama yang mempengaruhi tingginya permintaan akan penyewaan sepeda pada musim tersebut.
* Berdasarkan analisis grafik, dapat disimpulkan bahwa jam 17.00 (jam 5 sore) adalah waktu yang paling sibuk untuk menyewa sepeda. Informasi ini sangat berguna bagi penyedia jasa penyewaan sepeda untuk mengatur operasional mereka, seperti penjadwalan karyawan, pengaturan stok sepeda, dan pengembangan strategi pemasaran.
""")