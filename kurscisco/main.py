"""tajny_numer = 777

print(


+================================+
| Witaj w mojej grze, mugolu!    |
| Wprowadź liczbę całkowitą      |
| i zgadnij, jaki numer          |
| wybrałem dla ciebie.           |
| Jaki jest więc sekretny numer? |
+================================+
)
liczba=int(input("Wpisz liczbe calkowita: "))
while liczba!=tajny_numer:
    print("Nie, to nie jest ta liczba, którą wybrałem dla ciebie. Spróbuj ponownie!")
    if liczba<tajny_numer:
        print("Podaj większą liczbę")
    else:
        print("Podaj mniejszą liczbę")
    liczba = int(input("Wpisz liczbe calkowita: "))
print("Dobra robota! To numer, który wybrałem dla ciebie! Jesteś teraz wolny.")
print(tajny_numer)
---------------------


power=1
for exp in range(16):
    print("2 do potegi", exp, "wynosi", power)
    power*=2
  -------------
import time
for i in range(1,6):
    print(i, "Mississippi")
    time.sleep(1)
print("Szukam!")
  -------------------


print("Instrukcja przerywania")
for i in range(1,6):
    if i==3:
        continue
    print("Wewnątrz pętli.", i)
print("Poza pętlą.")
--------


najwieksza_liczba = -99999999
licznik = 0

while True:
    liczba = int(input("Wprowadz liczbe lub wpisz -1, aby zakonczyc: "))
    if liczba == -1:
        break
    licznik += 1
    if liczba > najwieksza_liczba:
        najwieksza_liczba = liczba

if licznik != 0:
    print("Najwieksza liczba wynosi", najwieksza_liczba)
else:
    print("Nie wprowadzono zadnej wartosci.")
    -------------

while True:
    slowo=input("Wprowadz haslo: ")
    if slowo=="pumpernikiel":
        print("Udało ci się opuścić pętlę.")
        break
------------

slowo_bez_samoglosek = ""
slowo_uzytkownika = input("Wprowadz slowo: ")
slowo_uzytkownika = slowo_uzytkownika.upper()
for litera in slowo_uzytkownika:
    if litera == "A":
        continue
    elif litera =="E":
        continue
    elif litera == "I":
        continue
    elif litera == "O":
        continue
    elif litera == "U":
        continue
    else:
        slowo_bez_samoglosek+=litera
print(slowo_bez_samoglosek)
-------------------------

i=5
while i<5:
    print(i)
    i+=1
else:
    print("else", i)
    -------------------

i=111
for i in range(2,1):
    print(i)
else:
    print("else:", i)
--------------------------


blokow=int(input("Wprowadz liczbę bloków: "))
wysokosc=0
warstwa=1
while warstwa<=blokow:
    blokow-=warstwa
    wysokosc+=1
    warstwa+=1
print("Wysokosc piramidy wynosi: ", wysokosc)
--------------------

c0=int(input("Podaj nieujemną liczbę różną od zera: "))
i=0
while c0>1:
    if c0%2==0:
        c0=c0/2
        i+=1
        print(int(c0))
    else:
        c0=3*c0+1
        i+=1
        print(int(c0))
print("Liczba krokow: ", i)

for i in range(1,11):
    if i%2==1:
        print(i)
    continue



x=1
while x<11:
    if x % 2 == 1:
        print(x)
    x+=1


for ch in "john.smith@pythoninstitute.org":
    if ch=="@":
        break
    print(ch,end="")


for cyfra in "0165031806510":
    if cyfra=="0":
        cyfra="x"
        print(cyfra, end="")
        continue
    else:
        print(cyfra, end="")


liczby=[10,5,7,2,1]
print("Zawartość listy:", liczby)
liczby[0]=111
liczby[1]=liczby[4]
print("Nowa zawartość listy: ", liczby)



liczby_z_kapelusza=[1,2,3,4,5]
liczby_z_kapelusza[int(len(liczby_z_kapelusza)/2)]=int((input("Wprowadz srodkowa wartośc: ")))
del liczby_z_kapelusza[-1]
print(liczby_z_kapelusza)
print(len(liczby_z_kapelusza))


moja_lista = [10, 1, 8, 3, 5]
suma = 0
for i in range(len(moja_lista)):
    suma+=moja_lista[i]
print(suma)


beatles=[]
print("Krok 1: ",beatles)
i=0
beatles.append(input("Wprowadz członków Beatlesów: "))
beatles.append(input("Wprowadz członków Beatlesów: "))
beatles.append(input("Wprowadz członków Beatlesów: "))
print("Krok 2: ",beatles)
for i in range(2):
    beatles.append(input("Wprowadz kolejnych członków Beatlesów: "))
    i+=1
print("Krok 3: ",beatles)
del beatles[-1],beatles[-1]
print("Krok 4: ",beatles)
beatles.insert(0,"Ringo Starr")
print("Krok 5: ",beatles)
-------------------
"""

swapped=True
lista = [8, 10, 6, 2, 4]
while swapped:
    swapped=False
    for i in range(len(lista)-1):
        if lista[i]>lista[i+1]:
            swapped=True
            lista[i],lista[i+1]=lista[i+1],lista[i]

print(lista)







