import streamlit as st
from core import valumotion_hesapla

st.set_page_config(page_title="ValuMotionX", layout="wide")
st.title("ValuMotionX - Değer Simülasyon Motoru")

with st.sidebar:
    st.header("Parametreler")
    zaman = st.slider("Zaman - saniye", 1, 60, 10)
    maddi = st.slider("Maddi Boyut", 0.0, 1.0, 0.7)
    manevi = st.slider("Manevi Boyut", 0.0, 1.0, 0.7) 
    dis = st.slider("Dış Boyut", 0.0, 1.0, 0.6)
    x_puan = st.slider("X Puan", 0.0, 1.0, 0.75)
    mod = st.selectbox("Mod", ["birey", "aile", "ekonomi", "egitim", "toplum", "proje"])

sonuc = valumotion_hesapla(zaman, maddi, manevi, dis, x_puan, mod)

col1, col2, col3 = st.columns(3)
col1.metric("Değer Skoru", sonuc["deger_skoru"])
col2.metric("Yer Değiştirme", sonuc["yer_degistirme"]) 
col3.metric("Birleşme", sonuc["birlesme"])

st.subheader(sonuc["durum"])
