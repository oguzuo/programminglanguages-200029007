def compose(*funcs):
    def inner(arg):
        for f in reversed(funcs):
            arg = f(arg)
        return arg
    return inner


def square(x):
    return x * x

def add_one(x):
    return x + 1

def test_compose():
    composed = compose(square, add_one, square)
    result1 = composed(2)
    result2 = composed(3)
    result3 = composed(4)
    print(result1, result2, result3)

test_compose()


"""



compose, *args sözdizimi kullanarak herhangi bir sayıda işlevi argüman olarak alan bir fonksiyondur.
İç içe fonksiyon, compose fonksiyonunun içinde tanımlanır ve tek bir argüman alır.
İç içe fonksiyonun içinde, fonksiyonlar funcs üzerinde ters sırada yinelendiği bir for döngüsü kullanılır.
Döngü içinde, arg argümanı her bir işleve aktarılır ve sonuç arg içinde güncellenerek saklanır.
Döngü tamamlandığında sonuç döndürülür.
İç içe fonksiyon, compose fonksiyonunun sonucu olarak döndürülür.
Kare ve add_one fonksiyonları, compose fonksiyonunun dışında tanımlanmıştır.
test_compose fonksiyonu, square, add_one ve square işlevlerini argüman olarak kullanarak compose fonksiyonunu çağırır ve sonuç olarak oluşan fonksiyonu composed olarak atar.
test_compose fonksiyonu, farklı argümanlarla composed fonksiyonunu üç kez çağırır ve sonuçları konsola yazdırır.


"""