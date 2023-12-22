import math
from fonksiyonlar import topla, cikar, carpma, bolme, modAlma, faktoriyel, logaritma

while True:
    try:
        secim = int(input("Yapacağınız işlemi seçin:\n"
                           "1-) Toplama\n"
                           "2-) Çıkarma\n"
                           "3-) Çarpma\n"
                           "4-) Bölme\n"
                           "5-) Mod Alma\n"
                           "6-) Faktöriyel bulma\n"
                           "7-) Logaritma hesaplama\n"
                           "8-) Çıkış\n"))

        if secim == 1:
            sonuc= topla()
            print(sonuc)
        elif secim == 2:
            print(cikar())
        elif secim == 3:
            print(carpma())
        elif secim == 4:
            print(bolme())
        elif secim == 5:
            print(modAlma())
        elif secim == 6:
            print(faktoriyel())
        elif secim == 7:
            print(logaritma())
        elif secim == 8:
            break
        else:
            print("Geçerli bir seçim giriniz.")
    except ValueError:
        print("Geçerli bir sayı giriniz.")
    except Exception as e:
        print(f"Hata: {e}")

