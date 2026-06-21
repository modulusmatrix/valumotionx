import streamlit as st
from core import valumotion_hesapla

st.set_page_config(page_title="Valumotion", page_icon="🌟", layout="wide")

st.title("🌟 Valumotion")
st.subheader("Yer Değiştirme ve Birleşme Teorisi")
st.markdown("**İnsanlığın Yaşam Döngüsünü Keşfedin** - Bayram Gedikli")

st.markdown("---")

kullanici_metin = st.text_area(
    "Kararınızı, Eyleminizi veya Durumunuzu Detaylı Yazın",
    placeholder="Örnek: Ailemle İstanbul'a taşınıp yeni bir iş kurmak istiyorum. Hem maddi durumumuz iyileşecek, hem çocuklarımızın eğitimi daha iyi olacak, hem de manevi huzur bulacağız...",
    height=200
)

mod = st.selectbox("Mod Seçiniz", ["Birey", "Toplum", "Proje", "Eğitim", "Aile", "Ekonomi", "Hukuk", "Diğer"])
zaman_s = st.slider("Zaman Etkisi (Yıl cinsinden - S-Z farkı)", min_value=1, max_value=100, value=10)

if st.button("🚀 Boyutları Analiz Et ve Değeri Hesapla", type="primary") and kullanici_metin.strip():
    with st.spinner("Teori boyutları analiz ediliyor..."):
        metin = kullanici_metin.lower()
        
        # Boyut Analizleri (Kitaba Sadık)
        maddi = "Maddi Boyut: "
        if any(k in metin for k in ['para', 'iş', 'şirket', 'yatırım', 'maaş', 'ev', 'araba', 'kar', 'zengin', 'ekonomi']):
            maddi += "**Güçlü** (+0.8) - Maddi kazanç ve kaynak artışı bekleniyor."
        else:
            maddi += "**Orta/Zayıf** (0.0) - Maddi boyut geliştirilmeli."
        
        manevi = "Manevi Boyut: "
        if any(k in metin for k in ['allah', 'mutlu', 'huzur', 'aile', 'sevap', 'iman', 'geliş', 'öğren', 'hayırlı']):
            manevi += "**Güçlü** (+0.85) - Ruhsal ve anlam katmanı yüksek."
        else:
            manevi += "**Zayıf** (-0.2) - Manevi boyut eksik kalabilir."
        
        dis_boyut = "Dış Boyut: "
        if any(k in metin for k in ['toplum', 'aile', 'şehir', 'ülke', 'insan', 'çevre', 'göç', 'topluma']):
            dis_boyut += "**Olumlu** (+0.7) - Dış etki ve toplumsal uyum iyi."
        else:
            dis_boyut += "**Sınırlı** (+0.2) - Dış boyut etkisi düşük."
        
        # X Boyutu (Uygulama Alanı)
        x_alan = mod if mod != "Diğer" else "Kişisel/Gelişim"
        x_puan = 0.75
        
        # Yer Değiştirme Puanı
        yd_puan = (0.8 + 0.85 + 0.7 + x_puan) / 4   # Ortalama
        if any(k in metin for k in ['yeni', 'değiş', 'kur', 'başla', 'taşın', 'ilerle']):
            yd_puan += 0.25
        if any(k in metin for k in ['kork', 'risk', 'zor', 'kaybet', 'kaçın']):
            yd_puan -= 0.45
        
        birlesme_puan = 0.78  # Birleşme gücü (kitaba göre zorunlu)
        
        # Hesaplama
        sonuc = valumotion_hesapla(
            zaman_s=zaman_s,
            yer_degismeler=[yd_puan],
            birlesmeler=[birlesme_puan],
            mod=mod.lower(),
            aciklama=kullanici_metin[:300]
        )
        
        # Sonuçlar
        st.subheader("📊 Boyut Analizi")
        col1, col2 = st.columns(2)
        with col1:
            st.info(maddi)
            st.info(manevi)
        with col2:
            st.info(dis_boyut)
            st.info(f"**X Boyutu ({x_alan}):** +{x_puan:.2f} - Uygulama alanı uygun.")
            st.info(f"**Zaman Boyutu:** +{zaman_s} yıl etki")
        
        st.success(f"**Nihai Değer Skoru: {sonuc['deger_skoru']}**")
        st.markdown(f"**Genel Durum:** {sonuc['durum']}")
        
        if sonuc['deger_skoru'] > 50:
            st.balloons()
            st.success("🌟 **Güçlü Artı Değer** - Bu yer değiştirme ve birleşme maksimum kazanç potansiyeli taşıyor.")
        elif sonuc['deger_skoru'] > 15:
            st.warning("⚠️ **Orta Seviye** - Bazı boyutlar güçlendirilmeli.")
        else:
            st.error("❌ **Eksi Değer Riski** - Bu karar değer kaybettirebilir. Farklı bir yol düşünün.")

else:
    if st.button("🚀 Boyutları Analiz Et ve Değeri Hesapla", type="primary"):
        st.warning("Lütfen bir karar veya eylem yazınız.")

st.markdown("---")
st.caption("Valumotion v0.4 • Yer Değiştirme ve Birleşme Teorisi • Bayram Gedikli")
