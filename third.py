import math

def je_prvocislo(cislo):

    if cislo <= 1:
        return False
    for i in range(2, int(math.sqrt(cislo)) + 1):
        if cislo % i == 0:
            return False
    return True

def vrat_prvocisla(maximum):

    seznam_prvocisel = []
    for cislo in range(2, maximum + 1):
        if je_prvocislo(cislo):
            seznam_prvocisel.append(cislo)
    return seznam_prvocisel

if __name__ == "__main__":
    cislo = int(input("Zadej maximum: "))
    prvocisla = vrat_prvocisla(cislo)
    print(prvocisla)
    cislo2 = int(input("Zadej číslo: "))
    print(je_prvocislo(cislo2))

