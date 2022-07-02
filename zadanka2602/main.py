'''
class Karta:

    symbole=["A","K","D","J","10","9","8","7","6","5","4","3","2"]
    kolory=["pik","kier","trefl","karo"]

    def __init__(self, symbol, kolor):
        self.symbol = symbol
        self.kolor = kolor

    def __str__(self):
        rep=self.symbol + self.kolor
        return rep

class Talia:
    def __init__(self):
        self.karty = []


    def __str__(self):
        if self.karty:
            rep = ""
            for karta in self.karty:
                rep += str(karta) + " "
        else:
            rep = "<pusta>"
        return rep

    def dodaj(self,karta):
        self.karty.append(karta)

    def wypelnij(self):
        for kolor in Karta.kolory:
            for symbol in Karta.symbole:
                self.dodaj(Karta(symbol,kolor))


talia1 = Talia()
print("utworzylem nowa talie: ")
print(talia1)
print("\n lecz jest ona poki co pusta...")
talia1.wypelnij()
print(talia1)
------------------

class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def dodawanie(self,z):
        self.z=z
        return (self.x+z.x,self.y+z.y)
    def odejmowanie(self,z):
        self.z=z
        return (self.x-z.x,self.y-z.y)
    def mnozenie(self,k):
        self.k=k
        return (self.x*k,self.y*k)

vec1=Vector(2,3)
vec2=Vector(2,4)
print(vec1.dodawanie(vec2))
print(vec1.odejmowanie(vec2))
print(vec1.mnozenie(2))
----------------


class Product1:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def details(self):
        print(self.name,":",self.price)
class Product2:
    def utworz(self,name,price):
        self.name=name
        self.price=price
    def details(self):
        print(self.name,": ",self.price)
produkt1=Product1("ryż",12)
produkt2=Product2()
produkt2.utworz("chleb",10)
produkt1.details()
produkt2.details()
----------------


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
    def przelew(self,adresat,kwota=0):
        self.aresat=adresat
        self.kwota=kwota
        adresat.stan+=self.kwota
        self.stan-=self.kwota
konto1= KontoBankowe("Jan Kowalski", 1000)
konto2=KontoBankowe("Klara Sobieraj",2000)
konto1.przelew(konto2,10000)
print(konto2.stan)
print(konto1.stan)
----------------


thing = ["a", "b", "c"]

for i, item in enumerate(thing):
    result = str(i)+item
    thing[i] = result
print(thing)

----------------


t = (10,20,10,40,50,60,70)
v = 50
result=[]
for i,item1 in enumerate(t):
    for j,item2 in enumerate(t):
        sum=item1+item2
        if sum==v:
            result.append((i,j))
        else:
            continue
print(result)
----------------

t = (10,20,10,40,50,60,70)
v = 50
class PySolution:
    def suma(self,liczby,cel):
        result=[]
        for i, item1 in enumerate(liczby):
            for j, item2 in enumerate(liczby):
                sum = item1 + item2
                if sum == cel:
                    result.append((i, j))
                else:
                    continue
        print(result)
p=PySolution()
p.suma(t,v)
----------------

a=10
b=20
a,b=b,a
print(a,b)
----------------

a=int(input("Podaj pierwsza liczbe: "))
b=int(input("Podaj pierwsza liczbe: "))
c=int(input("Podaj pierwsza liczbe: "))
srednia=(a+b+c)/3
print("Średnia: ",srednia)
----------------


class Crypto:
    def calculate(self,amount):
        self.amount=amount
        eth=self.amount/25
        btc=self.amount/50
        ltc=self.amount/10
        print("Za",self.amount,"możesz kupić",btc,"BTC lub",eth,"ETH lub",ltc,"LTC")
cash=Crypto()
cash.calculate(100)
----------------



class Zoll:
    def price(self,cost,duty):
        self.cost=cost
        self.duty=duty
        price=self.cost+0.01*self.cost*self.duty
        print("Cena netto: ",self.cost)
        print("Cena brutto: ",price)
laptop=Zoll()
laptop.price(3000,10)
----------------


lista=[]
lista.append(input("Podaj pierwsze słowo: "))
lista.append(input("Podaj pierwsze słowo: "))
lista.append(input("Podaj pierwsze słowo: "))
print(lista)
for word in lista:
    if word.endswith("a"):
        print(word)
    else:
        continue
----------------


zdanie="Miło było ale się skończyło"
zdanie_podzielone=list(zdanie.split())
for word in zdanie_podzielone:
    word1=word[1:]+word[0]
    print(word1,end=" ")
----------------


words=[]
words.append(input("Wprowadz slowo: "))
words.append(input("Wprowadz slowo: "))
words.append(input("Wprowadz slowo: "))
for word in words:
    if len(word)>5:
        print(word)
    else:
        continue
----------------


words=["HALAS","cisza","WOJNA"]
for word in words:
    if word.isupper():
        print(word)
    else:
        continue
----------------


words=["kajak","abba","zloto","zakaz"]
for word in words:
    if word == word[::-1]:
        print(word)
    else:
        continue
----------------


words="daj ać ja pobruszę a ty poczywaj"
wordslist=words.split()
for word in wordslist:
    if len(word)%2 == 0:
        print(word.upper(),end=" ")
    else:
        print(word,end=" ")

----------------


word="halfdead"
lenght=len(word)
letter="d"

for i,item in enumerate(word[::-1]):
    if item==letter:
        index=lenght-i-1
        print(index)
        break
----------------


for i in range(1,51):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")

    else:
        print(i)

----------------

import random

opcje=["papier","kamien","nozyce"]
class Gra:

    def losowy(self):
        self.los = random.choice(opcje)

    def kamien(self):
        self.wybor="kamien"

    def papier(self,):
        self.wybor = "papier"

    def nozyce(self):
        self.wybor = "nozyce"
    def wynik(self):
        if self.wybor != self.los:
            if self.wybor=="nozyce" and self.los == "kamien":
                    print("Wygrywa kamien")
            elif self.wybor=="nozyce" and self.los == "papier":
                    print("Wygrywają nozyce")
            elif self.wybor == "papier" and self.los == "kamien":
                    print("Wygrywa papier")
            else:
                    print("Wygrywa kamien")
        else:
                print("Remis")
komputer=Gra()
ja=Gra()
komputer.losowy()
print("Przeciwnik wybrał: ",komputer.losowy())
ja.papier()
ja.wynik()
----------------
'''
slownik={"a":1,"b":3,"c":2}
sort=[]
def sorted_dict_values(a):
















