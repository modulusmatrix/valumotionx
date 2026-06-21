import numpy as np
from datetime import datetime

def valumotion_hesapla(zaman_s=10, maddi=0.7, manevi=0.7, dis_boyut=0.6, x_puan=0.75, mod="birey"):
    """
    Yer Değiştirme ve Birleşme Teorisi Simülasyon Motoru
    """
    # Yer Değiştirme Skoru
    yd = (maddi + manevi + dis_boyut + x_puan) / 4
    
    # Birleşme Skoru (Çarpımsal etki)
    birlesme = (maddi * manevi * dis_boyut * x_puan) ** 0.25
    
    # Nihai Değer Hesabı
    deger = zaman_s * (yd * birlesme)
    
    # Mod katsayısı
    mod_katsayi = {
        "birey": 1.0, 
        "aile": 1.2, 
        "ekonomi": 1.15, 
        "egitim": 1.25, 
        "toplum": 1.4, 
        "proje": 1.1
    }
    
    deger = deger * mod_katsayi.get(mod, 1.0)
    
    return {
        "deger_skoru": round(deger, 2),
        "durum": "✅ Maksimum Değer Kazancı" if deger > 15 else "⚠️ Değer Kaybı Riski",
        "yer_degistirme": round(yd, 2),
        "birlesme": round(birlesme, 2),
        "maddi": round(maddi, 2),
        "manevi": round(manevi, 2),
        "dis_boyut": round(dis_boyut, 2),
        "mod": mod.capitalize()
    }
