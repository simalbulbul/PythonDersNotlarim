#LİSTELER

#[] birbirinden farklı veri yapılarını da içinde barındırabilir.
#list()
''''
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



# dizideki bir indisi değiştirme
liste2 = ["ali", "veli", "ahmet", "ayşe", "selma"]

print(len(liste2))

print(liste2[0:4])

liste2[2] = "ahmetin bsi"

print(liste2)



# diziye veri ekleme

liste4 = ["ali", "veli", "ahmet", "ayşe", "selma"]
liste4.append("şimal")
print(liste4)
liste4.remove("veli")
print(liste4)

# indekse göre eleman ekleme

liste8 = ["ali", "veli", "ahmet", "ayşe", "selma"] 
liste.insert(0,"selma")
print(liste)


# indekse göre eleman silme

liste9 = ["ali", "veli", "ahmet", "ayşe", "selma"] 
liste9.pop(3)
print(liste9)
'''