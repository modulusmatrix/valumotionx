import streamlit as st
from core import valumotion_hesapla
import re

st.set_page_config(page_title="Valumotion", page_icon="🌍", layout="centered")

st.title("🌟 Valumotion")
st.subheader("Yer Değiştirme ve Birleşme Teorisi")
st.markdown("**DÜNYA İÇİN YENİ BİR ANLAM**")

st.markdown("---")

# Kullanıcı girdisi
st.markdown("### Kararını, Eylemini veya Durumunu Yaz")
kullanici_metin = st.text_area(
    "Ne yapmak istiyorsun? Hangi kararı vereceksin?",
    placeholder="Örnek: Ankara'da yeni bir iş kurmak istiyorum, 2 yıl sonra kendi şirketimi açacağım...",
    height=150
)

mod = st.selectbox("Mod Seç", ["Birey", "Toplum", "Proje", "Karar"], index=0)
mod_lower = mod.lower()

zaman_s = st.slider("Zaman Etkisi (Yıl cinsinden)", min_value=1, max_value=50, value=5)

if st.button("🚀 Değeri Hesapla", type="primary") and kullanici_metin.strip():
    with st.spinner("Teori analiz ediliyor..."):
        
        # Basit AI Analizi (Kelime ve Duygu Analizi)
        metin = kullanici_metin.lower()
        
        # Maddi puan
        maddi_kelimeler = ['para', 'iş', 'şirket', 'yatırım', 'ev', 'araba', 'maaş', 'kar', 'zarar']
        maddi_puan = sum(1 for kelime in maddi_kelimeler if kelime in metin) * 0.25
        
        # Manevi puan
        manevi_kelimeler = ['mutlu', 'huzur', 'allah', 'iman', 'sevap', 'aile', 'evlilik', 'öğrenmek']
        manevi_puan = sum(1 for kelime in manevi_kelimeler if kelime in metin) * 0.3
        
        # Dış boyut (sosyal, çevre)
        dis_kelimeler = ['toplum', 'ülke', 'insan', 'aile', 'arkadaş', 'şehir', 'göç']
        dis_puan = sum(1 for kelime in dis_kelimeler if kelime in metin) * 0.25
        
        # Yer değiştirme puanı (olumlu - olumsuz)
        olumlu = len(re.findall(r'\b(başar|iyi|güzel|doğru|ilerle|kazanç|mutlu)\b', metin))
        olumsuz = len(re.findall(r'\b(kötü|zor|risk|korku|kaybet|yanlış|zorluk)\b', metin))
        yd_puan = (olumlu - olumsuz) * 0.4
        
        yer_degismeler = [yd_puan, maddi_puan + manevi_puan + dis_puan]
        birlesmeler = [0.6, 0.4]  # Varsayılan birleşme gücü

        # Hesaplama
        sonuc = valumotion_hesapla(
            zaman_s=zaman_s,
            yer_degismeler=yer_degismeler,
            birlesmeler=birlesmeler,
            mod=mod_lower,
            aciklama=kullanici_metin[:200]
        )
        
        # Sonuç Gösterimi
        st.success(f"**Değer Skoru: {sonuc['deger_skoru']}**")
        st.markdown(f"**Durum:** {sonuc['durum']}")
        st.markdown(f"**Mod:** {sonuc['mod']}")
        st.markdown(f"**Zaman Etkisi:** {zaman_s} yıl")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Maddi Etki", f"{maddi_puan:.2f}")
        with col2:
            st.metric("Manevi Etki", f"{manevi_puan:.2f}")
        with col3:
            st.metric("Dış Boyut", f"{dis_puan:.2f}")
        
        if sonuc['deger_skoru'] > 30:
            st.balloons()
            st.success("🌟 Bu yer değiştirme güçlü bir değer üretebilir.")
        elif sonuc['deger_skoru'] > 0:
            st.info("✅ Olumlu ancak geliştirilebilir.")
        else:
            st.error("⚠️ Bu karar değer kaybettirebilir. Tekrar düşünmeni öneririm.")

else:
    if st.button("🚀 Değeri Hesapla", type="primary"):
        st.warning("Lütfen bir karar veya eylem yazın.")

st.markdown("---")
st.caption("Valumotion v0.2 • Yer Değiştirme ve Birleşme Teorisi AI")
