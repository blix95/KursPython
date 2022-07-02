
"""
def simple_function():
    print('Hello world!')
    print('Wikipedia')


simple_function()


def my_function():
    Dokumentacja funkcji
help(my_function)


def fibbonaci_numbers(n):
    ''' zwraca liczby Fibonacciego mniejsze od n '''
    wynik = []
    a, b = 0, 1
    # while a < n:
    while len(wynik) < n:
        wynik.append(a)
        a, b = b, a+b
    return wynik
x=fibbonaci_numbers(14)
print(x)



def dlugosc_lan(x):
    k=0
    for i in x:
        k+=1
    return k
print(dlugosc_lan("Domek"))



def suma(lista):
    sum=0
    for i in lista:
        sum+=i
    return sum
print(suma([10,5,6,]))


def mnozenie(lista):
    wynik=lista[0]
    for i in lista[1:]:
        wynik*=i
    return wynik

print(mnozenie([2,3,4,2]))


def licz_max(lista):
    a=lista[0]
    for i in lista[1:]:
        if a<i:
            a=i
    return a
print(licz_max([1,2,4,23,5]))



def liczba(ciag):
    slowo={}
    for i in ciag:
        if i in slowo.keys():
            slowo[i]+=1
        else:
            slowo[i]=1
    return slowo
print(liczba("google.com"))


def zlicz(slowa):
    x=0
    for i in slowa:
        if len(i)>=2 and i[0]==i[-1]:
            x+=1
    return x
print(zlicz(['abc', 'xyz', 'aba', '1221']))

def pozycja(krotka):
    return krotka[-1]
def sortowanie(lista):
    lista.sort(key=pozycja)
    return lista
print(sortowanie([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


def zwracanie(slowo):
    if len(slowo)<2:
        return ""
    else:
        return (slowo[:2]+slowo[-2:])
print(zwracanie("P"))


def silnia(n):
    if n==1:
        return 1
    return n*silnia(n-1)
print(silnia(5))

def fibbonaci(n):
    if n<2:
        return n
    return fibbonaci(n-2)+fibbonaci(n-1)
print(fibbonaci(4))
"""