import time
def person():
    try:
        name = input("Lütfen bir isim giriniz: ")
        return name
    except ValueError:
        print("Hata! Lütfen bir isim giriniz.")
        time.sleep(2)
        person()

def age_value():
    try:
        age = int(input("Lütfen bir yaş giriniz: "))
        return age
    except ValueError:
        print("Hata! Lütfen bir yaş giriniz.")
        time.sleep(2)

def city():
    try:
        sehir = input("Lütfen şehrinizin adını giriniz: ")
        return sehir
    except ValueError:
        print("Hata! Lütfen bir şehir ismi giriniz.")
        time.sleep(2)
        city()

def cevap():
    name = person()
    age = age_value()
    sehir = city()
    try:
        print(f"İsminiz: {name}")
        print(f"Yaşınız: {age}")
        print(f"Yaşadığınız şehir: {sehir}")
        kontrol = input("Bu bilgiler doğru mu? (evet/hayır)")
        if kontrol == "evet":
            print("Programı kullandığınız için teşekkür ederiz!")
        elif kontrol == "hayır":
            asd = input("Hangi bilgiler yanlış? (şehir, yaş, isim şeklinde yazınız.)")
            try:
                if asd == "isim":
                    person()
                    cevap()
                elif asd == "şehir":
                    city()
                    cevap()
                elif asd == "yaş":
                    age_value()
                    cevap()
                else:
                    print("Lütfen geçerli bir seçenek seçiniz!")
            except ValueError:
                print("Hata! Lütfen yazı yazınız.")
            return asd
        else:
            print("Lütfen geçerli bir seçenek seçiniz!")
            cevap()

        return kontrol
    except ValueError:
        print("Bir hata ile karşılaşıldı!")

cevap()
