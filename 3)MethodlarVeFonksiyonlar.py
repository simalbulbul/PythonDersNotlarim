##########################

#len() methodu
#belirlenen string dizisinin kaç adet karakter içerdiği bilgisini döndürür
a = "Bilgisayar_Programcılığı"
print(a)
print(len(a))

##########################

#upper() ve lower() methodları
#belirlenen string dizisinin içindeki ifadenin hepsini büyük veya küçük hale getirir.

print(a.upper()) #büyütür
print(a.lower()) #küçültür

print(a.isupper()) #bu ifade büyük mü False
print(a.islower()) #bu ifade küçük mü False

##########################

#replace() methodu
#elimizdeki string dizisinin içerisindeki karakterlerle ilgili değişiklik yapmak istediğimizde kullanılır
#önce neyi değiştirmek istediğini, sonra neyle değiştirmek istediğini yazmalısın.

print(a.replace("a","e")) #metindeki a harflerini e harfi ile değiştir

##########################

#strip() methodu
#elimizdeki string değerlerinin sağ ve sol kısmındaki boşluk değerlerini temizler. kırpma yapar 

b= "   deneme    "
print(b.strip())

##########################

#dir() fonksiyonu
#üzerinde çalışılan veri tipine uygulanabilecek olan methodları gösterir

print(dir(a))