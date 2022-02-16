print("Vücut kitle hesaplama uygulamasına hoşgeldiniz.\n")
boy = float(input("Lütfen boyunuzun uzunluğunu giriniz (Lütfen noktalı bir şekilde giriniz 1.80 gibi): "))
kilo = float(input("Lütfen kilonuzu giriniz: "))

boyCarpimi = boy * boy
bmi = kilo / boyCarpimi

yuvarlama = round(bmi,1) # burda float ile işlem yaptığımız için çok basamaklı sayı çıkıyor burda sadece 1 basamak alması için bir fonksiyon kullanıyoruz.
# print(yuvarlama)

if bmi == bmi < 18.49:
    print("Vücut kitle endeksiniz {} Normal kilonun altındasınız.".format(yuvarlama))

elif bmi == bmi > 18.5 and bmi < 24.99:
    print("Vücut kitle endeksiniz {} Kilonuz normal.".format(yuvarlama))

elif bmi == bmi > 25 and bmi < 29.99:
    print("Vücut kitle endeksiniz {} Kilonuz ideal kilonun üzerinde.".format(yuvarlama))

elif bmi == bmi > 30:
    print("Vücut kitle endeksiniz {} Kilonuz ideal kilonun çok üzerinde.".format(yuvarlama))

# python vucüt-kitle-endeksi.py