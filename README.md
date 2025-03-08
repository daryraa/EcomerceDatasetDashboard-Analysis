# E-Commerce Data Analysis Dashboard

Dashboard ini dirancang untuk menganalisis data e-commerce dan memberikan wawasan tentang performa penjualan, produk, ulasan pelanggan, serta performa penjual. Dashboard ini dibangun menggunakan **Streamlit**, **Pandas**, **Matplotlib**, **Seaborn**, dan **Geopandas**.

## Prasyarat

Pastikan Anda memiliki **Python 3.x** atau **conda** terinstal di sistem Anda.

## Menyiapkan Lingkungan

Jika Anda menggunakan **conda** untuk mengelola lingkungan, ikuti langkah-langkah berikut:

1. Buat lingkungan conda baru dengan Python 3.9:

   ```bash
   conda create --name main-ds python=3.9
   ```

2. Aktifkan lingkungan yang baru dibuat:

   ```bash
   conda activate main-ds
   ```

3. Instal dependensi yang diperlukan dengan menjalankan perintah berikut:

   ```bash
   pip install -r requirements.txt
   ```

   Pastikan file `requirements.txt` ada di direktori proyek Anda dengan daftar pustaka seperti:

   ```
   streamlit
   pandas
   matplotlib
   seaborn
   geopandas
   shapely
   ```

## Menyiapkan Data

Pastikan Anda memiliki dataset berikut di folder `data/`:

- `customers_dataset.csv` - Data pelanggan
- `geolocation_dataset.csv` - Data geolokasi pelanggan
- `order_items_dataset.csv` - Data item pesanan
- `order_payments_dataset.csv` - Data pembayaran pesanan
- `order_reviews_dataset.csv` - Data ulasan pesanan
- `orders_dataset.csv` - Data pesanan
- `product_category_name_translation.csv` - Data kategori produk
- `products_dataset.csv` - Data produk
- `sellers_dataset.csv` - Data penjual

Letakkan semua berkas CSV tersebut di dalam folder `data/` di direktori proyek Anda.

## Menjalankan Dashboard

1. Pastikan semua pustaka yang diperlukan sudah terinstal (lihat langkah di atas).
2. Letakkan semua berkas dataset di folder `data/`.
3. Jalankan aplikasi Streamlit dengan perintah berikut di terminal atau command prompt:

   ```bash
   streamlit run app.py
   ```

4. Setelah itu, aplikasi Streamlit akan terbuka di browser Anda, biasanya di `http://localhost:8501`.

## Fitur Dashboard

- **Overview Penjualan**: Menampilkan metrik total pesanan dan total pendapatan.
- **Performa Penjualan & Revenue**: Menampilkan tren transaksi per bulan.
- **Produk Terlaris & Kurang Diminati**: Menampilkan produk yang paling banyak terjual dan yang kurang diminati.
- **Analisis RFM (Recency, Frequency, Monetary)**: Menganalisis pelanggan berdasarkan kebaruan pembelian, frekuensi, dan nilai transaksi.
- **Distribusi Skor Ulasan**: Menampilkan distribusi skor ulasan pelanggan dan tren ulasan bulanan.
- **Top Seller Berdasarkan Transaksi & Revenue**: Menampilkan penjual dengan transaksi dan pendapatan tertinggi.
- **Rekomendasi Bisnis**: Memberikan rekomendasi bisnis berdasarkan analisis data.

## Insight

Dashboard ini memberikan wawasan yang berguna untuk:
- Mengidentifikasi produk yang perlu dipromosikan lebih agresif.
- Mengetahui tren ulasan pelanggan untuk meningkatkan layanan.
- Menganalisis performa penjual dan memberikan insentif bagi yang terbaik.
- Meningkatkan retensi pelanggan dengan program loyalitas berdasarkan analisis RFM.