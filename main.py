import streamlit as st
from core import valumotion_hesapla

st.set_page_config(page_title="Valumotion", page_icon="🌍", layout="centered")

st.title("🌟 Valumotion")
st.subheader("Yer Değiştirme ve Birleşme Teorisi AI")
st.markdown("**DÜNYA İÇİN YENİ BİR ANLAM**")

st.markdown("---")

# Mod seçimi
mod = st.selectbox(
    "Hangi modda hesaplama yapmak istiyorsun?",
    ["Birey", "Toplum", "Proje", "Karar"],
    index=0
)

mod_lower = mod.lower()

# Zaman girişi
zaman_s = st.slider("Zaman Etkisi (Gelecekteki Etki Süresi)", 
                   min_value=1, max_value=100, value=10, 
                   help="Ne kadar uzun vadeli düşünüyorsun?")

# Yer Değiştirmeler
st.markdown("### Yer Değiştirmeler (Doğru/Yanlış)")
yd1 = st.slider("1. Yer Değiştirme Etkisi", -1.0, 1.0, 0.8, 0.1)
yd2 = st.slider("2. Yer Değiştirme Etkisi", -1.0, 1.0, 0.6, 0.1)
yd3 = st.slider("3. Yer Değiştirme Etkisi (Opsiyonel)", -1.0, 1.0, 0.0, 0.1)

yer_degismeler = [yd1, yd2, yd3]

# Birleşmeler
st.markdown("### Birleşmeler")
b1 = st.slider("1. Birleşme Gücü", 0.0, 1.0, 0.7, 0.1)
b2 = st.slider("2. Birleşme Gücü (Opsiyonel)", 0.0, 1.0, 0.0, 0.1)

birlesmeler = [b1, b2] if b2 > 0 else [b1]

# Açıklama
aciklama = st.text_area("Karar / Durum / Eylem Açıklaması (Opsiyonel)", 
                       placeholder="Örnek: Yeni işe başlamak, evlenmek, şirket kurmak...")

# Hesapla butonu
if st.button("🚀 Değeri Hesapla", type="primary"):
    sonuc = valumotion_hesapla(
        zaman_s=zaman_s,
        yer_degismeler=yer_degismeler,
        birlesmeler=birlesmeler,
        mod=mod_lower,
        aciklama=aciklama
    )
    
    st.success(f"**Sonuç: {sonuc['deger_skoru']}**")
    st.markdown(f"**Durum:** {sonuc['durum']}")
    st.markdown(f"**Mod:** {sonuc['mod']}")
    st.markdown(f"**Tarih:** {sonuc['tarih']}")
    
    if sonuc['aciklama']:
        st.info(f"**Açıklama:** {sonuc['aciklama']}")
    
    # Basit yorum
    if sonuc['deger_skoru'] > 50:
        st.balloons()
        st.success("🎉 Çok güçlü bir yer değiştirme! Allah'ın izniyle büyük değer ortaya çıkacak.")
    elif sonuc['deger_skoru'] > 0:
        st.success("✅ Olumlu yönde ilerliyor.")
    else:
        st.error("⚠️ Bu yer değiştirme değer kaybettirebilir. Tekrar değerlendirmeni öneririm.")

st.markdown("---")
st.caption("Valumotion v0.1 • Yer Değiştirme ve Birleşme Teorisi")
