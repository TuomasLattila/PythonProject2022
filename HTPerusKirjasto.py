######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Tuomas Lättilä
# Opiskelijanumero:
# Päivämäärä: 6.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä HTPerusKirjasto.py

#versio = 1.0

import datetime
import sys

PAIVIA = 7
EROTIN = ";"
PAIVAT = ["Maanantai", "Tiistai", "Keskiviikko", "Torstai", "Perjantai", "Lauantai", "Sunnuntai"]

class LUETUTTIEDOT:
    pvm = None
    hinta = None

def kysyTiedosto(valinta):
    if valinta == 1:
        tiedosto = input("Anna luettavan tiedoston nimi: ")

    if valinta == 3 or valinta == 4:
        tiedosto = input("Anna kirjoitettavan tiedoston nimi: ")
    return tiedosto

def lueTiedosto(tiedostoR, oliolista):
    oliolista.clear()
    #LUETAAN TIEDOT JA LISÄTÄÄN NE OLIOLISTAAN
    try:
        tiedosto = open(tiedostoR, "r", encoding="utf-8")
        tiedosto.readline() #OTSIKKO

        while True:
            rivi = tiedosto.readline()
            if len(rivi) == 0:
                break
            rivi = rivi.strip("\n")
            rivi = rivi.split(EROTIN)
            
            luetutTiedot = LUETUTTIEDOT()
            luetutTiedot.pvm = datetime.datetime.strptime(rivi[0], '"%Y-%m-%d %H:%M:%S"')
            luetutTiedot.hinta = float(rivi[1])
            oliolista.append(luetutTiedot)

        tiedosto.close()
        print("Tiedosto '" + tiedostoR + "' luettu.")
        
    except Exception:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(tiedostoR))
        sys.exit(0)
    return oliolista

def tilastoAnalyysi(oliolista, tuloslista):
    tuloslista.clear()
    arvolista = []
    pvmlista = []

    #ANALYSOIDAAN TILASTOTIEDOT
    for luetutTiedot in oliolista:
        arvolista.append(luetutTiedot.hinta)
        pvmlista.append(luetutTiedot.pvm)
        
    lkm = len(oliolista)
    keskihinta = round(sum(arvolista)/lkm, 1)
    
    hintaH = round(min(arvolista), 2)
    indeksiH = arvolista.index(hintaH)
    pvmH = pvmlista[indeksiH].strftime("%d.%m.%Y %H:%M")
    
    hintaK = round(max(arvolista), 2)
    indeksiK = arvolista.index(hintaK)
    pvmK = pvmlista[indeksiK].strftime("%d.%m.%Y %H:%M")

    #LISÄTÄÄN TILASTOTIEDOT TULOSLISTAAN
    tuloslista.append("Analyysin tulokset {0:d} tunnilta ovat seuraavat:".format(lkm))
    tuloslista.append("Sähkön keskihinta oli {0:.1f} snt/kWh.".format(keskihinta))
    tuloslista.append("Halvimmillaan sähkö oli {0:.2f} snt/kWh, {1:s}.".format(hintaH, pvmH))
    tuloslista.append("Kalleimmillaan sähkö oli {0:.2f} snt/kWh, {1:s}.".format(hintaK, pvmK))
    tuloslista.append("")
    tuloslista.append("Päivittäiset keskiarvot (Pvm;snt/kWh):")

    arvolista.clear()
    pvmlista.clear()
    print("Tilastotietojen analyysi suoritettu {0:d} alkiolle.".format(len(oliolista)))
    return tuloslista
        
def paivittaisetAnalyysi(oliolista, tuloslista):
    arvo = 0
    maara = 0
    paivia = 0

    #ANALYSOIDAAN JA LISÄTÄÄN TULOSLISTAAN PÄIVITTÄISET KESKIARVOT
    verrattava_Pv = oliolista[0].pvm.strftime("%d.%m.%Y")
    for luetutTiedot in oliolista:
        pv = luetutTiedot.pvm.strftime("%d.%m.%Y")

        if pv != verrattava_Pv:
            keskiarvo = round(arvo/maara, 1)
            pvm = verrattava_Pv
            tuloslista.append("{0:s}{1:s}{2:.1f}".format(pvm, EROTIN, keskiarvo))
            arvo = 0
            maara = 0
            paivia += 1

            verrattava_Pv = pv
        
        arvo += luetutTiedot.hinta
        maara += 1

    #LISÄTÄÄN LISTAAN VIIMEISEN PÄIVÄN TIEDOT
    keskiarvo = round(arvo/maara, 1)
    pvm = pv
    tuloslista.append("{0:s}{1:s}{2:.1f}".format(pvm, EROTIN, keskiarvo))
    paivia += 1
    
    print("Päivittäiset keskiarvot laskettu {0:d} päivälle.".format(paivia))
    return tuloslista

def kirjoitaTiedot(tiedostoW, lista):
    try:
        tiedosto = open(tiedostoW, "w", encoding="utf-8")
        for tulos in lista:
            tiedosto.write(tulos + "\n")

        tiedosto.close()
        print("Tiedosto '{0:s}' kirjoitettu.".format(tiedostoW))
        
    except Exception:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(tiedostoW))
        sys.exit(0)
    return None

def viikonpaivaAnalyysi(oliolista, tuloslista2):
    tuloslista2.clear()
    arvolista = []
    maaralista =[]

    #LUODAAN OLIOLISTA
    for i in range(PAIVIA):
        arvolista.append(0)
        maaralista.append(0)
        
    #LAJITELLAAN TIEDOT OLIOLISTAAN OIKEILLE PAIKOILLE   
    for luetutTiedot in oliolista:
        arvolista[luetutTiedot.pvm.weekday()] += luetutTiedot.hinta
        maaralista[luetutTiedot.pvm.weekday()] += 1

    #LISÄTÄÄN KIRJOITETTAVAAN LISTAAN TEKSTIT
    tuloslista2.append("Viikonpäivä;Keskimääräinen hinta snt/kWh")
    for x in range(PAIVIA):
        if maaralista[x] == 0:
            arvo = 0
            tuloslista2.append("{0:s}{1:s}{2:.1f}".format(PAIVAT[x], EROTIN, arvo))
        else:
            arvo = round(arvolista[x]/maaralista[x], 1)
            tuloslista2.append("{0:s}{1:s}{2:.1f}".format(PAIVAT[x], EROTIN, arvo))
        
    arvolista.clear()
    maaralista.clear()
    return tuloslista2

######################################################################
# eof
