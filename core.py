import streamlit as st
from core import valumotion_hesapla
from datetime import datetime

st.set_page_config(page_title="Valumotion", page_icon="📜", layout="centered")

st.markdown("""
<style>
    .main {background-color: #F5E8C7; color: #3C2F2F;}
    .big-title {font-size: 58px; font-weight: bold; color: #8B4513; text-align: center;}
    .subtitle {font-size: 22px; color: #5C4033; text-align: center; font-style: italic;}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-title">VALUMOTION</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Yer Değiştirme ve Birleşme Teorisi Simülasyonu</p>', unsafe_allow_html=True)

st.markdown("---")

kullanici_metin = st.text_area("Kararınızı veya Eyleminizi Yazın", height=140,
    placeholder="Örnek: Ailemi helal kazanç için yeni bir şehre taşımak istiyorum...")

mod = st.selectbox("Mod", ["Birey", "Aile", "Ekonomi", "Eğitim", "Toplum"])
zaman_s = st.slider("Zaman Etkisi (Yıl)", 1, 100, 10)

if st.button("📜 SİMÜLASYONU BAŞLAT", type="primary", use_container_width=True) and kullanici_metin:
    with st.spinner("Formül Simülasyonu Çalışıyor..."):
        metin = kullanici_metin.lower()
        
        # Boyut Skorları (Yapay Zeka Destekli)
        maddi = 0.85 if any(w in metin for w in ['para','iş','kazanç','yatırım','ekonomi']) else 0.55
        manevi = 0.9 if any(w in metin for w in ['allah','huzur','helal','sevap','hayırlı','aile']) else 0.5
        dis_boyut = 0.8 if any(w in metin for w in ['toplum','aile','şehir','ülke','insan']) else 0.6
        x_puan = 0.75
        
        sonuc = valumotion_hesapla(zaman_s, maddi, manevi, dis_boyut, x_puan, mod.lower())
        
        # Sonuçlar
        st.subheader("📊 SİMÜLASYON SONUÇLARI")
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Maddi Boyut", f"{sonuc['maddi']}")
        col2.metric("Manevi Boyut", f"{sonuc['manevi']}")
        col3.metric("Dış Boyut", f"{sonuc['dis_boyut']}")
        col4.metric("X (Alan)", "0.75")
        
        st.markdown(f"**Yer Değiştirme Skoru:** `{sonuc['yer_degistirme']}`")
        st.markdown(f"**Birleşme Skoru:** `{sonuc['birlesme']}`")
        
        st.success(f"**NİHAİ DEĞER SKORU: {sonuc['deger_skoru']}**")
        st.progress(min(100, int(sonuc['deger_skoru'] * 1.5)))
        
        st.markdown(f"**Genel Durum:** {sonuc['durum']}")

        st.caption(f"Simülasyon Tarihi: {datetime.now().strftime('%d.%m.%Y %H:%M')}")

st.markdown("---")
st.caption("Valumotion • Yer Değiştirme ve Birleşme Teorisi Simülasyonu")
