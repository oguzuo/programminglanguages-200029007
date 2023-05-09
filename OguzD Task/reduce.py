def my_reduce(func, iterable):
    it = iter(iterable)
    value = next(it)
    for item in it:
        value = func(value, item)
    return value

def test_my_reduce():
    print(my_reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6])) # 21
    print(my_reduce(lambda x, y: x * y, [1, 2, 3, 4, 5, 6])) # 720
    print(my_reduce(lambda x, y: x + y, ["apple", "banana", "cherry"])) # "applebananacherry"

test_my_reduce()


# step 1 my_reduce isimli bir fonksiyon tanımlanıyor. Bu fonksiyon, iki argüman alıyor: func ve iterable
# step 2 it isimli bir değişkene iterable objesinin iterator'ı atanıyor.
# step 3 next fonksiyonu kullanılarak it iterator'ünden ilk eleman (value) alınıyor. Döngüde bu değerle işlemlere başlanacak.
# step 4 for döngüsü kullanılarak it iterator'ündeki tüm elemanlar tek tek alınıyor ve func fonksiyonu kullanılarak value değişkenine uygulanıyor.
# step 5 Son olarak, döngü sona erdikten sonra, value değişkeni fonksiyondan döndürülüyor.