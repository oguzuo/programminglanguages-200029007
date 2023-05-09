def my_filter(func, iterable):
    result = []
    for item in iterable:
        if func(item):
            result.append(item)
    return result


def test_my_filter():
    result1 = my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])
    print(result1)  # [2, 4, 6]
    
    result2 = my_filter(lambda x: len(x) > 5, ["apple", "banana", "cherry", "durian"])
    print(result2)  # ["banana", "durian"]
    
    result3 = my_filter(lambda x: x.isalpha(), ["apple", "123", "cherry", ""])
    print(result3)  # ["apple", "cherry"]


test_my_filter()


# adım 1  my_filter adında bir fonksiyon tanımlanıyor. Bu fonksiyon, iki argüman alıyor: birincisi bir fonksiyon, ikincisi ise bir iterable.
# adım 2 result adında bir boş liste oluşturuluyor. Bu liste, filtrelenmiş sonuçların saklanacağı yerdir.
# adım 3 iterable üzerinde döngü oluşturuluyor ve her eleman için if koşulu kontrol ediliyor. Bu koşul, elemanın fonksiyondaki belirli bir kriteri karşılaması durumunda True değerini döndüren func fonksiyonu tarafından belirlenir.
# adım 4 Koşul sağlandığında, eleman result listesine eklenir.
# adım 5 Son olarak, result listesi döndürülür.
# test_my_filter adında bir fonksiyon daha tanımlanıyor. Bu fonksiyon, my_filter fonksiyonunun örneklerini içeriyor ve sonuçlarını print fonksiyonu kullanarak ekrana yazdırıyor.