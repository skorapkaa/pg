def cislo_text(cislo):
    cislo_str = str(cislo)
    prvni_index = ""
    druhy_index = ""

    if(cislo == '0'):
        return "nula"
    
    if(len(cislo_str)==3):
        return "sto"
    
    if(cislo == '11'):
        return "jedenáct"
    elif(cislo == '12'):
        return "dvanáct"
    elif(cislo == '13'):
            return "třináct"
    elif(cislo == '14'):
            return "čtrnáct"    
    elif(cislo == '15'):
            return "patnáct"
    elif(cislo == '16'):
            return "šestnáct"
    elif(cislo == '17'):
            return "sedmnáct"
    elif(cislo == '18'):
            return "osmnáct"
    elif(cislo == '19'):
            return "devatenáct"

    


    if(len(cislo_str) == 2):  
        if(cislo_str[0] == '2'):
            prvni_index = "dvacet"
        elif(cislo_str[0] == '3'):
            prvni_index = "třicet"
        elif(cislo_str[0] == '4'):
            prvni_index = "čtyřicet"                
        elif(cislo_str[0] == '5'):
            prvni_index = "padesát"
        elif(cislo_str[0] == '6'):
            prvni_index = "šedesát"                
        elif(cislo_str[0] == '7'):
            prvni_index = "sedmdesát"       
        elif(cislo_str[0] == '8'):
            prvni_index = "osmdesát"
        elif(cislo_str[0] == '9'):
            prvni_index = "devadesát"


    if(len(cislo_str) == 1 or cislo_str[1] != '0'):
        if(cislo_str[1] == "1"):
            druhy_index = " jedna"
        elif(cislo_str[1] == "2"):
            druhy_index = " dva"  
        elif(cislo_str[1] == "3"):
            druhy_index = " tři"  
        elif(cislo_str[1] == "4"):
            druhy_index = " čtyři"  
        elif(cislo_str[1] == "5"):
            druhy_index = " pět"  
        elif(cislo_str[1] == "6"):
            druhy_index = " šest"  
        elif(cislo_str[1] == "7"):
            druhy_index = " sedm"    
        elif(cislo_str[1] == "8"):
            druhy_index = " osm"  
        elif(cislo_str[1] == "9"):
            druhy_index = " devět"
            


    zaverecne_cislo = prvni_index + druhy_index



    
    return zaverecne_cislo

if __name__ == "__main__":
    cislo = int(input("Zadej číslo: "))
    while(cislo > 100 or cislo < 0):

        print("Číslo musí být mezi 0-100")
        cislo = int(input("Zadej číslo: "))

    cislo = str(cislo)

    
    text = cislo_text(cislo)
    print(text)
