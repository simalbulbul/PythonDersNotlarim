#LİSTELER

#[] birbirinden farklı veri yapılarını da içinde barındırabilir.
#list()


notlar = [100,90,70,60]

print(notlar)
print(type(notlar)) #<class 'list'>

liste = [ "a", 19.3, 23]
print(len(liste))

print(type(liste)) #dizinin türünü belirler
print(type(liste[0])) #dizinin 0. indisinin türünü gösterir

genel_liste = [notlar,liste]
print(genel_liste)


notlar = [100,90,[70,60]] #bu dizinin içerisinde farklı bir dizi daha vardır. 2. dizinin içerisindeki elemanlara ulaşmak için de aşağıdaki method kullanılır.

print(notlar[2][0])
