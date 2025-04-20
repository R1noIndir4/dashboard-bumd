
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard Interaktif BUMD Indonesia", layout="wide")

# Load all data
summary_df = pd.read_excel('Final_Tabels_Analisis_BUMD.xlsx', sheet_name='Summary_Pos_Neg')
roa_roe_df = pd.read_excel('Final_Tabels_Analisis_BUMD.xlsx', sheet_name='ROA_ROE')
untung_rugi_df = pd.read_excel('Final_Tabels_Analisis_BUMD.xlsx', sheet_name='Untung_Rugi')
trend_df = pd.read_excel('Final_Tabels_Analisis_BUMD.xlsx', sheet_name='Trend_Aset_Ekuitas')
solv_der_df = pd.read_excel('Final_Tabels_Analisis_BUMD.xlsx', sheet_name='Solvabilitas_DER')
provinsi_strength_df = pd.read_excel('Final_Tabels_Analisis_BUMD.xlsx', sheet_name='Provinsi_Strength')
potensi_sektor_df = pd.read_excel('Final_Tabels_Analisis_BUMD.xlsx', sheet_name='Potensi_Sektor')
aset_laba_df = pd.read_excel('Final_Tabels_Analisis_BUMD.xlsx', sheet_name='Aset_vs_Laba')
pad_df = pd.read_excel('Final_Tabels_Analisis_BUMD.xlsx', sheet_name='PAD_Contribution')
cluster_df = pd.read_excel('Final_Tabels_Analisis_BUMD.xlsx', sheet_name='Cluster_Analysis')

st.title("📊 Dashboard Interaktif - Analisis BUMD Indonesia 2025")

st.header("1️⃣ ROA dan ROE BUMD per Sektor")
st.dataframe(roa_roe_df)

fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(roa_roe_df['Kategori Lapangan Usaha'], roa_roe_df['ROA (%) 2023'], label='ROA')
ax.barh(roa_roe_df['Kategori Lapangan Usaha'], roa_roe_df['ROE (%) 2023'], label='ROE', alpha=0.7)
ax.set_xlabel('Persentase (%)')
ax.set_title('ROA dan ROE per Sektor BUMD')
ax.legend()
st.pyplot(fig)

st.header("2️⃣ Jumlah BUMD Untung vs Rugi per Provinsi")
st.dataframe(untung_rugi_df)

st.header("3️⃣ Tren Aset dan Ekuitas BUMD")
st.line_chart(trend_df.set_index('Tahun'))

st.header("4️⃣ Solvabilitas dan DER per Sektor")
st.dataframe(solv_der_df)

st.header("5️⃣ Pemetaan Provinsi BUMD Terkuat")
st.bar_chart(provinsi_strength_df.set_index('Provinsi'))

st.header("6️⃣ Sektor Usaha BUMD Paling Potensial")
st.bar_chart(potensi_sektor_df.set_index('Kategori Lapangan Usaha')['Skor Potensi'])

st.header("7️⃣ Korelasi Total Aset vs Laba Bersih")
st.scatter_chart(aset_laba_df.set_index('Provinsi'))

st.header("8️⃣ Kontribusi BUMD terhadap PAD")
st.bar_chart(pad_df.set_index('Provinsi'))

st.header("9️⃣ Cluster Analysis BUMD berdasarkan Kinerja")
st.dataframe(cluster_df)
