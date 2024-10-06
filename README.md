# Bike-Sharing Dashboard

## Deskripsi Proyek
Dashboard ini dirancang untuk menganalisis dan memvisualisasikan data penggunaan layanan bike-sharing. Proyek ini menggunakan dataset yang berisi informasi tentang penggunaan bike-sharing, termasuk data mengenai anggota dan non-anggota, serta pemakaian berdasarkan musim dan hari dalam seminggu.

## Tujuan
- Menjawab pertanyaan bisnis berikut:
  1. **Bagaimana Musim Mempengaruhi Penggunaan Bike Sharing?**
  2. **Bagaimana Perbandingan Pengguna Bike Sharing antara Non-Anggota dan Anggota Berdasarkan Tahun?**

## Fitur
- Visualisasi total penggunaan bike-sharing berdasarkan bulan.
- Analisis jumlah penggunaan bike-sharing berdasarkan musim.
- Perbandingan jumlah pengguna non-anggota dan anggota.

## Instalasi
Untuk menjalankan dashboard ini, Anda perlu menginstal dependensi yang diperlukan. Gunakan perintah berikut:

- conda create --name main-ds python=3.9
- conda init
- conda activate main-ds
- pip install pandas matplotlib babel seaborn plotly streamlit

## Run streamlit app
- streamlit run dashboard/app.py
