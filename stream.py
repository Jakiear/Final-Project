# import libary 
import streamlit as st
import joblib
import pandas as pd
import time

# page title
st.set_page_config(
    page_title="Prediksi Kemungkinan Stunting Bayi Sampai Umur 60 Bulan")

hide_style = """
<style>
#MainMenu {visibility: visible;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_style, unsafe_allow_html=True) 

# Title
st.markdown("<h1 style='text-align: center;'>Prediksi Kemungkinan Stunting Bayi Sampai Umur 60 Bulan</h1>", unsafe_allow_html=True)

#Elemen
nama = st.text_input("Masukkan Nama",placeholder='Nama')
umur = st.number_input("Masukkan Umur (bulan)", min_value = 0, max_value=60)
jk = st.selectbox("Jenis Kelamin",('Laki-laki','Perempuan'))
tb = st.text_input("Masukkan Tinggi Badan (cm)")

# preprocessing
def normalisasi(x):
    # import data test
    cols = ['umur', 'jk', 'tb']
    df = pd.DataFrame([x],columns=cols)
    data_test = pd.read_csv('data_test.csv')
    data_test = data_test.drop(data_test.columns[0],axis=1)
    # memasukkan data kedalam data test
    data_test = data_test._append(other=df,ignore_index=True)
    # return data_test yang sudah dinormalisasi
    return (data_test)

def knn(x): 
    return joblib.load('modelKNN1.pkl').predict(x)

# Button 
sumbit = st.button("Tes Prediksi")
if sumbit == True:
      if  nama != '' and jk != '' and tb != 0 and umur != 0:
            if jk == 'Laki-laki':
                 jk = 0
            else:
                 jk = 1
            # normalisasi data
            data = normalisasi([umur,jk,tb])
            # prediksi data
            prediksi = knn(data)
            # cek prediksi
            with st.spinner("Tunggu Sebentar..."):
                  if prediksi[-1] == 0:
                        time.sleep(1)
                        st.warning("Hasil Prediksi: "+nama+" Sangat Pendek / Severely Stunted (Ada Kemungkinan Terkena Stunting)")
                        st.write("""
                                 Upaya yang bisa dilakukan untuk meningkatkan kondisi gizi seperti: 
                                 1) Mulai berikan asupan makanan yang bernutrisi dan bergizi, seperti protein hewani pada mpasi.
                                 2) Memberikan suplemen tambahan terutama yang mengandung vitamin A, Zinc, zat besi, kalsium dan yodium.
                                 3) Menerapkan pola hidup bersih dengan menjaga sanitasi dan kebersihan lingkungan tempat tinggal.
                                 4) Melakukan imunisasi rutin sesuai jadwal.
                                 
                                 Sumber: Kementerian Kesehatan Republik Indonesia
                                 """)
                  elif prediksi [-1] == 1:
                        time.sleep(1)
                        st.warning("Hasil Prediksi: "+nama+" Pendek / Stunted (Ada Kemungkinan Terkena Stunting)")
                        st.write("""
                                 Upaya yang bisa dilakukan untuk meningkatkan kondisi gizi seperti: 
                                 1) Mulai berikan asupan makanan yang bernutrisi dan bergizi, seperti protein hewani pada mpasi.
                                 2) Memberikan suplemen tambahan terutama yang mengandung vitamin A, Zinc, zat besi, kalsium dan yodium.
                                 3) Menerapkan pola hidup bersih dengan menjaga sanitasi dan kebersihan lingkungan tempat tinggal.
                                 4) Melakukan imunisasi rutin sesuai jadwal.
                                 
                                 Sumber: Kementerian Kesehatan Republik Indonesia
                                 """)
                  elif prediksi [-1] == 2:
                        time.sleep (1)
                        st.success("Hasil Prediksi: "+nama+" Normal (Tidak Terkena Stunting)")
                        st.write("""
                                 Upaya yang bisa dilakukan untuk mempertahankan kondisi gizi dan mencegah kondisi stunting seperti: 
                                 1) Pemenuhan gizi ibu saat hamil terutama zat besi.
                                 2) Memberikan ASI eksklusif sampai 6 bulan dan setelah 6 bulan diberikan makanan pendamping ASI yang bernutrisi juga bergizi.
                                 3) Mendapatkan akses air bersih dan fasilitas sanitasi, serta menjaga lingkungan tetap bersih.
                                 4) Memantau pertumbuhan bayi dan melakukan imunisasi rutin sesuai jadwal.
                                 
                                 Sumber: Kementerian Kesehatan Republik Indonesia
                                 """)
                  elif prediksi [-1] == 3:
                        time.sleep (1)
                        st.success("Hasil Prediksi: "+nama+" Tinggi (Tidak Terkena Stunting)")
                        st.write("""
                                 Upaya yang bisa dilakukan untuk mempertahankan kondisi gizi dan mencegah kondisi stunting seperti: 
                                 1) Pemenuhan gizi ibu saat hamil terutama zat besi.
                                 2) Memberikan ASI eksklusif sampai 6 bulan dan setelah 6 bulan diberikan makanan pendamping ASI yang bernutrisi juga bergizi.
                                 3) Mendapatkan akses air bersih dan fasilitas sanitasi, serta menjaga lingkungan tetap bersih.
                                 4) Memantau pertumbuhan bayi dan melakukan imunisasi rutin sesuai jadwal.
                                 
                                 Sumber: Kementerian Kesehatan Republik Indonesia
                                 """)
      else:
          st.error("Harap Isi Semua Kolom")



