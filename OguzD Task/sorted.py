def my_sort(iterable, key=None, reverse=False):
    return sorted(iterable, key=key, reverse=reverse)

# Test cases
print(my_sort([3, 2, 1]))  # [1, 2, 3]
print(my_sort(['apple', 'banana', 'cherry']))  # ['apple', 'banana', 'cherry']
print(my_sort(['apple', 'banana', 'cherry'], key=len))  # ['apple', 'cherry', 'banana']
print(my_sort(['apple', 'banana', 'cherry'], key=str.upper))  # ['apple', 'banana', 'cherry']
print(my_sort(['apple', 'banana', 'cherry'], key=str.upper, reverse=True))  # ['CHERRY', 'BANANA', 'APPLE']



"""

Bu kod, my_sort adlı bir fonksiyon tanımlar. Bu fonksiyon, Python'da yerleşik olarak bulunan sorted fonksiyonunun bir arayüzünü sağlar. sorted fonksiyonu, verilen bir iterable (örneğin liste) üzerinde sıralama yapar ve sıralanmış bir liste döndürür. my_sort fonksiyonu, aynı işlevi yapar, ancak sıralama sırasında kullanılacak bir anahtar fonksiyonu belirlemenizi ve sıralama yönünü (normal veya ters) belirlemenizi sağlar.

my_sort fonksiyonunun argümanları şunlardır:

iterable: Sıralanacak olan iterable (örneğin, liste)
key=None: Anahtar fonksiyonu. Varsayılan değeri None'dır.
reverse=False: Sıralama yönü. Varsayılan değeri False'dır (normal sıralama).
Fonksiyon, sıralama yapmak için Python'un yerleşik sorted fonksiyonunu çağırır ve argümanları iterable, key ve reverse olarak ayarlar. Sıralanmış liste, fonksiyon tarafından doğrudan döndürülür.

Sonra, birkaç test çağrısı yer alır, burada my_sort fonksiyonu, farklı iterable'lar ve anahtar fonksiyonları kullanılarak çağrılır ve sonuçlar ekrana yazdırılır.



"""
