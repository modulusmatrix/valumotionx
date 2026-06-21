def valumotion_hesapla(zaman_s: float, maddi: float, manevi: float, 
                      dis_boyut: float, x_puan: float, mod: str = "birey"):
    
    # Input validation
    if zaman_s <= 0:
        raise ValueError("Zaman pozitif olmalı")
    for val, name in [(maddi,"maddi"), (manevi,"manevi"), (dis_boyut,"dis_boyut"), (x_puan,"x_puan")]:
        if not 0 <= val <= 1:
            raise ValueError(f"{name} 0-1 arasında olmalı")
    
    # Yer Değiştirme Skoru - Aritmetik ortalama
    yd = (maddi + manevi + dis_boyut + x_puan) / 4
    
    # Birleşme Skoru - Geometrik ortalama = Çarpımsal etki
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
    deger = deger * mod_katsayi.get(mod.lower(), 1.0)
    
    # Durum belirleme - Eşik değeri dinamik yapalım
    esik = 10 * mod_katsayi.get(mod.lower(), 1.0)  # Moda göre değişir
    durum = "✅ Maksimum Değer Kazancı" if deger > esik else "⚠️ Değer Kaybı Riski"
    
    return {
        "deger_skoru": round(deger, 2),
        "durum": durum,
        "aciklama": f"{mod.capitalize()} modunda {zaman_s}s için hesaplandı",
        "yer_degistirme": round(yd, 3),
        "birlesme": round(birlesme, 3),
        "mod_katsayisi": mod_katsayi.get(mod.lower(), 1.0),
        "ham_skor": round(zaman_s * (yd * birlesme), 2),  # Katsayısız skor
        "bileşenler": {
            "maddi": maddi,
            "manevi": manevi, 
            "dis_boyut": dis_boyut,
            "x_puan": x_puan
        }
    }
