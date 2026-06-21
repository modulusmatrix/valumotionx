import numpy as np
from datetime import datetime

def valumotion_hesapla(zaman_s=1, yer_degismeler=None, birlesmeler=None, mod="birey", aciklama=""):
    if yer_degismeler is None:
        yer_degismeler = [0.0]
    if birlesmeler is None:
        birlesmeler = [0.0]
    
    net_yd = sum(yer_degismeler)
    net_birlesme = np.prod([1 + b for b in birlesmeler]) if birlesmeler else 1.0
    zaman_carpani = zaman_s
    
    deger = zaman_carpani * (net_yd * net_birlesme)
    
    mod_katsayi = {"birey": 1.0, "toplum": 1.8, "proje": 1.4, "karar": 1.2}
    deger = deger * mod_katsayi.get(mod, 1.0)
    
    durum = "✅ Maksimum Değer Kazancı" if deger > 0 else "❌ Değer Kaybı"
    
    return {
        "deger_skoru": round(deger, 2),
        "durum": durum,
        "mod": mod.capitalize(),
        "tarih": datetime.now().strftime("%d.%m.%Y %H:%M"),
        "aciklama": aciklama
    }
