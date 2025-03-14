import math

def calculator():
    print("Gelişmiş Hesap Makinesi")
    print("İşlemler:")
    print("1. Toplama (+)")
    print("2. Çıkarma (-)")
    print("3. Çarpma (*)")
    print("4. Bölme (/)")
    print("5. Üs Alma (^)")
    print("6. Karekök (√)")
    print("7. Logaritma (log)")
    print("8. Sinüs (sin)")
    print("9. Kosinüs (cos)")
    print("10. Tanjant (tan)")
    print("11. Faktöriyel (!)")
    print("12. Çıkış")

    while True:
        choice = input("Yapmak istediğiniz işlemi Seçiniz: ")
        if (choice == '12'):
            print("Çıkış Yapılıyor...")
            break

        if (choice in ('1','2','3','4','5')):
            num1 = float(input("Birinci sayıyı giriniz:"))
            num2 = float(input("İkinci sayıyı giriniz:"))

            if (choice == '1'):
                print(f"Sonuç: {num1 + num2}")
            elif (choice == '2'):
                print(f"Sonuç: {num1 - num2}")
            elif (choice == '3'):
                print(f"Sonuç: {num1 * num2}")
            elif (choice == '4'):
                if (num2 != 0):
                    print(f"Sonuç: {num1 / num2}")
                else:
                    print("Hata: 0'a bölme hatası!")
            elif(choice == '5'):
                print(f"Sonuç: {num1 ** num2}")

        elif (choice in('6', '7', '8', '9', '10', '11')):
            num = float(input("Sayıyı girin: "))

            if (choice == '6'):
                if (num >= 0):
                    print(f"Sonuç: {math.sqrt(num)}")
                else:
                    print("Negatif sayıların karekökü alınamaz!")
            elif (choice == '7'):
                if (num > 0):
                    print(f"Sonuç: {math.log(num)}")
                else:
                    print("Hata:Logaritma negatif veya sıfırdan küçük sayılar için tanımsızdır.")
            if (choice == '8'):
                print(f"Sonuç: {math.sin(math.radians(num))}")
            elif (choice == '9'):
                print(f"Sonuç: {math.cos(math.radians(num))}")
            elif (choice == '10'):
                print(f"Sonuç: {math.tan(math.radians(num))}")
            elif (choice == '11'):
                if (num > 0 and num == int(num)):
                    print(f"Sonuç: {math.factorial(int(num))}")
                else:
                    print("Hata:Faktöriyel yalnızca pozitif tam sayıları hesaplayabilir.")

    else:
        print("Geçersiz giriş,lütfen tekrar deneyiniz")

if __name__ == "__main__":
    calculator()





























