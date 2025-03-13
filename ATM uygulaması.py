print(""" *****************
ATM uygulamasına hoşgeldiniz
İşlemler:
1-Bakiye Sorgulama
2-Para Yatırma
3-Para Çekme
Programdan çıkmak için 'q' ya basın.
*****************
""")

bakiye = 1000
while True:
    işlem = input("işlem seçiniz:")

    if (işlem == "q"):
        print("yine bekleriz...")
        break
    elif (işlem == "1"):
        print("bakiyeniz {} tldir.".format(bakiye))
    elif (işlem == "2"):
        miktar = int(input("miktarı giriniz:"))
        bakiye += miktar

    elif (işlem == "3"):
         miktar = int(input("miktarı giriniz:"))
         if (bakiye - miktar < 0 ):
            print("böyle bir miktar çekemezsiniz...")
            continue
         bakiye -= miktar
    else:
        print("geçersiz işlem.")
