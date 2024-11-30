#Nejsou zde zadne vyjimky protote testovaci cisla jsou jasne dane. Popripade dodelam :D
def bin_to_dec(binarni_cislo):

    binarni_cislo = str(binarni_cislo)
    binarni_cislo = list(binarni_cislo[::-1])

    desitkove_cislo = 0


    for index, cislo in enumerate(binarni_cislo):
        if cislo == "1":
            desitkove_cislo += 2 ** index

    return desitkove_cislo


def test_funkce():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128
