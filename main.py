import streamlit as st
from core import valumotion_hesapla
from datetime import datetime

st.set_page_config(page_title="Valumotion", page_icon="🌟", layout="centered")

# Logo Tonlarına Özel CSS
st.markdown("""
<style>
    .main {
        background-color: #0A1428;
        color: #E0E0E0;
    }
    .big-title {
        font-size: 58px;
        font-weight: bold;
        background: linear-gradient(90deg, #FFD700, #C0C0C0, #FFD700);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0;
    }
    .subtitle {
        font-size: 20px;
        color: #A8B0C0;
        text-align: center;
        margin-top: 0;
    }
    .stButton>button {
        background: linear-gradient(90deg, #FFD700, #B8860B);
        color: #0A1428;
        font-weight: bold;
        border: none;
        height: 52px;
        font-size: 18px;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #FFEA80, #E6B800);
        transform: scale(1.03);
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-title">VALUMOTION</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">YER DEĞİŞTİRME VE BİRLEŞME TEORİSİ</p>', unsafe_allow_html=True)
st.caption("THE GLOBAL VALUE CREATION PLATFORM")

st.markdown("---")

kullanici_metin = st.text_area(
    "Kararınızı veya Eyleminizi Yazın",
    placeholder="Örnek: Ailemi helal kazanç için yeni bir şehre taşımak ve daha huzurlu bir hayat kurmak istiyorum...",
    height=160
)

col1, col2 = st.columns([3, 2])
with col1:
    mod = st.selectbox("Mod", ["Birey", "Aile", "Ekonomi", "Eğitim", "Toplum", "Proje"])
with col2:
    zaman_s = st.slider("Zaman Etkisi (Yıl)", 1, 100, 12)

if st.button("⚡ ANALİZİ BAŞLAT", type="primary", use_container_width=True) and kullanici_metin.strip():
    with st.spinner("Yapay Zeka Analizi Devam Ediyor..."):
        
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
        
        st.markdown("### 🧠 Yapay Zeka Yorumu")
        if sonuc['deger_skoru'] > 55:
            st.success("🔥 Bu yer değiştirme çok güçlü bir değer potansiyeli taşıyor. Allah bereket versin.")
        elif sonuc['deger_skoru'] > 35:
            st.info("✅ Olumlu ve anlamlı bir adım. Uygulamada niyet ve sebat çok önemli.")
        elif sonuc['deger_skoru'] > 15:
            st.warning("⚠️ Orta seviyede. Bazı yönleri gözden geçirmenizi öneririm.")
        else:
            st.error("❌ Bu karar şu an için değer kaybettirebilir. Daha hayırlı bir yol arayın.")

        st.caption(f"Analiz Tarihi: {datetime.now().strftime('%d.%m.%Y %H:%M')}")

st.markdown("---")
st.markdown("**Valumotion** • Yer Değiştirme ve Birleşme Teorisi AI")
