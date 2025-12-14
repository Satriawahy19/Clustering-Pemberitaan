import streamlit as st
import pandas as pd

st.set_page_config(page_title="Clustering Berita", layout="wide")

st.title("📊 K-Means Clustering Berita Online")
st.write("Website sederhana untuk menampilkan hasil clustering berita.")

data = pd.read_csv("hasil_clustering_berita.csv")

cluster = st.selectbox(
    "Pilih Cluster",
    sorted(data['Cluster'].unique())
)

filtered = data[data['Cluster'] == cluster]

st.subheader(f"Cluster {cluster}")
st.write("Jumlah berita:", len(filtered))

for _, row in filtered.head(10).iterrows():
    st.markdown(f"**{row['JUDUL BERITA']}**")
    st.caption(row['ISI BERITA'][:200] + "...")
