#Funkce na rozpoznání sudých a lichých čísel
def sudy_nebo_lichy(cislo):
    if cislo%2==0:
        print(f"Čislo {cislo} je sudé")
    else:
        print(f"Číslo {cislo} je liché")

sudy_nebo_lichy(1000000)
sudy_nebo_lichy(5)    

