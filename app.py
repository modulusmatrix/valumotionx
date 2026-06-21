import streamlit as st
import plotly.graph_objects as go
from core import valumotion_hesapla

st.set_page_config(
    page_title="ValuMotionX", 
    page_icon="⚡", 
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("⚡ ValuMotionX")
st.caption("Yer Değiştirme ve Birleşme Teorisi - Değer Simülasyon Motoru")

# Sidebar
with st.sidebar:
    st.header("🎛️ Parametreler")
    zaman = st.slider("Zaman (saniye)", 1, 120, 10, 
                     help="Sürecin toplam süresi")
    maddi = st.slider("Maddi Boyut", 0.0, 1.0, 0.7, 0.01,
                     help="Fiziksel kaynak, para, mal")
    manevi = st.slider("Manevi Boyut", 0.0, 1.0, 0.7, 0.01,
                      help="Anlam, duygu, motivasyon")
    dis = st.slider("Dış Boyut", 0.0, 1.0, 0.6, 0.01,
                   help="Çevre, sosyal etki, koşullar")
    x_puan = st.slider("X Faktörü", 0.0, 1.0, 0.75, 0.01,
                      help="Bilinmeyen, şans, katalizör")
    mod = st.selectbox("Uygulama Modu", 
                      ["birey", "aile", "ekonomi", "egitim", "toplum", "proje"],
                      help="Hesaplama hangi alanda yapılıyor")
    
    st.divider()
    if st.button("🔄 Varsayılana Dön", use_container_width=True):
        st.rerun()

# Hesaplama
try:
    sonuc = valumotion_hesapla(zaman, maddi, manevi, dis, x_puan, mod)
    
    # Metrikler
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Değer Skoru", sonuc["deger_skoru"], 
               delta=round(sonuc["deger_skoru"] - 10, 2))
    col2.metric("Yer Değiştirme", sonuc["yer_degistirme"])
    col3.metric("Birleşme", sonuc["birlesme"])
    col4.metric("Mod Katsayısı", f"x{sonuc.get('mod_katsayisi', 1.0)}")
    
    st.subheader(sonuc["durum"])
    st.info(sonuc["aciklama"])
    
    # Grafikler yan yana
    g1, g2 = st.columns(2)
    
    with g1:
        # Radar Chart
        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(
            r=[sonuc['maddi'], sonuc['manevi'], sonuc['dis_boyut'], 
               sonuc['x_puan'], sonuc['maddi']],
            theta=['Maddi', 'Manevi', 'Dış Boyut', 'X Faktör', 'Maddi'],
            fill='toself', name='Boyutlar', line_color='#FF4B4B'
        ))
        fig_radar.update_layout(
            polar=dict(radialaxis=dict(range=[0, 1])),
            height=350, title="4 Boyut Dengesi", showlegend=False
        )
        st.plotly_chart(fig_radar, use_container_width=True)
    
    with g2:
        # Gauge Chart - Değer Skoru
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=sonuc["deger_skoru"],
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Değer Seviyesi"},
            gauge={'axis': {'range': [0, 50]},
                   'bar': {'color': "#FF4B4B"},
                   'steps': [
                       {'range': [0, 10], 'color': "#FFE5E5"},
                       {'range': [10, 25], 'color': "#FFB3B3"},
                       {'range': [25, 50], 'color': "#FF8080"}],
                   'threshold': {'line': {'color': "red", 'width': 4},
                                'thickness': 0.75, 'value': 15}}))
        fig_gauge.update_layout(height=350)
        st.plotly_chart(fig_gauge, use_container_width=True)
    
    # Detay
    with st.expander("📊 Detaylı Sonuçlar"):
        st.json(sonuc)

except ValueError as e:
    st.error(f"❌ Giriş Hatası: {e}")
except KeyError as e:
    st.error(f"❌ Veri Hatası: {e}. core.py return kısmını kontrol et")
except Exception as e:
    st.error(f"❌ Hata: {e}")

with st.expander("📚 Teori Nasıl Çalışır?"):
    st.markdown("""
    **Yer Değiştirme**: `(Maddi + Manevi + Dış + X) / 4` → Aritmetik ortalama. Dengeli dağılım = yüksek skor.
    
    **Birleşme**: `(Maddi × Manevi × Dış × X)^0.25` → Geometrik ortalama. Çarpımsal etki. Bir boyut 0 ise tüm sistem 0.
    
    **Nihai Değer**: `Zaman × Yer Değiştirme × Birleşme × Mod Katsayısı`
    
    **Örnek**: Maddi=0.9, Manevi=0.1 → Yer Değiştirme=0.5 ama Birleşme=0.3. Dengesizlik cezalandırılır.
    """)
