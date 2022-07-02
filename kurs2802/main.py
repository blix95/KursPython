'''
import math


class Figura:
    def obwod(self):  # L
        """Obliczanie obwodu."""
        raise NotImplementedError

    def pole(self):  # S/P
        """Obliczanie pola powierzchni."""
        raise NotImplementedError


class Kolo(Figura):
    def __init__(self,promien):
        self.promien=promien
    def obwod(self):
        return 2*math.pi*self.promien
    def pole(self):
        return math.pi*self.promien**2

class Prostokat(Figura):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def obwod(self):
        return 2*(self.a+self.b)
    def pole(self):
        return self.a*self.b



class Kwadrat(Prostokat):
    def __init__(self,a):
        self.a=a
        self.b=a

class Trapez(Figura):
    def __init__(self,a,b,h):
        self.a,self.b,self.h=a,b,h
        self.c=math.sqrt(self.h**2+(self.a-self.b)**2)

    def obwod(self):
        return self.a + self.b + self.c + self.h
    def pole(self):
        return (self.a+self.b)*(self.h/2)
tr=Trapez(5,10,4)
print(tr.obwod())
print(tr.pole())

------------------------
class Vehicle:
    kolor="Biały"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"Liczba miejsc siedzących w {self.name} to {capacity} pasażerów"

class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)

class Car(Vehicle):
    pass



car1=Bus("Szkolne Volvo",180,12)
car2=Car("Audi Q5",230,209)
print(car1.kolor,car1.name,car1.max_speed,car1.mileage)
print(car2.kolor,car2.name,car2.max_speed,car2.mileage)
----------------


class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        x=super().fare()
        return 1.1*x

School_bus = Bus("Szkolne Volvo", 12, 50)
print("Całkowita opłata za przejazd autobusem wynosi:", School_bus.fare())
----------------


class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("Szkolne Volvo", 12, 50)

print(type(School_bus))

----------------


class Rectangle:

    def __init__(self, length, width):
        self.length=length
        self.width=width

    def perimeter(self):
        return 2*(self.length+self.width)

    def area(self):
        return self.width*self.length

    def display(self):
        print("Długość: ",self.length)
        print("Szerokość: ",self.width)
        print("Obwod: ",self.perimeter())
        print("Pole: ",self.area())

class Parallelepipede(Rectangle):
    def __init__(self,length,width,height):

        Rectangle.__init__(self,length,width)
        self.height=height
    def volume(self):
        return super().area()*self.height


f=Parallelepipede(2,5,10)
f.display()
print(f.volume())

----------------
'''

