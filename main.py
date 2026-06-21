import streamlit as st
from core import valumotion_hesapla
from datetime import datetime

st.set_page_config(page_title="Valumotion", page_icon="📜", layout="centered")

# Roman Sayfası Tonu + Logo Uyumlu CSS
st.markdown("""
<style>
    .main {
        background-color: #FAF0D9;
        color: #3C2F2F;
    }
    .big-title {
        font-size: 55px;
        font-weight: bold;
        color: #8B4513;
        text-align: center;
        margin-bottom: 5px;
    }
    .subtitle {
        font-size: 21px;
        color: #5C4033;
        text-align: center;
        font-style: italic;
    }
    .stButton>button {
        background: linear-gradient(90deg, #8B4513, #D4A017);
        color: white;
        font-weight: bold;
        height: 55px;
        font-size: 18px;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #A0522D, #E8B923);
    }
</style>
""", unsafe_allow_html=True)

# Logo Ekleme
st.image("https://i.ibb.co/8XzYkLq/valumotion-logo.png", width=280)  # Geçici link (istediğin logo linkini koyabilirsin)

st.markdown('<p class="big-title">VALUMOTION</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Yer Değiştirme ve Birleşme Teorisi</p>', unsafe_allow_html=True)
st.caption("THE GLOBAL VALUE CREATION PLATFORM")

st.markdown("---")

kullanici_metin = st.text_area(
    "Kararınızı veya Eyleminizi Yazın",
    placeholder="Örnek: Ailemi alarak helal kazanç için yeni bir şehre taşınmak ve huzurlu bir hayat kurmak istiyorum...",
    height=160
)

col1, col2 = st.columns([3, 2])
with col1:
    mod = st.selectbox("Mod", ["Birey", "Aile", "Ekonomi", "Eğitim", "Toplum", "Proje"])
with col2:
    zaman_s = st.slider("Zaman Etkisi (Yıl)", 1, 100, 12)

if st.button("📜 ANALİZİ BAŞLAT", type="primary", use_container_width=True) and kullanici_metin.strip():
    with st.spinner("Teori ve Yapay Zeka Analizi Yapılıyor..."):
        
        metin = kullanici_metin.lower()
        olumlu = len([w for w in ['helal','hayırlı','huzur','allah','sevap','bereket','aile','geliş'] if w in metin])
        olumsuz = len([w for w in ['haram','korku','kaybet','zulüm','yanlış'] if w in metin])
        
        yd_puan = 0.65 + (olumlu * 0.2) - (olumsuz * 0.25)
        yd_puan = max(0.1, min(1.0, yd_puan))
        
        sonuc = valumotion_hesapla(
            zaman_s=zaman_s,
            yer_degismeler=[yd_puan],
            birlesmeler=[0.82],
            mod=mod.lower()
        )
        
        st.success(f"**NİHAİ DEĞER SKORU: {sonuc['deger_skoru']}**")
        st.progress(min(100, int(sonuc['deger_skoru'] * 2)))
        
        st.markdown(f"**Durum:** {sonuc['durum']}")
        
        st.markdown("### 📜 Teori ve Yapay Zeka Yorumu")
        if sonuc['deger_skoru'] > 55:
            st.success("🔥 Bu yer değiştirme çok güçlü bir potansiyele sahip. Hayırlı olsun.")
        elif sonuc['deger_skoru'] > 35:
            st.info("✅ Olumlu bir adım. Niyet ve uygulama ile daha da güçlenebilir.")
        elif sonuc['deger_skoru'] > 15:
            st.warning("⚠️ Orta seviyede. Kararı gözden geçirmekte fayda var.")
        else:
            st.error("❌ Bu karar değer kaybettirebilir. Daha hayırlı bir yol arayın.")

        st.caption(f"Analiz Tarihi: {datetime.now().strftime('%d.%m.%Y %H:%M')}")

st.markdown("---")
st.markdown("**Valumotion** • Yer Değiştirme ve Birleşme Teorisi AI")
