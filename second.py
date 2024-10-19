def dej_cislo(cislo):
    cislo = int(cislo)

    if cislo == 100:
        return "sto"

    if 11 <= cislo <= 19:
        if cislo == 11:
            return "jedenáct"
        elif cislo == 12:
            return "dvanáct"
        elif cislo == 13:
            return "třináct"
        elif cislo == 14:
            return "čtrnáct"
        elif cislo == 15:
            return "patnáct"
        elif cislo == 16:
            return "šestnáct"
        elif cislo == 17:
            return "sedmnáct"
        elif cislo == 18:
            return "osmnáct"
        elif cislo == 19:
            return "devatenáct"

    desitky = ""
    if 20 <= cislo < 30:
        desitky = "dvacet"
    elif 30 <= cislo < 40:
        desitky = "třicet"
    elif 40 <= cislo < 50:
        desitky = "čtyřicet"
    elif 50 <= cislo < 60:
        desitky = "padesát"
    elif 60 <= cislo < 70:
        desitky = "šedesát"
    elif 70 <= cislo < 80:
        desitky = "sedmdesát"
    elif 80 <= cislo < 90:
        desitky = "osmdesát"
    elif 90 <= cislo < 100:
        desitky = "devadesát"


    jednotky = cislo % 10
    if jednotky == 1:
        jednotky_text = "jedna"
    elif jednotky == 2:
        jednotky_text = "dva"
    elif jednotky == 3:
        jednotky_text = "tři"
    elif jednotky == 4:
        jednotky_text = "čtyři"
    elif jednotky == 5:
        jednotky_text = "pět"
    elif jednotky == 6:
        jednotky_text = "šest"
    elif jednotky == 7:
        jednotky_text = "sedm"
    elif jednotky == 8:
        jednotky_text = "osm"
    elif jednotky == 9:
        jednotky_text = "devět"
    else:
        jednotky_text = ""


    if cislo == 1:
        return "jedna"
    elif cislo == 2:
        return "dva"
    elif cislo == 3:
        return "tři"
    elif cislo == 4:
        return "čtyři"
    elif cislo == 5:
        return "pět"
    elif cislo == 6:
        return "šest"
    elif cislo == 7:
        return "sedm"
    elif cislo == 8:
        return "osm"
    elif cislo == 9:
        return "devět"
    elif cislo == 10:
        return "deset"

    if desitky and jednotky_text:
        return desitky + " " + jednotky_text
    elif desitky:
        return desitky
    elif jednotky_text:
        return jednotky_text

    return "Neplatné číslo"

if __name__ == "__main__":
    cislo = input("Zadej číslo od 1 do 100: ")
    text = dej_cislo(cislo)
    print(text)
