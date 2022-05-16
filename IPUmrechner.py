##IP Umrechner von dezimal zu binär und umgekehrt. Eine einfacherere Methode existiert bereits: https://docs.python.org/3/library/ipaddress.html#ipaddress.ip_address 
##dies entstand aus Lernzwecken

## dezimal zu binär

def dez_bin(InputIP):
    OktettList = InputIP.split(".")
    BinaerIP = []
    BinaerOktett = ""
 
    for n in range(0,4):
        DezimalOktett = int(OktettList[n])
        if DezimalOktett == 0:
            BinaerIP.append("00000000") 
            continue
        elif DezimalOktett > 0:
            while DezimalOktett > 0:
                Rest = DezimalOktett % 2 
                BinaerOktett +=(str(Rest))
                DezimalOktett //= 2
        BinaerOktett = BinaerOktett[::-1]    
        if len(BinaerOktett) < 8:
            while len(BinaerOktett) < 8:
                BinaerOktett = "0" + BinaerOktett
        BinaerIP.append(BinaerOktett)
        BinaerOktett = "" 
    BinaerIPString = "."         
    return BinaerIPString.join(BinaerIP)

##binär zu dezimal

def bin_dez(InputIP):
    BinaerListe = InputIP.split(".")
    DezimalIP = []
    BinaerTable= [     #Index:
                 128,  #0
                 64,   #1
                 32,   #2
                 16,   #3
                 8,    #4
                 4,    #5
                 2,    #6
                 1     #7
                 ]   

    for b in range(0,4):
        DezimalOktett = 0
        BinaerOktett = BinaerListe[b]
        for i in range(0,8):
            if "1" in BinaerOktett[i]:
                DezimalOktett += BinaerTable[i]
        DezimalIP.append(str(DezimalOktett))
    DezimalIPString = "."
    return DezimalIPString.join(DezimalIP)

## Chekt ob eingegebene IP gültig ist.
## Für binäre IP

def valid_bin(InputIP):
    import re
    validBinaerIP = re.compile("^[0-1]{8}[.]{1}[0-1]{8}[.]{1}[0-1]{8}[.]{1}[0-1]{8}$")
    if validBinaerIP.match(InputIP) is not None:
        Fehler = False
    else:
        Fehler = True 
        print("Die eingegebene IP (Binär) ist ungültig.")
    return Fehler            

## Für dezimal IP

def valid_dez(InputIP):
    import re
    validDezimalIP = re.compile("^[0-9]{1,3}[.]{1}[0-9]{1,3}[.]{1}[0-9]{1,3}[.]{1}[0-9]{1,3}$")
    if validDezimalIP.match(InputIP) is not None:
        InputIPList = InputIP.split(".")
        for c in range(0,3):
            if int(InputIPList[c]) > 255:
                Fehler = True 
                print("Die", str(c+1) + ".te", "eingegebene Zahl ist zu groß (>255).")
        if int(InputIPList[3]) > 254:
                Fehler = True 
                print("Die letzte eingegebene Zahl ist zu groß (>254).")
        else:
            Fehler = False
    elif validDezimalIP.match(InputIP) is None:
        Fehler = True
        print("Die eingegebene IP (Dezimal) ist ungültig.")
    return Fehler

## Das Hauptmenü
Terminate = False
while Terminate == False:
    print("Gebe 1 ein um von binär auf dezimal umzurechnen.")
    print("Gebe 2 ein um von dezimal auf binär umzurechnen.")
    print("Gebe \"terminate\" ein um den Rechner zu beenden.")
    print("Treffe eine Wahl.")
    InputAuswahl = input()

    if InputAuswahl == "terminate":
        Terminate = True 
 
    elif InputAuswahl == "1":
        print("Gebe eine gültige binäre IP ein. Format = xxxxxxxx.xxxxxxxx.xxxxxxxx.xxxxxxxx (nur binäre Zahlen 0 und 1).")
        InputIP = input() 
        binIPvalid = valid_bin(InputIP)
        if binIPvalid == False:
            print(bin_dez(InputIP))
  
    elif InputAuswahl == "2":
        print("Gebe eine gültige dezimale IP ein. Format = x.x.x.x (Zahlen von 1 bis 255. Maximal = 255.255.255.244).")
        InputIP = input() 
        binIPvalid = valid_dez(InputIP)
        if binIPvalid == False:      
            print(dez_bin(InputIP))
    else:
        print("Die Eingabe ist ungültig.")