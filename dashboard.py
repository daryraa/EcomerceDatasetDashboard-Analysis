import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Setup halaman
st.set_page_config(layout="wide", page_title="E-Commerce Analysis")

# Judul
st.title("📊 E-Commerce Data Analysis Dashboard")

# Load Data (Pastikan dataset tersedia)
@st.cache_data
def load_data():
    order = pd.read_csv('data/order_full_clean.csv')
    return order

# Load dataset order_full_clean
order = load_data()

# Calculate total orders and revenue
total_orders = order['order_id'].nunique()
total_revenue = order['payment_value'].sum()

# Create a metrics section at the top of your dashboard
st.header("📊 Overview Penjualan")

# Create two columns
col1, col2 = st.columns(2)

# Display metrics with large font and icons
with col1:
    st.metric(label="🛒 Total Orders", value=f"{total_orders:,}")
    
with col2:
    st.metric(label="💰 Total Revenue", value=f"Rp {total_revenue:,.2f}")

# Add a divider for visual separation
st.markdown("---")

# 1️⃣ **Performa Penjualan & Revenue**
st.header("📈 Performa Penjualan & Revenue")
order["order_purchase_timestamp"] = pd.to_datetime(order["order_purchase_timestamp"])

# Convert to string format instead of Period object
monthly_sales = order.groupby(order["order_purchase_timestamp"].dt.strftime('%Y-%m'))["order_id"].count().reset_index()
monthly_sales.columns = ["Bulan", "Total Transaksi"]

fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=monthly_sales, x="Bulan", y="Total Transaksi", marker="o", ax=ax)
ax.set_title("Tren Transaksi Per Bulan")
ax.set_xlabel("Bulan")
ax.set_ylabel("Total Transaksi")
plt.xticks(rotation=45)
st.pyplot(fig)

st.write("💡 **Insight**: Tren transaksi per bulan menunjukkan fluktuasi. Strategi promo bisa disesuaikan dengan pola ini.")

# 2️⃣ **Produk Paling Laku & Kurang Diminati**
st.header("🔥 Produk Terlaris & Kurang Diminati")
top_products = order["product_id"].value_counts().head(5)
least_products = order["product_id"].value_counts().tail(5)

col1, col2 = st.columns(2)
with col1:
    st.subheader("🔝 Produk Terlaris")
    st.bar_chart(top_products)

with col2:
    st.subheader("🔻 Produk Kurang Laku")
    st.bar_chart(least_products)

st.write("💡 **Insight**: Produk dengan permintaan tinggi bisa dipromosikan lebih agresif, sementara produk kurang laku dapat dievaluasi.")

# 4️⃣ **RFM Analysis**
st.header("👑 Analisis RFM (Recency, Frequency, Monetary)")

# Prepare RFM data
st.write("Menyiapkan data RFM...")

# Assuming you have already prepared rfm_df in your code or need to prepare it here
# For this example, I'll create a simplified version
order['order_purchase_timestamp'] = pd.to_datetime(order['order_purchase_timestamp'])

# Get the most recent date
max_date = order['order_purchase_timestamp'].max()

# Create customer-level RFM metrics
rfm = order.groupby('customer_id').agg({
    'order_purchase_timestamp': lambda x: (max_date - x.max()).days,  # Recency
    'order_id': 'nunique',  # Frequency
    'payment_value': 'sum'  # Monetary
}).reset_index()

rfm.columns = ['customer_id', 'recency', 'frequency', 'monetary']

# Potong customer_id jadi 5 karakter pertama
rfm["short_customer_id"] = rfm["customer_id"].astype(str).str[:5]

# Create the RFM visualizations
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(20, 6))
colors = ["#72BCD4", "#72BCD4", "#72BCD4", "#72BCD4", "#72BCD4"]

# By Recency
sns.barplot(
    y="recency", 
    x="short_customer_id", 
    data=rfm.sort_values(by="recency", ascending=True).head(5), 
    palette=colors, 
    ax=ax[0]
)
ax[0].set_ylabel("Recency (days)")
ax[0].set_xlabel(None)
ax[0].set_title("By Recency (days)", loc="center", fontsize=14)
ax[0].tick_params(axis='x', labelsize=12)

# By Frequency
sns.barplot(
    y="frequency", 
    x="short_customer_id", 
    data=rfm.sort_values(by="frequency", ascending=False).head(5), 
    palette=colors, 
    ax=ax[1]
)
ax[1].set_ylabel("Frequency")
ax[1].set_xlabel(None)
ax[1].set_title("By Frequency", loc="center", fontsize=14)
ax[1].tick_params(axis='x', labelsize=12)

# By Monetary
sns.barplot(
    y="monetary", 
    x="short_customer_id", 
    data=rfm.sort_values(by="monetary", ascending=False).head(5), 
    palette=colors, 
    ax=ax[2]
)
ax[2].set_ylabel("Monetary Value")
ax[2].set_xlabel(None)
ax[2].set_title("By Monetary", loc="center", fontsize=14)
ax[2].tick_params(axis='x', labelsize=12)

plt.suptitle("Best Customer Based on RFM Parameters", fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.95])
st.pyplot(fig)

st.write("💡 **Insight**: Analisis RFM menunjukkan pelanggan-pelanggan terbaik berdasarkan kebaruan pembelian, frekuensi, dan total belanja.")

# 5️⃣ **Distribusi Skor Ulasan**
st.header("⭐ Distribusi Skor Ulasan")

# Basic distribution of review scores
review_distribution = order["review_score"].value_counts().sort_index()
st.bar_chart(review_distribution)

# Prepare monthly review trend data
order['review_creation_date'] = pd.to_datetime(order['review_creation_date'])
order['month'] = order['review_creation_date'].dt.strftime('%Y-%m')

# Create pivot table for stacked bar chart
review_trend = pd.pivot_table(
    data=order,
    index='month',
    columns='review_score',
    aggfunc='size',
    fill_value=0
).reset_index()

# Plot stacked bar chart for review scores over time
fig, ax = plt.subplots(figsize=(12, 6))
review_trend.set_index('month').plot(kind='bar', stacked=True, ax=ax, colormap='viridis')
plt.title("Distribusi Skor Ulasan Pelanggan Per Bulan")
plt.xlabel("Bulan")
plt.ylabel("Jumlah Ulasan")
plt.legend(title="Skor Ulasan", loc='upper left', bbox_to_anchor=(1,1))
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
st.pyplot(fig)

st.write("💡 **Insight**: Mayoritas pelanggan puas, tetapi perlu memperhatikan tren ulasan negatif yang perlu ditindaklanjuti.")

# 6️⃣ **Performa Seller**
st.header("🏆 Top Seller Berdasarkan Transaksi & Revenue")

top_sellers_transactions = order["seller_id"].value_counts().head(5)
top_sellers_revenue = order.groupby("seller_id")["payment_value"].sum().sort_values(ascending=False).head(5)

col1, col2 = st.columns(2)
with col1:
    st.subheader("📌 Top Seller - Transaksi Terbanyak")
    st.bar_chart(top_sellers_transactions)

with col2:
    st.subheader("💰 Top Seller - Revenue Tertinggi")
    st.bar_chart(top_sellers_revenue)

st.write("💡 **Insight**: Seller dengan transaksi dan revenue tinggi bisa diberikan insentif atau fitur eksklusif.")

# 📌 **Rekomendasi Bisnis**
st.header("📌 Rekomendasi")
st.markdown(""" 
- **Optimalkan produk dengan penjualan tinggi** dengan promo dan diskon.
- **Evaluasi dan tindaklanjuti ulasan negatif** untuk meningkatkan kualitas layanan.
- **Dukung seller terbaik** dengan insentif agar mereka semakin berkembang.
- **Program loyalitas khusus** untuk pelanggan RFM terbaik untuk meningkatkan retensi.
""")

st.markdown("By Dary Ramadhan Abdussalam")
