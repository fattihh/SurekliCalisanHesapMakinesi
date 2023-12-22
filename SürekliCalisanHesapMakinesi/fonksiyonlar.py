import math

def topla():
    sayi1 = None  # İlk sayıyı tanımlamak için bir başlangıç değeri atanır
    while True:
        try:
            if sayi1 is None:
                sayi1 = float(input("Toplanacak birinci sayiyi giriniz: "))
            else:
                sayi2 = float(input("Toplanacak ikinci sayiyi giriniz: "))
                return sayi1 + sayi2
        except ValueError:
            print("Hatali giris. Lutfen geçerli formatta sayilari giriniz.")

def cikar():
    sayi1 = None
    while True:
        try:
            if sayi1 is None:
                sayi1 = float(input("Cikarilacak birinci sayiyi giriniz: "))
            else:
                sayi2 = float(input("Cikarilacak ikinci sayiyi giriniz: "))
                return sayi1 - sayi2
        except ValueError:
            print("Hatali giris. Lutfen geçerli formatta sayilari giriniz.")

def carpma():
    sayi1 = None
    while True:
        try:
            if sayi1 is None:
                sayi1 = float(input("Carpilacak birinci sayiyi giriniz: "))
            else:
                sayi2 = float(input("Carpilacak ikinci sayiyi giriniz: "))
                return sayi1 * sayi2
        except ValueError:
            print("Hatali giris. Lutfen geçerli formatta sayilari giriniz.")

def bolme():
    sayi1 = None
    while True:
        try:
            if sayi1 is None:
                sayi1 = float(input("Bölünecek sayiyi giriniz: "))
            else:
                sayi2 = float(input("Bölmeyi giriniz: "))
                return sayi1 / sayi2
        except ValueError:
            print("Hatali giris. Lutfen geçerli formatta sayilari giriniz.")
        except ZeroDivisionError:
            print("Sifira bölme hatasi")

def modAlma():
    sayi1 = None
    while True:
        try:
            if sayi1 is None:
                sayi1 = float(input("Modu alinacak sayiyi giriniz: "))
            else:
                sayi2 = int(input("Modu giriniz: "))
                return math.fmod(sayi1 , sayi2)
        except ValueError:
            print("Hatali giris. Lutfen geçerli formatta sayilari giriniz.")

def faktoriyel():
    while True:
        try:
            sayi1 = int(input("Faktöriyeli alinacak sayiyi giriniz: "))
            return math.factorial(sayi1)
        except ValueError :
            print(f"Hatalı giriş.")
        except OverflowError:
            print("Hesaplama sırasında bir taşma hatası oluştu. Lütfen daha küçük bir sayı girin.")

def logaritma():
    sayi1 = None
    while True:
        try:
            if sayi1 is None:
                sayi1 = float(input("Logaritmanın gövdesini giriniz : "))
            elif sayi1==0:
                print("Hatali giris. Lutfen geçerli formatta sayilari giriniz.")
                sayi1 = float(input("Logaritmanın gövdesini giriniz : "))
            elif sayi1==1:
                return  0
            else:
                sayi2 = int(input("Logaritmanın tabanını giriniz giriniz : "))
                return math.log(sayi1,sayi2)
        except ValueError:
            print("Hatali giris. Lutfen geçerli formatta sayilari giriniz.")








