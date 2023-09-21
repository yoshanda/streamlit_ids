# -*- coding: utf-8 -*-
"""stream-ids.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jvzfxs93Amf5S-gPMbQseeh8NT8z6Jma
"""

!pip install streamlit -q

!wget -q -O - ipv4.icanhazip.com

import pickle
import streamlit as st

from google.colab import drive
drive.mount('/content/drive')

# membaca model
ids_model = pickle.load(open('/content/drive/MyDrive/Persiapan Skripsi/Bismillah/IDS/model.pkl', 'rb'))

#judul web
st.title('Prediksi Serangan Jaringan')

#membagi kolom
col1, col2, col3 = st.columns(3)

with col1 :
    protocol_type_new = st.text_input ('input protocol type')

with col2 :
    service_new = st.text_input ('input service')

with col3 :
    flag_new = st.text_input ('input flag')

# code untuk prediksi
detek_serangan = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi Serangan Jaringan'):
    prediksi_serangan = ids_model.predict([[protocol_type_new, service_new, flag_new]])

    if(prediksi_serangan[0] == 0):
        detek_serangan = 'Terdeteksi Serangan DoS'
    elif(prediksi_serangan[0] == 1):
        detek_serangan = 'Terdeteksi Serangan Probe'
    elif(prediksi_serangan[0] == 2):
        detek_serangan = 'Terdeteksi Serangan R2L'
    elif(prediksi_serangan[0] == 3):
        detek_serangan = 'Terdeteksi Serangan U2R'
    else:
        detek_serangan = 'Terdeteksi Bukan Serangan'
st.success(detek_serangan)