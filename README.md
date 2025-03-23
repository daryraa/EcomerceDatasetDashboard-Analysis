# Dashboard Analisis Data E-Commerce 

Dashboard ini dibuat buat ngelihat data e-commerce dengan cara yang lebih gampang dan visual. Bisa buat ngecek performa penjualan, produk mana yang laris atau kurang diminati, ulasan pelanggan, sampai performa penjual. Kita pakai **Streamlit**, **Pandas**, **Matplotlib**, **Seaborn**, dan **Geopandas** buat bikin dashboard ini jalan.

Link Dashboard : https://ecomercedatasetdashboard-analysis-test.streamlit.app/

## Sebelum Mulai 🔧

Pastikan udah install **Python** atau pakai **conda** buat manajemen lingkungan kerja.

## Cara Setup Lingkungan 

Kalau pakai **conda**, ikutin langkah-langkah ini ya:

1. Bikin environment baru dengan Python 3.9:

   ```bash
   conda create --name main-ds python=3.9
   ```

2. Aktifin environment yang tadi dibuat:

   ```bash
   conda activate main-ds
   ```

3. Install semua yang dibutuhkan:

   ```bash
   pip install -r requirements.txt
   ```

   Pastikan ada file `requirements.txt` di folder proyek kamu, yang isinya kurang lebih kayak gini:

   ```
   streamlit
   pandas
   matplotlib
   seaborn
   geopandas
   shapely
   ```

## Siapin Datanya 

Pastikan semua dataset udah ada di folder `data/`:

- `customers_dataset.csv` - Data pelanggan
- `geolocation_dataset.csv` - Data lokasi pelanggan
- `order_items_dataset.csv` - Data barang yang dipesan
- `order_payments_dataset.csv` - Data pembayaran
- `order_reviews_dataset.csv` - Data ulasan pelanggan
- `orders_dataset.csv` - Data pesanan
- `product_category_name_translation.csv` - Data kategori produk
- `products_dataset.csv` - Data produk
- `sellers_dataset.csv` - Data penjual

Simpan semua file ini di folder `data/` dalam proyek.

## Cara Jalankan Dashboard 

1. Pastikan semua yang dibutuhkan udah terinstall (cek langkah sebelumnya).
2. Pastikan dataset ada di folder `data/`.
3. Jalankan perintah ini di terminal atau command prompt:

   ```bash
   streamlit run dashboard.py
   ```

4. Browser bakal otomatis kebuka, dan dashboard bisa langsung dipakai!
