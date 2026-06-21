import streamlit as st
from core import valumotion_hesapla
from datetime import datetime

st.set_page_config(page_title="Valumotion", page_icon="🌟", layout="centered")

st.title("🌟 VALUMOTION")
st.markdown("**Değer Analiz Merkezi**")
st.caption("Yer Değiştirme ve Birleşme Teorisi")

st.markdown("---")

st.markdown("""
> **“İnsan sadece yer değiştirme ve birleşme yapar, değeri Allah yaratır.”**  
> YBT — Bayram Gedikli
""")

kullanici_metin = st.text_area(
    "Kararınızı veya Eyleminizi Yazın",
    placeholder="Örnek: Ailemi alıp helal bir kazanç için yeni bir şehre hicret etmek istiyorum...",
    height=150
)

col1, col2 = st.columns(2)
with col1:
    mod = st.selectbox("Mod", ["Birey", "Aile", "Ekonomi", "Eğitim", "Toplum"])
with col2:
    zaman_s = st.slider("Zaman Etkisi (Yıl)", 1, 50, 10)

if st.button("🚀 ANALİZİ BAŞLAT", type="primary", use_container_width=True) and kullanici_metin.strip():
    with st.spinner("Hakikat filtresi çalışıyor..."):
        metin = kullanici_metin.lower()
        
        yd_puan = 0.65
        if any(w in metin for w in ['helal','hayırlı','hicret','aile','huzur','allah','sevap']):
            yd_puan += 0.35
        if any(w in metin for w in ['haram','zulüm','korku','kaybet']):
            yd_puan -= 0.4
        
        sonuc = valumotion_hesapla(
            zaman_s=zaman_s,
            yer_degismeler=[yd_puan],
            birlesmeler=[0.8],
            mod=mod.lower()
        )
        
        st.success(f"**Nihai Değer Skoru: {sonuc['deger_skoru']}**")
        st.markdown(f"**Durum:** {sonuc['durum']}")
        
        st.markdown("### 📜 Hakikat Filtresi Yorumu")
        
        if sonuc['deger_skoru'] > 45:
            st.success("**Hicret ve Bereket Sertifikası**  \nBu yer değiştirme, bereket ve hayır kapılarını açabilir. Allah'ın izniyle.")
        elif sonuc['deger_skoru'] > 20:
            st.info("**Orta Değerli Yol**  \nKararınız olumlu yönde ancak niyet ve uygulama çok önemli.")
        else:
            st.error("**Dikkat Gerekli**  \nBu eylem değer kaybettirebilir. Daha hayırlı bir yer değiştirme arayın.")
        
        st.caption(f"Analiz Tarihi: {datetime.now().strftime('%d.%m.%Y %H:%M')}")

st.markdown("---")
st.markdown("**Valumotion** • Yer Değiştirme ve Birleşme Teorisi AI")
