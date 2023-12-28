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
# Tehtävä HTPerus.py

import HTPerusKirjasto


def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Lue tiedosto")
    print("2) Analysoi")
    print("3) Kirjoita tiedosto")
    print("4) Analysoi viikonpäivittäiset keskiarvot")
    print("0) Lopeta")
    try:
        valinta = int(input("Anna valintasi: "))
    except Exception:
        valinta = ""
    return valinta

def paaohjelma():
    oliolista = []
    tuloslista = []
    tuloslista2 = []

    while True:
        valinta = valikko()
        
        if valinta == 1:
            tiedostoR = HTPerusKirjasto.kysyTiedosto(valinta)
            oliolista = HTPerusKirjasto.lueTiedosto(tiedostoR, oliolista)

        elif valinta == 2:
            if len(oliolista) == 0:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")
            else:
                tuloslista = HTPerusKirjasto.tilastoAnalyysi(oliolista, tuloslista)
                tuloslista = HTPerusKirjasto.paivittaisetAnalyysi(oliolista, tuloslista)

        elif valinta == 3:
            if len(tuloslista) == 0:
                print("Ei tietoja tallennettavaksi, analysoi tiedot ennen tallennusta.")
            else:
                tiedostoW = HTPerusKirjasto.kysyTiedosto(valinta)
                HTPerusKirjasto.kirjoitaTiedot(tiedostoW, tuloslista)

        elif valinta == 4:
            if len(oliolista) == 0:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")
            else:
                tiedostoW = HTPerusKirjasto.kysyTiedosto(valinta)
                tuloslista2 = HTPerusKirjasto.viikonpaivaAnalyysi(oliolista, tuloslista2)
                HTPerusKirjasto.kirjoitaTiedot(tiedostoW, tuloslista2)

        elif valinta == 0:
            print("Lopetetaan.")
            print()
            break

        else:
            print("Tuntematon valinta, yritä uudestaan.")
            
        print()
        
    oliolista.clear()
    tuloslista.clear()
    tuloslista2.clear()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

######################################################################
# eof
