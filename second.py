def cislo_text(cislo):
    if cislo == 0:
        return "nula"
    
    if cislo >= 100:
        return "sto" + ("" if cislo == 100 else " " + cislo_text(cislo % 100))
    
    if 10 < cislo < 20:
        teen_numbers = {
            11: "jedenáct", 12: "dvanáct", 13: "třináct",
            14: "čtrnáct", 15: "patnáct", 16: "šestnáct",
            17: "sedmnáct", 18: "osmnáct", 19: "devatenáct"
        }
        return teen_numbers[cislo]

    prvni_index = ""
    druhy_index = ""

    if cislo >= 20:
        tens = {
            2: "dvacet", 3: "třicet", 4: "čtyřicet", 
            5: "padesát", 6: "šedesát", 7: "sedmdesát", 
            8: "osmdesát", 9: "devadesát"
        }
        prvni_index = tens[cislo // 10]

    if cislo % 10 != 0:
        jednotky = {
            1: " jedna", 2: " dva", 3: " tři", 
            4: " čtyři", 5: " pět", 6: " šest", 
            7: " sedm", 8: " osm", 9: " devět"
        }
        druhy_index = jednotky[cislo % 10]
    
    return prvni_index + druhy_index

if __name__ == "__main__":
    cislo = int(input("Zadej číslo: "))
    while cislo > 100 or cislo < 0:
        print("Číslo musí být mezi 0-100")
        cislo = int(input("Zadej číslo: "))

    text = cislo_text(cislo)
    print(text)
