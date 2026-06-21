import numpy as np

def valumotion_hesapla(zaman_s: float, maddi: float, manevi: float, 
                      dis_boyut: float, x_puan: float, mod: str = "birey"):
    
    # Input validation
    if zaman_s <= 0:
        raise ValueError("Zaman pozitif olmalı")
    for val, name in [(maddi,"maddi"), (manevi,"manevi"), (dis_boyut,"dis_boyut"), (x_puan,"x_puan")]:
        if not 0 <= val <= 1:
            raise ValueError(f"{name} 0-1 arasinda olmali")
    
    yd = (maddi + manevi + dis_boyut + x_puan) / 4
    birlesme = (maddi * manevi * dis_boyut * x_puan) ** 0.25
    deger = zaman_s * (yd * birlesme)
    
    mod_katsayi = {
        "birey": 1.0, "aile": 1.2, "ekonomi": 1.15,
        "egitim": 1.25, "toplum": 1.4, "proje": 1.1
    }
    deger = deger * mod_katsayi.get(mod.lower(), 1.0)
    
    esik = 10 * mod_katsayi.get(mod.lower(), 1.0)
    durum = "Maksimum Deger Kazanci" if deger > esik else "Deger Kaybi Riski"
    
    return {
        "deger_skoru": round(deger, 2),
        "durum": durum,
        "aciklama": f"{mod.capitalize()} modunda {zaman_s}s icin hesaplandi",
        "yer_degistirme": round(yd, 3),
        "birlesme": round(birlesme, 3),
        "maddi": maddi,
        "manevi": manevi,
        "dis_boyut": dis_boyut,
        "x_puan": x_puan,
        "mod": mod.capitalize()
    }
