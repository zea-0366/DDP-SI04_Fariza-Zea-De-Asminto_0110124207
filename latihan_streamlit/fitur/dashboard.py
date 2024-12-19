import streamlit as st

st.title("Halaman Dashboard")
st.image("image.jpeg",  caption="Gambar Rumah")

#  Fungsi Menghitung dan Menyimpan Data
def total():
  total_nabung = sum(z["Jumlah"]
                     for z in st.session_state["total_semua"]
                     if z ["Tipe"] == "Menabung")
  return total_nabung 

total_semua = st.session_state["total_semua"]
total_nabung = total()

st.metric("Total Menabung", f"Rp {total_nabung}")