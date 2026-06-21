def valumotion_hesapla(zaman_s, maddi, manevi, dis_boyut, x_puan, mod="birey"):
    if zaman_s <= 0:
        raise ValueError("Zaman pozitif olmali")
    yd = (maddi + manevi + dis_boyut + x_puan) / 4
    birlesme = (maddi * manevi * dis_boyut * x_puan) ** 0.25
    deger = zaman_s * yd * birlesme * {"birey":1.0,"aile":1.2,"ekonomi":1.15,"egitim":1.25,"toplum":1.4,"proje":1.1}.get(mod,1.0)
    return {
        "deger_skoru": round(deger,2),
        "durum": "Kazanc" if deger>10 else "Risk",
        "aciklama": "Hesaplandi",
        "yer_degistirme": round(yd,3),
        "birlesme": round(birlesme,3),
        "maddi": maddi,
        "manevi": manevi,
        "dis_boyut": dis_boyut,
        "x_puan": x_puan,
        "mod": mod,
        "mod_katsayisi": 1.0
    }
