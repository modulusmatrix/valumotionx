import streamlit as st
from core import valumotion_hesapla

st.set_page_config(page_title="Valumotion", page_icon="🌍", layout="wide")

st.title("🌟 Valumotion")
st.subheader("Yer Değiştirme ve Birleşme Teorisi")
st.markdown("**DÜNYA İÇİN YENİ BİR ANLAM**")

st.markdown("---")

kullanici_metin = st.text_area(
    "Kararını, Eylemini veya Durumunu Detaylı Yaz",
    placeholder="Örnek: Ailemle birlikte İstanbul'a taşınıp yeni bir iş kurmak istiyorum. Bu sayede hem maddi durumumuz iyileşecek hem de çocuklarımızın geleceği daha iyi olacak...",
    height=180
)

mod = st.selectbox("Mod Seç", ["Birey", "Toplum", "Proje", "Karar"])
zaman_s = st.slider("Zaman Etkisi (Yıl)", 1, 50, 5)

if st.button("🚀 Analiz Et ve Değeri Hesapla", type="primary") and kullanici_metin.strip():
    with st.spinner("Teori boyutları analiz ediliyor..."):
        
        # Basit ama etkili boyut analizi
        metin = kullanici_metin.lower()
        
        # Boyut Analizleri
        maddi = "Maddi Boyut: "
        if any(k in metin for k in ['para', 'iş', 'şirket', 'yatırım', 'maaş', 'kar', 'ev', 'araba', 'zengin']):
            maddi += "Güçlü maddi kazanç potansiyeli görülüyor. (+)"
        else:
            maddi += "Maddi boyut orta veya zayıf. Değerlendirme yapılmalı."
        
        manevi = "Manevi Boyut: "
        if any(k in metin for k in ['allah', 'mutlu', 'huzur', 'aile', 'sevap', 'iman', 'öğren', 'geliş']):
            manevi += "Manevi tatmin ve anlam yüksek. (+)"
        else:
            manevi += "Manevi boyut zayıf kalabilir."
        
        dis_boyut = "Dış Boyut: "
        if any(k in metin for k in ['toplum', 'aile', 'şehir', 'ülke', 'insan', 'göç', 'çevre', 'arkadaş']):
            dis_boyut += "Sosyal ve çevresel uyum olumlu görünüyor. (+)"
        else:
            dis_boyut += "Dış boyut etkisi sınırlı."
        
        # Yer Değiştirme Puanı (AI benzeri)
        yd_puan = 0.65
        if any(k in metin for k in ['yeni', 'değiş', 'taşın', 'kur', 'başla', 'ilerle']):
            yd_puan += 0.35
        if any(k in metin for k in ['kork', 'risk', 'zor', 'kaybet', 'kaç']):
            yd_puan -= 0.4
        
        birlesme_puan = 0.7
        
        # Hesaplama
        sonuc = valumotion_hesapla(
            zaman_s=zaman_s,
            yer_degismeler=[yd_puan, 0.8],
            birlesmeler=[birlesme_puan, 0.6],
            mod=mod.lower(),
            aciklama=kullanici_metin[:250]
        )
        
        # Sonuçları Göster
        st.success(f"**Nihai Değer Skoru: {sonuc['deger_skoru']}**")
        st.markdown(f"**Durum:** {sonuc['durum']}")
        
        st.markdown("### 📊 Boyut Analizi")
        col1, col2 = st.columns(2)
        with col1:
            st.info(maddi)
            st.info(manevi)
        with col2:
            st.info(dis_boyut)
            st.info(f"**Zaman Boyutu:** {zaman_s} yıl boyunca etki edecek.")
            st.info(f"**X Boyutu (Diğer Faktörler):** Kişisel yetenek ve irade etkisi orta-yüksek.")
        
        st.markdown("### 📌 Öneri")
        if sonuc['deger_skoru'] > 40:
            st.success("Bu yer değiştirme güçlü bir değer üretebilir. Allah'ın izniyle hayırlı olsun.")
        elif sonuc['deger_skoru'] > 10:
            st.warning("Olumlu ama bazı boyutlar güçlendirilmeli.")
        else:
            st.error("Bu eylem şu an için değer kaybettirebilir. Farklı bir yer değiştirme yolu düşün.")

else:
    st.info("Yukarıya kararını yaz ve butona bas.")

st.markdown("---")
st.caption("Valumotion v0.3 • Yer Değiştirme ve Birleşme Teorisi")
