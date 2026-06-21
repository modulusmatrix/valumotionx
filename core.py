def valumotion_hesapla(zaman_s: float, maddi: float, manevi: float, 
                      dis_boyut: float, x_puan: float, mod: str = "birey"):
    # Input validation
    for val, name in [(maddi,"maddi"), (manevi,"manevi"), (dis_boyut,"dis_boyut"), (x_puan,"x_puan")]:
        if not 0 <= val <= 1:
            raise ValueError(f"{name} 0-1 arasında olmalı")
    
    # Açıklamalı return
    return {
        "deger_skoru": round(deger, 2),
        "durum": "✅ Maksimum Değer Kazancı" if deger > 15 else "⚠️ Değer Kaybı Riski",
        "aciklama": f"{mod.capitalize()} modunda {zaman_s}s için hesaplandı",
        # ... diğerleri
    }
