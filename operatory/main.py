# a=int(input("Podaj pierwsza liczbe: "))
# b=int(input("Podaj druga liczbę: "))
# print(a/b)
# print(a%b)
# print(a//b)

'''
x=2
y=7
if x>3 or y%2==0:
    print("Co najmniej jeden warunekt jest spełniony")
elif x<=3 and y%2==1:
    print("Żaden warunek nie jest spełniony")
---------------
x=5
print(not(x>3 and x<10))
----------------

wartosc=2
wartosc="warunek spełniony" if wartosc!=2 else "warunek nie spełniony"
print(wartosc)

----------------
nice=True
personality=("wredny","miły")[nice]
print("Kot jest", personality)

-------------------
uczestnicy=["Dominik","Kasia","Kacper","Agnieszka","Kinga","Bartosz","Marta"]
uczestnicy.sort()
print(uczestnicy)
ilosckobiet=0
for imie in uczestnicy:
    print(imie)
    if imie[-1]=="a":
        ilosckobiet+=1
print("Ilość kobiet to: ",ilosckobiet)

-----------
for i in range(6):
    print(i)
else:
    print("Gotowe")

a=int(input("Podaj pierwsza liczbe: "))
b=int(input("Podaj druga liczbe: "))
while

'''

liczby=list()
for i in range(1500,2701):
    if i%7==0 and i%5==0:
        print(i)
        liczby.append(i)
print(liczby)