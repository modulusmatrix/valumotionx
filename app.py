import streamlit as st
import plotly.graph_objects as go
from core import valumotion_hesapla

st.set_page_config(page_title="ValuMotionX", page_icon="⚡", layout="wide")

st.title("⚡ ValuMotionX - Yer Değiştirme ve Birleşme Teorisi")
st.caption("Maddi + Manevi boyutların çarpımsal etkisiyle değer hesabı")

with st.sidebar:
    st.header("🎛️ Parametreler")
    zaman = st.slider("Zaman (saniye)", 1, 120, 10)
    maddi = st.slider("Maddi Boyut", 0.0, 1.0, 0.7, 0.05, 
                     help="Fiziksel/kaynak değeri")
    manevi = st.slider("Manevi Boyut", 0.0, 1.0, 0.7, 0.05,
                      help="Anlam/duygu değeri")
    dis = st.slider("Dış Boyut", 0.0, 1.0, 0.6, 0.05,
                   help="Çevre/etki alanı")
    x_puan = st.slider("X Faktörü", 0.0, 1.0, 0.75, 0.05,
                      help="Bilinmeyen/katalizör")
    mod = st.selectbox("Uygulama Modu", 
                      ["birey", "aile", "ekonomi", "egitim", "toplum", "proje"])

try:
    sonuc = valumotion_hesapla(zaman, maddi, manevi, dis, x_puan, mod)
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Değer Skoru", sonuc["deger_skoru"])
    col2.metric("Yer Değiştirme", sonuc["yer_degistirme"])
    col3.metric("Birleşme", sonuc["birlesme"])
    col4.metric("Mod Katsayısı", f"x{sonuc['mod_katsayisi']}")
    
    st.subheader(sonuc["durum"])
    st.write(sonuc["aciklama"])
    
    # Radar Chart
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=[maddi, manevi, dis, x_puan, maddi],
        theta=['Maddi', 'Manevi', 'Dış Boyut', 'X Faktör', 'Maddi'],
        fill='toself', name='Mevcut Durum'
    ))
    fig.update_layout(polar=dict(radialaxis=dict(range=[0, 1])), height=400)
    st.plotly_chart(fig, use_container_width=True)

except ValueError as e:
    st.error(f"Hata: {e}")

with st.expander("📚 Teori Nedir?"):
    st.markdown("""
    **Yer Değiştirme**: 4 boyutun aritmetik ortalaması. Dengeyi gösterir.
    
    **Birleşme**: 4 boyutun geometrik ortalaması. Biri sıfırsa hepsi çöker = Çarpımsal etki.
    
    **Formül**: `Değer = Zaman × Yer Değiştirme × Birleşme × Mod Katsayısı`
    """)
