'''
fun=lambda x:x**x
print(fun(2))
-----------------

srednia=lambda x,y:(x+y)/2
print(srednia(6,8))
---------------
fun=lambda x:x>10
print("Podana wartość jest wieksza od 10: ",fun(12))
-----------------

class nazwaklasy:
    pass
obiekt=nazwaklasy()
print(type(obiekt))
-----------------
class NazwaKlasy:

    def nazwa_metody(self, argument1, argument2):
        print(argument1)
        print(argument2)
-----------------

class MyClass:
    x=5
p1=MyClass()
print(p1.x)
-----------------


class Parrot:
    species="ptak" #atrybut klasy
    #atrybuty instancji
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sing(self,song):
        return self.name + " śpiewa "+song
    def dance(self):
        return self.name + " teraz tańczy"
#tworzenie instancji klasy parrot
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

print("Blu to",blu.__class__.species)
print("Woo to też",woo.__class__.species)

print(blu.name,"ma",blu.age)
print(woo.name,"ma",woo.age)
print(woo.sing("Wind of changes"))
-----------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def my_name(self):
        print("Cześć, mam na imię "+self.name)


p1=Person("Jan",36)
print(p1.name)
print(p1.my_name())
-----------------

class MyClass:
    x=5
p1=MyClass()
print(p1.x)
-----------------


class KontoBankowe:
    def __init__(self, nazwa, stan = 0):
        self.nazwa = nazwa
        self.stan = stan

    def info(self):
        print("nazwa:", self.nazwa)
        print("stan:", self.stan)

    def wyplac(self, ilosc):
        self.stan -= ilosc

    def wplac(self, ilosc):
        self.stan += ilosc
jk = KontoBankowe("Jan Kowalski", 1000)
jk.info()
jk.wplac(2000)
jk.wyplac(1500)
jk.info()
jk.stan=12000
jk.info()
-----------------


#zajęcia 23.02

class Jets:

    def __init__(self, name, country,maxspeed,mileage):
        self.name = name
        self.origin = country
        self.maxspeed = maxspeed
        self.mileage = mileage

jet1=Jets("F16","USA",240,18)
print(jet1.name)
print(jet1.origin)
print(jet1.maxspeed)
print(jet1.mileage)
-----------------


class Car:
    def __init__(self,color,mileage):
        self.color=color
        self.mileage=mileage

car1=Car("Niebieski",20000)
car2=Car("Czerwony",30000)
for car in (car1,car2):
    print(car.color + " samochód ma ",car.mileage," kilometrów przebiegu")
-----------------


class Jets:

    def __init__(self, name, country, quantity=0):
        self.name = name
        self.origin = country
        self.quantity=quantity
    def info(self):
        print("Nazwa: ",self.name)
        print("Pochodzenie: ",self.origin)
jet1=Jets("SU33","Rosja",)
jet2=Jets("AJS37","Szwecja",)
jet3=Jets("Mirage2000","Francja",35)
jet4=Jets("F14","USA",87)
jet5=Jets("MiG29","ZSRR",)
jet6=Jets("A10","USA",)
sum=0
for jet in (jet1,jet2,jet3,jet4,jet5,jet6):
    print(jet.info())
    sum+=jet.quantity
print("W sumie samolotów jest: ",sum)
-----------------


class Nobel:
    def __init__(self,category,year,winner):
        self.category=category
        self.year=year
        self.winner= winner
win1=Nobel("medicine",2021,"Thomas Perlmann")
win2=Nobel("physics",2021,"Goran Hansson")
win3=Nobel("literature",2021,"Mats Malm")
for win in (win1,win2,win3):
    print("W roku",win.year,"nagrodę Nobla w kategorii "+win.category+" zdobył "+win.winner+".")
-----------------


class Slowo:
    def __init__(self,slowo):
        self.slowo=slowo
    def odwracanie(self):
        return " ".join(reversed(self.slowo.split()))
slowo1=Slowo("hello .py")
print(slowo1.odwracanie())
-----------------

class Slowo:
    def get_string(self):
        self.word=input("Podaj slowo: ")
    def print_string(self):
        print(self.word.upper())
slowo1=Slowo()
slowo1.get_string()
print(slowo1.print_string())
-----------------


class Rectangle:
    def __init__(self,dlugosc,szerokosc):
        self.dlugosc=dlugosc
        self.szerokosc=szerokosc
    def pole(self):
        return self.dlugosc*self.szerokosc
w1=Rectangle(12,2)
print(w1.pole())
-----------------

import math
class Circle:
    def __init__(self,promien):
        self.promien=promien
    def pole(self):
        return math.pi*self.promien**2
    def obwod(self):
        return 2*math.pi*self.promien
kolo=Circle(10)
print(round(kolo.pole(),2))
print(round(kolo.obwod(),2))
-----------------

class Temperature:
    def convert_fahrenheit(self,cel):
        return (cel*(9/5)+32)
    def convert_celcius(self,far):
        -----------------


class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        self.age="undefined"
        self.marks="undefined"
    def display(self):
        print(self.name)
        print(self.roll)
        print(self.age)
        print(self.marks)
    def set_age(self,age):
        self.age=age

    def set_marks(self,marks):
        if marks >=2 and marks<=5:
            self.marks=marks
        else:
            print("Ocena poza zakresem!Wprowadz poprawna ocene")
student1=Student("Kamil",3452)
student1.display()
student1.set_age(23)
student1.set_marks(6)
student1.display()
        -----------------

import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("Wspolrzedna x:", self.x)
        print("Wspolrzedna y:", self.y)

    def move(self, x, y):
        self.x += x
        self.y += y

    def dist(self,z):
        return math.sqrt((self.x-z.x)**2+(self.y-z.y)**2)


p1 = Point(5, 10)
p2 = Point(2, 4)
print(p1.dist(p2))
p2.show()

        -----------------


class KontoBankowe:
    def __init__(self, nazwa, stan=0):
        self.nazwa = nazwa
        self.stan = stan

    def info(self):
        print("nazwa:", self.nazwa)
        print("stan:", self.stan)

    def wyplac(self, ilosc):
        self.stan -= ilosc

    def wplac(self, ilosc):
        self.stan += ilosc



class KontoDebetowe(KontoBankowe):
    def __init__(self, nazwa, stan=0, limit=0):
        KontoBankowe.__init__(self, nazwa, stan)
        self.limit = limit

    def wyplac(self, ilosc):
            """Jeżeli stan konta po operacji przekroczyłby limit, przerwij."""
        if (self.stan - ilosc) < (-self.limit):
            print("Brak srodkow na koncie")
        else:
            KontoBankowe.wyplac(self, ilosc)

account=KontoDebetowe("Jan Nowak",0,1000)
account.info()
account.wyplac(1000)
account.info()

    -----------------
'''

import math


class Figura:
    def obwod(self):  # L
        """Obliczanie obwodu."""
        raise NotImplementedError

    def pole(self):  # S/P
        """Obliczanie pola powierzchni."""
        raise NotImplementedError
f = Figura()
f.obwod()

class Kolo(Figura):
    def __init__(self,promien):
        self.promien=promien
    def obwod(self):
        return 2*math.pi*self.promien
    def pole(self):
        return math.pi*self.promien**2
kolo=Kolo(5)
print(kolo.obwod())
print(kolo.pole())