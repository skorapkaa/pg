def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):

    if not (1 <= cilova_pozice[0] <= 8 and 1 <= cilova_pozice[1] <= 8):
        return False

    if cilova_pozice in obsazene_pozice:
        return False

    typ = figurka["typ"]
    pozice = figurka["pozice"]
    radek, sloupec = pozice
    cilovy_radek, cilovy_sloupec = cilova_pozice

    if typ == "pěšec":
        if sloupec == cilovy_sloupec:
            if cilovy_radek == radek + 1 and (cilovy_radek, cilovy_sloupec) not in obsazene_pozice:
                return True
            if radek == 2 and cilovy_radek == radek + 2 and (radek + 1, sloupec) not in obsazene_pozice and (cilovy_radek, cilovy_sloupec) not in obsazene_pozice:
                return True
        return False

    elif typ == "jezdec":
        if (abs(radek - cilovy_radek), abs(sloupec - cilovy_sloupec)) in [(2, 1), (1, 2)]:
            return True
        return False

    elif typ == "věž":
        if radek == cilovy_radek:
            krok = 1 if sloupec < cilovy_sloupec else -1
            for s in range(sloupec + krok, cilovy_sloupec, krok):
                if (radek, s) in obsazene_pozice:
                    return False
            return True
        elif sloupec == cilovy_sloupec:
            krok = 1 if radek < cilovy_radek else -1
            for r in range(radek + krok, cilovy_radek, krok):
                if (r, sloupec) in obsazene_pozice:
                    return False
            return True
        return False

    elif typ == "střelec":
        if abs(radek - cilovy_radek) == abs(sloupec - cilovy_sloupec):
            krok_radek = 1 if cilovy_radek > radek else -1
            krok_sloupec = 1 if cilovy_sloupec > sloupec else -1
            for i in range(1, abs(cilovy_radek - radek)):
                if (radek + i * krok_radek, sloupec + i * krok_sloupec) in obsazene_pozice:
                    return False
            return True
        return False

    elif typ == "dáma":
        if radek == cilovy_radek or sloupec == cilovy_sloupec:
            return je_tah_mozny({"typ": "věž", "pozice": pozice}, cilova_pozice, obsazene_pozice)
        elif abs(radek - cilovy_radek) == abs(sloupec - cilovy_sloupec):
            return je_tah_mozny({"typ": "střelec", "pozice": pozice}, cilova_pozice, obsazene_pozice)
        return False

    elif typ == "král":
        if max(abs(radek - cilovy_radek), abs(sloupec - cilovy_sloupec)) == 1:
            return True
        return False

    return False
    


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # True, při prvním tahu, může pěšec jít o 2 pole dopředu
    print(je_tah_mozny(pesec, (5, 2),
                       obsazene_pozice))  # False, protože pěšec se nemůže hýbat o tři pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

    print(je_tah_mozny(jezdec, (4, 4),
                       obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True
