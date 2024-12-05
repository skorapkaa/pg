def dec_to_bin(cislo):
    binarni_cislo = ""
    cislo = int(cislo)
    if cislo == 0:
        return "0"
    if cislo == 1:
        return "1"
    
    while cislo > 0:
        if cislo % 2 == 0:
            binarni_cislo += "0"
        else:
            binarni_cislo += "1"
        cislo = cislo // 2
                
    binarni_cislo = binarni_cislo[::-1]                
    return binarni_cislo


def test_bin_to_dec():
    assert dec_to_bin("0") == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin("100") == "1100100"
    assert dec_to_bin(101) == "1100101"
    assert dec_to_bin(127) == "1111111"
    assert dec_to_bin("128") == "10000000"
