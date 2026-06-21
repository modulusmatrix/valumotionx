import streamlit as st
import plotly.graph_objects as go
from core import valumotion_hesapla

st.set_page_config(page_title="ValuMotionX", page_icon="⚡", layout="wide")

st.title("⚡ ValuMotionX")
st.caption("Yer Değiştirme ve Birleşme Teorisi - Değer Simülasyon Motoru")

with st.sidebar:
    st.header("🎛️ Parametreler")
    zaman = st.slider("Zaman (sn)", 1, 120, 10)
    maddi = st.slider("Maddi Boyut", 0.0, 1.0, 0.7, 0.05)
    manevi = st.slider("Manevi Boyut", 0.0, 1.0, 0.7, 0.05)
    dis = st.slider("Dış Boyut", 0.0, 1.0, 0.6, 0.05)
    x_puan = st.slider("X Faktörü", 0.0, 1.0, 0.75, 0.05)
    mod = st.selectbox("Mod", ["birey", "aile", "ekonomi", "egitim", "toplum", "proje"])

try:
    sonuc = valumotion_hesapla(zaman, maddi, manevi, dis, x_puan, mod)
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Değer Skoru", sonuc["deger_skoru"])
    col2.metric("Yer Değiştirme", sonuc["yer_degistirme"])
    col3.metric("Birleşme", sonuc["birlesme"])
    col4.metric("Mod Katsayısı", f"x{sonuc['mod_katsayisi']}")
    
    st.subheader(sonuc["durum"])
    st.info(sonuc["aciklama"])
    
    # Radar Chart - 4 boyut
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=[sonuc['maddi'], sonuc['manevi'], sonuc['dis_boyut'], sonuc['x_puan'], sonuc['maddi']],
        theta=['Maddi', 'Manevi', 'Dış Boyut', 'X Faktör', 'Maddi'],
        fill='toself', 
        name='Mevcut Durum',
        line_color='#FF4B4B'
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(range=[0, 1], showticklabels=True)),
        showlegend=False, height=400,
        title="4 Boyut Analizi"
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Detay tablosu
    with st.expander("📊 Hesap Detayları"):
        st.json(sonuc)

except ValueError as e:
    st.error(f"❌ Hata: {e}")
except KeyError as e:
    st.error(f"❌ Eksik veri: {e}. core.py return kısmını kontrol et")
except Exception as e:
    st.error(f"❌ Beklenmedik hata: {e}")

with st.expander("📚 Yer Değiştirme ve Birleşme Teorisi Nedir?"):
    st.markdown("""
    **Yer Değiştirme Skoru**: 4 boyutun aritmetik ortalaması `(maddi+manevi+dis+x)/4`. Dengeyi ölçer.
    
    **Birleşme Skoru**: 4 boyutun geometrik ortalaması `(maddi×manevi×dis×x)^0.25`. Çarpımsal etki. Biri 0 ise sonuç 0.
    
    **Formül**: `Değer = Zaman × Yer Değiştirme × Birleşme × Mod Katsayısı`
    
    **Modlar**: Birey x1.0, Aile x1.2, Ekonomi x1.15, Eğitim x1.25, Toplum x1.4, Proje x1.1
    """)
