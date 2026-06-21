import streamlit as st
from core import valumotion_hesapla
from datetime import datetime

st.set_page_config(page_title="Valumotion", page_icon="⚡", layout="centered")

st.markdown("""
<style>
    .big-font {font-size: 52px !important; font-weight: bold; color: #1E88E5;}
    .subtitle {font-size: 22px; color: #424242;}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">VALUMOTION</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Yer Değiştirme ve Birleşme Teorisi • Canlı AI Analiz</p>', unsafe_allow_html=True)

st.markdown("---")

kullanici_metin = st.text_area(
    "Kararınızı veya Eyleminizi Detaylı Anlatın",
    placeholder="Örnek: Ailemi alarak helal bir kazanç için yeni bir şehre taşınmak istiyorum. Çocuklarımın geleceğini düşünerek daha iyi bir ortam sağlamak istiyorum...",
    height=160
)

col1, col2 = st.columns([3, 2])
with col1:
    mod = st.selectbox("Mod", ["Birey", "Aile", "Ekonomi", "Eğitim", "Toplum", "Proje"])
with col2:
    zaman_s = st.slider("Zaman Etkisi (Yıl)", 1, 100, 12)

if st.button("⚡ CANLI ANALİZ BAŞLAT", type="primary", use_container_width=True) and kullanici_metin.strip():
    with st.spinner("Yapay Zeka + Teori Analizi Yapılıyor..."):
        
        # Gelişmiş AI Benzeri Analiz
        metin = kullanici_metin.lower()
        
        # Skor hesaplama
        olumlu = len([w for w in ['helal','hayırlı','hicret','aile','huzur','allah','sevap','bereket','doğru','geliş'] if w in metin])
        olumsuz = len([w for w in ['haram','korku','kaybet','zulüm','yanlış','tehlike'] if w in metin])
        
        yd_puan = 0.6 + (olumlu * 0.22) - (olumsuz * 0.28)
        yd_puan = max(0.1, min(1.0, yd_puan))
        
        sonuc = valumotion_hesapla(
            zaman_s=zaman_s,
            yer_degismeler=[yd_puan],
            birlesmeler=[0.82],
            mod=mod.lower()
        )
        
        # Canlı Sonuç
        st.success(f"**NİHAİ DEĞER SKORU: {sonuc['deger_skoru']}**")
        
        progress = min(100, int(sonuc['deger_skoru'] * 2))
        st.progress(progress)
        
        st.markdown(f"**Durum:** {sonuc['durum']}")
        
        # Dinamik ve Canlı Yorum
        st.markdown("### 🧠 Yapay Zeka + Teori Yorumu")
        
        if sonuc['deger_skoru'] > 55:
            st.success("🔥 **Çok Güçlü Bir Yer Değiştirme!**  \nBu adım, hem dünya hem ahiret için yüksek değer üretebilir. Allah bereket versin.")
        elif sonuc['deger_skoru'] > 35:
            st.info("✅ **Olumlu ve Potansiyelli**  \nDoğru yöndesiniz. Niyetinizi ve uygulamayı güçlendirirseniz daha yüksek değere ulaşabilirsiniz.")
        elif sonuc['deger_skoru'] > 15:
            st.warning("⚠️ **Orta Seviye**  \nKararınız risk taşıyor. Bazı yönleri gözden geçirmenizi öneririm.")
        else:
            st.error("❌ **Dikkat! Değer Kaybı Riski Yüksek**  \nBu yer değiştirme şu an için uygun görünmüyor. Daha hayırlı alternatifler düşünün.")
        
        st.caption(f"Analiz Tarihi: {datetime.now().strftime('%d.%m.%Y %H:%M')} • Valumotion AI")

st.markdown("---")
st.markdown("**Valumotion** — Yer Değiştirme ve Birleşme Teorisi Canlı AI")
