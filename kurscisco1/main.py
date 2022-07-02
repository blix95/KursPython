'''
kwota=int(input("Wprowadz kwote: "))
czas=int(input("Podaj czas inwestycji: "))
zwrot=round(kwota*(1.1**czas),2)
print("Chcesz zainwestować ",kwota,"zł na okres", czas, "lat")
print("Po ",czas,"latach otrzymasz ", zwrot, "zł.")
###
word="Python"
print(word[::-1])


name=input("Podaj swoje imię i nazwisko: ")
age=input("Podaj swój wiek: ")
print("Nazywasz się", name, "i masz", age ,"lat")


tel={}
tel={'Maja': 50004, 'Jasio':12313}
print(tel)
tel['Ola']=102123
print(tel)
del tel['Maja']


str1="Datatypes"
str2="FullStack"
middle=int(len(str2)/2)
print(str2[middle-1:middle+2])

s1="FullStack"
s2="Python"

l=len(s1)
middle=l//2
s3=s1[0:middle]+s2+s1[middle:]
print(s3)

s1="America"
s2="Japan"
ls1=len(s1)
ls2=len(s2)
ms1=ls1//2
ms2=ls2//2
s3=s1[0]+s2[0]+s1[ms1]+s2[ms2]+s1[-1]+s2[-1]
print(s3)

tuple1 = (10, 20, 30, 40, 50)

tuple1[::-1]
print(tuple1[::-1])

tuple1 = ("Pomarańczowy", [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])


kursanci=["Kasia","Asia","Gosia","Zosia","Wacek"]
kursanci.sort()
print(kursanci)
print(len(kursanci))

keys = ['Dziesieć', 'Dwadzieścia', 'Trzydzieści']
values = [10, 20, 30]
tuple1=dict(zip(keys,values))
print(tuple1)


sample_set = {"Żółty", "Pomarańczowy", "Czarny"}
sample_list = ["Niebieski", "Zielony", "Czerwony"]

sample_set.update(sample_list)
print(sample_set )



a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
print("Iloraz tych liczb to: ", round(a/b,2))
print("Reszta z dzielenia tych liczb to: ", a%b)
print("Wynik dzielenia całkowitego tych liczb to: ", a//b)



x=5
print(x>4 or x<3)


def fibbonaci(n):
    wynik = []
    a, b = 0, 1
    while a<n:
        wynik.append(a)
        a, b = b, a+b
    return wynik
x= fibbonaci(10)
print(x)



def lenght(str):
    count = 0
    for char in str:
        count+=1
    return count

print(lenght('Python'))

def sum(tab):
    suma = 0
    for i in tab:
        suma += i
    return suma

x=[1,2,3,4,5]
print(sum(x))


def maks(x):
    maks=x[0]
    for i in x[1:]:
        if i > maks:
            maks = i;
    return maks

tab=[1,10,-2,8,-4]
print(maks(tab))


def char_frequency(str):
    dict={}
    for n in str:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

print(char_frequency('google.com'))


def length(tab):
    count = 0
    for str in tab:
        if len(str)>2 and str[0] == str[-1]:
            count += 1
    return count

tab=['abc', 'xyz', 'aba', '1221']
print(length(tab))



def ostatnia(tab):
    return tab[-1]

def sortowanie(x):
    return sorted(x,key=ostatnia)
print(sortowanie([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))



def minimum(tab):
    min=tab[0]
    for i in tab[1:]:
        if i<min:
            min=i
        else:
            pass
    return min

print(minimum([2,0,-3,4,10]))
'''
