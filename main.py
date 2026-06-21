import streamlit as st
from core import valumotion_hesapla

st.set_page_config(page_title="Valumotion", page_icon="🌟", layout="centered")

st.title("🌟 Valumotion")
st.markdown("**Yer Değiştirme ve Birleşme Teorisi**")
st.caption("Bayram Gedikli")

st.markdown("---")

kullanici_metin = st.text_area(
    "Kararınızı veya Eyleminizi Yazın",
    placeholder="Örnek: Ailemle birlikte başka bir şehre taşınıp kendi işimi kurmak istiyorum...",
    height=140
)

mod = st.selectbox("Mod", ["Birey", "Toplum", "Proje", "Eğitim", "Aile", "Ekonomi", "Diğer"], index=0)
zaman_s = st.slider("Zaman Etkisi (Yıl)", 1, 50, 8)

if st.button("🚀 Analiz Et", type="primary", use_container_width=True) and kullanici_metin:
    with st.spinner("Teori ve Yapay Zeka Analizi Yapılıyor..."):
        
        metin = kullanici_metin.lower()
        
        # Daha Akıllı Boyut Puanlaması
        maddi_puan = 0.75 if any(w in metin for w in ['para','iş','şirket','yatırım','maaş','kar']) else 0.3
        manevi_puan = 0.85 if any(w in metin for w in ['allah','mutlu','huzur','aile','sevap','iman']) else 0.4
        dis_puan = 0.7 if any(w in metin for w in ['toplum','aile','ülke','insan','çevre']) else 0.35
        
        yd_puan = (maddi_puan + manevi_puan + dis_puan) / 3
        # Ekstra zeka
        if any(w in metin for w in ['yeni','değiş','kur','başla','geliştir']):
            yd_puan += 0.3
        if any(w in metin for w in ['kork','risk','zor','kaybet']):
            yd_puan -= 0.35
        
        sonuc = valumotion_hesapla(
            zaman_s=zaman_s,
            yer_degismeler=[yd_puan],
            birlesmeler=[0.75],
            mod=mod.lower(),
            aciklama=kullanici_metin
        )
        
        # Temiz Sonuç
        st.subheader("📊 Analiz Sonucu")
        
        st.success(f"**Nihai Değer Skoru: {sonuc['deger_skoru']}**")
        st.markdown(f"**Durum:** {sonuc['durum']}")
        
        st.markdown("### Boyut Değerlendirmesi")
        cols = st.columns(3)
        cols[0].metric("Maddi Boyut", f"{maddi_puan:.2f}")
        cols[1].metric("Manevi Boyut", f"{manevi_puan:.2f}")
        cols[2].metric("Dış Boyut", f"{dis_puan:.2f}")
        
        st.info(f"**X Alanı ({mod}):** {yd_puan:.2f} → Yer Değiştirme Gücü")
        st.info(f"**Zaman Etkisi:** {zaman_s} yıl")
        
        # Öneri
        if sonuc['deger_skoru'] > 45:
            st.success("🌟 Bu yer değiştirme güçlü bir değer üretebilir. Hayırlı olsun.")
        elif sonuc['deger_skoru'] > 15:
            st.warning("⚠️ Olumlu ancak bazı boyutlar güçlendirilmeli.")
        else:
            st.error("❌ Dikkat: Bu karar değer kaybettirebilir.")

st.markdown("---")
st.caption("Valumotion v0.5 • Daha Temiz ve Akıllı Versiyon")
