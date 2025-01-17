#dictionart - sözlük veri yapısı
#kapsayıcıdır değiştirilebilir fakat sırasızdır

sozluk = {
    "AND" : "VE",
    "OR" : "VEYA",
    "YES" : "EVET",
    "NO"  : "HAYIR"
}
print(sozluk)

print(len(sozluk))

print(sozluk["AND"])

#yeni veri eklemek için aşağıdaki kullanılır. indislerle çalışmadığı için indis üzeirnden ekleme yapılamaz.

sozluk["TEST"] = "Test"
print(sozluk)
