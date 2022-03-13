import streamlit as st

st.title('Aplikasi Menghitung Luas, Alas, Dan Tinggi Segitiga')
st.caption('## Ini adalah aplikasi menghitung segitiga sederhana XD')




st.header('Menghitung Luas')
alas = st.slider('Masukkan Alas', 0)
tinggi = st.slider('Masukkan Tinggi', 0)
hitung = st.button('Hitung Luas')

if hitung:
    luas = 0.5  * tinggi * alas
    st.success(f'Luas Segitiganya Adalah {luas}')

st.header('Menghitung Alas')
luas1 = st.slider('Masukkan Luas', 0)
tinggi1 = st.slider('Masukkan Tinggi.', 0)
hitung1 = st.button('Hitung Alas')

if hitung1:
    alas1 = luas1 * 2 / tinggi1
    st.success(f'Alas Segitiganya Adalah {alas1}')

st.header('Menghitung Tinggi')
luas2 = st.slider('Masukkan Luas.', 0)
alas2 = st.slider('Masukkan alas.', 0)
hitung2 = st.button('Hitung Tinggi')

if hitung2:
    tinggi2 = luas2 * 2 / alas2
    st.success(f'Tinggi Segitiganya Adalah {tinggi2}')
