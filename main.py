import streamlit as st
from core import valumotion_hesapla

st.set_page_config(page_title="Valumotion", page_icon="🌟", layout="centered")

st.title("🌟 Valumotion")
st.markdown("**Yer Değiştirme ve Birleşme Teorisi**")
st.caption("Bayram Gedikli")

st.markdown("---")

kullanici_metin = st.text_area(
    "Kararınızı veya Eyleminizi Yazın",
    placeholder="Örnek: Yeni bir şehre taşınıp helal kazançla ailemi geçindirmek ve çocuklarıma iyi bir gelecek sağlamak istiyorum...",
    height=160
)

mod = st.selectbox("Mod", ["Birey", "Aile", "Ekonomi", "Eğitim", "Toplum", "Diğer"])
zaman_s = st.slider("Zaman Etkisi (Yıl)", min_value=1, max_value=50, value=10)

if st.button("🚀 Analiz Et ve Değeri Hesapla", type="primary", use_container_width=True) and kullanici_metin.strip():
    with st.spinner("Teori ve İslami Kaynaklara Göre Analiz Yapılıyor..."):
        
        metin = kullanici_metin.lower()
        
        # Basit ve Temiz Puanlama
        olumlu_kelimeler = ['helal', 'hayırlı', 'aile', 'huzur', 'Allah', 'sevap', 'doğru', 'geliş', 'öğren', 'yeni', 'kur']
        olumsuz_kelimeler = ['haram', 'korku', 'risk', 'kaybet', 'yanlış', 'zulüm']
        
        olumlu_skor = sum(1 for w in olumlu_kelimeler if w in metin) * 0.25
        olumsuz_skor = sum(1 for w in olumsuz_kelimeler if w in metin) * 0.3
        yd_puan = 0.65 + olumlu_skor - olumsuz_skor
        
        sonuc = valumotion_hesapla(
            zaman_s=zaman_s,
            yer_degismeler=[yd_puan],
            birlesmeler=[0.78],
            mod=mod.lower(),
            aciklama=kullanici_metin
        )
        
        # Sonuç
        st.subheader("📊 Analiz Sonucu")
        st.success(f"**Nihai Değer Skoru: {sonuc['deger_skoru']}**")
        st.markdown(f"**Durum:** {sonuc['durum']}")
        
        st.markdown("### Zaman Etkisi")
        st.info(f"Bu yer değiştirme **{zaman_s} yıl** boyunca etki edecek.")
        
        # Dini Temelli Yorum
        st.markdown("### Kur'an ve Hadis Işığında Yorum")
        
        if sonuc['deger_skoru'] > 40:
            st.success("""
            **"Kim ki Allah için bir hayır işlerse, onun için on katı vardır."** (En'âm Suresi, 160)  
            Bu karar, doğru yer değiştirme ve birleşmeye işaret ediyor. Hayırlı bir adım gibi görünüyor.
            """)
        elif sonuc['deger_skoru'] > 15:
            st.warning("""
            **"İnsan için ancak çalıştığının karşılığı vardır."** (Necm Suresi, 39)  
            Karar orta seviyede. Bazı yönlerini güçlendirmen faydalı olur.
            """)
        else:
            st.error("""
            **"Kim zerre kadar hayır işlerse onu görür, kim zerre kadar şer işlerse onu görür."** (Zilzal Suresi, 7-8)  
            Bu yer değiştirme dikkatli düşünülmeli. Daha hayırlı alternatifler araştır.
            """)
        
        st.caption("Valumotion v0.6 • Kur'an ve Hadis Temelli Yorum")

else:
    st.info("Yukarıya kararınızı detaylı yazın.")

st.markdown("---")
st.caption("Valumotion • Yer Değiştirme ve Birleşme Teorisi")
