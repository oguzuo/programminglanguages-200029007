def my_map(func, iterable):
    result = []
    for item in iterable:
        result.append(func(item))
    return result


def test_my_map():
    result1 = my_map(lambda x: x ** 2, [1, 2, 3])
    print(result1)  # [1, 4, 9]
    
    result2 = my_map(lambda x: x.upper(), ["apple", "banana", "cherry"])
    print(result2)  # ["APPLE", "BANANA", "CHERRY"]
    
    result3 = my_map(len, ["apple", "banana", "cherry"])
    print(result3)  # [5, 6, 6]


test_my_map()





# adım 1 my_map adında bir fonksiyon tanımlanıyor. Bu fonksiyon, iki parametre alıyor: func ve iterable. func, bir fonksiyon nesnesi olacak ve iterable ise üzerinde işlem yapılacak elemanların bulunduğu bir iterable (liste, demet vb.) olacak.

# adım 2  result adında bir boş liste tanımlanıyor. Bu liste sonuçlar için kullanılacak.

# adım 3 iterable üzerinde bir for döngüsü kuruluyor ve her eleman için func fonksiyonu uygulanarak elde edilen sonuçlar result listesine ekleniyor.

# adım 4 Son olarak, result listesi return ediliyor.

# adım 5 test_my_map adında bir fonksiyon tanımlanıyor. Bu fonksiyon, my_map fonksiyonunun doğru çalışıp çalışmadığını test etmek için kullanılacak.

# adım 6 test_my_map fonksiyonu içinde, örnek kullanımlar oluşturuluyor ve print fonksiyonu kullanılarak sonuçlar ekrana yazdırılıyor.

# adım 7 test_my_map fonksiyonu sonlandırılıyor.
